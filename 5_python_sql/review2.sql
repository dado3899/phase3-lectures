INSERT INTO journals (name)
VALUES ("Flatiron Journal of science and shit");

INSERT INTO authors (name)
VALUES ("Sherina"), ("Mark");

SELECT * FROM authors
WHERE id = 1;

INSERT INTO articles (topic,date,author_id,journal_id)
VALUES ("ORM", "second Tuesday of next week",2,1);

SELECT journals.name, articles.topic, authors.name
FROM articles
JOIN authors, journals
ON articles.author_id = authors.id AND articles.journal_id = journals.id
