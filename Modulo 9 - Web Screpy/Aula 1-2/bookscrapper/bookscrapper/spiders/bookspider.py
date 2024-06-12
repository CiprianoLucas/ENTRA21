import scrapy

from bookscrapper.items import BookItem

class BookspyderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"] # Previne a Spider de seguir links de outros domínios
    start_urls = ["https://books.toscrape.com/"]
    
    def format_link(self, value):
        if "catalogue/" in value:
            return f"https://books.toscrape.com/{value}"
        
        return f"https://books.toscrape.com/catalogue/{value}"

    def parse(self, response):
        books = response.css("article.product_pod")
        
        for book in books:
            book_page_url = self.format_link(book.css("h3 > a::attr(href)").get())
            
            yield response.follow(book_page_url, callback=self.parse_book_page)
        
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:   
            next_page_url = self.format_link(next_page)            
                 
            yield response.follow(next_page_url, callback=self.parse)
            
    def parse_book_page(self, response):
        
        yield BookItem(
            url=response.url,
            image=response.css("#product_gallery img::attr(src)").get(),
            name=response.css("h1::text").get(),
            rating=response.css("p.star-rating::attr(class)").get().split()[1],
            price_excl=response.css("table tr:nth-of-type(3) td::text").get(),
            price_incl=response.css("table tr:nth-of-type(4) td::text").get(),
            tax=response.css("table tr:nth-of-type(5) td::text").get(),
            availability=response.css("table tr:nth-of-type(6) td::text").get(),
            category=response.css(".breadcrumb li:nth-of-type(3) a::text").get(),
        )
        
        
