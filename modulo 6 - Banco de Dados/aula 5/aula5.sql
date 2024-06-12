
-- Selecione o título e o autor de todos os livros.
SELECT title, author FROM books;

-- Selecione os livros escritos por Henry Davis.
SELECT title FROM books WHERE author = 'Henry Davis';

-- Selecione o título, autor e ano dos livros publicados antes de 1900.
SELECT title, author, release_year FROM books WHERE release_year < 1900;

-- Selecione todos os livros cujo título comece com a letra "O".
SELECT * FROM books WHERE title ILIKE 'O%';

-- Selecione o título e o autor dos livros cujo ano seja posterior a 1950.
SELECT title, author FROM books WHERE release_year > 1950;

-- Selecione o número total de livros na tabela.
SELECT COUNT(*) FROM books;

-- Selecione o autor com o maior número de livros publicados.
SELECT author, COUNT(*) FROM books
GROUP BY author
ORDER BY COUNT(*) DESC;

-- Selecione os livros ordenados por ano em ordem ascendente.
SELECT title, release_year FROM books
ORDER BY release_year;

-- Selecione o título do livro mais antigo.
SELECT title FROM books 
WHERE release_year IN (SELECT MIN(release_year) FROM books) 
LIMIT 1;

-- Selecione o título do livro mais recente.
SELECT title FROM books 
WHERE release_year IN (SELECT MAX(release_year) FROM books)
LIMIT 1;

-- Selecione o título e o autor dos três últimos livros na tabela.
SELECT title, author FROM books 
ORDER BY id DESC
LIMIT 3;


-- Selecione a quantidade total de produtos em estoque.
SELECT SUM(quantity_in_stock) FROM products;

-- Selecione o preço médio dos produtos.
SELECT ROUND(AVG(price::NUMERIC),2)::MONEY FROM products;

-- Selecione o produto mais caro da tabela.
SELECT product FROM products
ORDER BY price DESC
LIMIT 1;

-- Selecione o produto mais barato da tabela.
SELECT product FROM products
ORDER BY price
LIMIT 1;

-- Selecione o valor do total do estoque (preço * estoque) para cada produto.
SELECT product, (price * quantity_in_stock) AS total_price_in_stock FROM products;

-- Selecione a quantidade de produtos que possuem estoque menor que 20.
SELECT COUNT(*) FROM products
WHERE quantity_in_stock < 20;

-- Selecione o produto com o maior retorno após a venda de todas as unidades em estoque.
SELECT 	product FROM products
ORDER BY (price * quantity_in_stock) DESC
LIMIT 1;


-- Selecione o nome e cargo de cada funcionário, juntamente com o departamento em que trabalham.
SELECT 
	e.name "funcionario", 
	e.role "cargo", 
	d.name "departamento"
from employees e
LEFT JOIN departments d on e.department_id = d.id;

-- Selecione o nome, o cargo e o salário dos funcionários do departamento de vendas.
SELECT 
	e.name "funcionario",
	e.role "cargo",
	e.salary "Salario"
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE d.name = 'Vendas';

-- Selecione o nome, o cargo e o salário dos funcionários cujo salário seja maior que 3500 e que trabalham no departamento de vendas.
SELECT
	e.name "funcionario",
	e.role "cargo",
	e.salary "salario"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE salary::numeric > 3500 AND d.name = 'Vendas';

-- Selecione o nome, o cargo, o salário e o nome do projeto associado a cada funcionário.
SELECT
    e.name "funcionario",
    e.role "cargo",
    e.salary "salario",
    STRING_AGG(p.name, ', ') AS "projetos"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN projects p ON p.department_id = d.id
GROUP BY e.id;

-- Liste o total gasto pela empresa no pagamento dos funcionários.
SELECT 	SUM(salary) FROM employees;

-- Liste o total de salário pago para os funcionários de cada departamento.
SELECT
	d.name "departamento",
	SUM(e.salary) "total do salario"
FROM departments d
INNER JOIN employees e
ON e.department_id = d.id
GROUP BY d.id;

-- Liste o maior salário de cada departamento.
SELECT 
	MAX(e.salary) "maior salario", 
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY d.id;











