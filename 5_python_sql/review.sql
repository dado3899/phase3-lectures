CREATE TABLE journals(
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE authors(
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE articles(
    id INTEGER PRIMARY KEY,
    topic TEXT,
    date TEXT,
    author_id INTEGER,
    journal_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (journal_id) REFERENCES journals(id)
);