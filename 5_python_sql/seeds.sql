-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
DROP TABLE journals;
DROP TABLE authors;
DROP TABLE articles;

CREATE TABLE IF NOT EXISTS journals(
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY,
    topic TEXT,
    date TEXT,
    author_id INTEGER,
    journal_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (journal_id) REFERENCES journals(id)
);

INSERT INTO journals (name)
VALUES ("Flatiron Journal of science and shit");

INSERT INTO authors (name)
VALUES ("Sherina"), ("Mark");

INSERT INTO articles (topic,date,author_id,journal_id)
VALUES ("ORM", "second Tuesday of next week",2,1);



