# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import psycopg2


class FormatValuesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        monetary_keys = ("price_excl", "price_incl","tax")
        
        for key in monetary_keys:
            adapter[key] = self.format_money(adapter[key])
            
        adapter["rating"] = self.format_rating(adapter["rating"])
        
        adapter["availability"] = self.format_stock(adapter["availability"])
        
        adapter["image"] = self.format_image_url(adapter["image"])
        
        return item
    
    def format_image_url(self, value):
        formatted_value = re.sub(r"\.\./", "", value)
        
        return f"https://books.toscrape.com/{formatted_value}"

    def format_rating(self, value):
        return {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }[value]

    def format_money(self, value):
        return float(value[1:])

    def format_stock(self, value):
        formatted_value = re.findall(r"\d+", value)
        if formatted_value:
            return int(formatted_value[0])
        else:
            return 0
        
class PostgteSQLPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            dbname=crawler.settings.get("DB_NAME"),
            user=crawler.settings.get("DB_USER"),
            password=crawler.settings.get("DB_PASSWORD"),
            host=crawler.settings.get("DB_HOST"),
            port=crawler.settings.get("DB_PORT"),
        )
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host, 
            port=port
        )
        
        self.cursor = self.conn.cursor()
        
        create_query= """
        CREATE TABLE IF NOT EXISTS books(
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            image TEXT,
            name VARCHAR(255) NOT NULL,
            rating SMALLINT DEFAULT 0,
            price_excl NUMERIC(12,2) DEFAULT 0,
            price_incl NUMERIC(12,2) DEFAULT 0,
            tax NUMERIC(12,2) DEFAULT 0,
            availability SMALLINT DEFAULT 0,
            category VARCHAR(255)        
        );
        """
        self.cursor.execute(create_query)
        self.cursor.execute("TRUNCATE books RESTART IDENTITY;")
        self.conn.commit()
        
    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO books (
                url,
                image,
                name,
                rating,
                price_excl,
                price_incl,
                tax,
                availability,
                category
            ) VALUES(%s, %s, %s, %s,%s, %s, %s, %s, %s);
            """, (
                item["url"],
                item["image"],
                item["name"],
                item["rating"],
                item["price_excl"],
                item["price_incl"],
                item["tax"],
                item["availability"],
                item["category"]
            ))
        
        self.conn.commit()
        
        return item
        
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
