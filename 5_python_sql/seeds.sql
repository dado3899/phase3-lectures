-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
-- DROP TABLE test;
-- DROP TABLE test2;

-- CREATE TABLE IF NOT EXISTS test(
--     id INTEGER PRIMARY KEY,
--     name TEXT
-- );

-- CREATE TABLE IF NOT EXISTS test2(
--     id INTEGER PRIMARY KEY,
--     test_id INTEGER,
--     FOREIGN KEY (test_id) REFERENCES test(id)
-- );


DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY,
    title TEXT
);
CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY,
    comment TEXT,
    post_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

INSERT INTO posts(title)
VALUES ("CSS 101");

INSERT INTO posts(title)
VALUES ("CSS Sucks");

INSERT INTO comments(comment,post_id)
VALUES ("try tailwind", 1);

INSERT INTO comments(comment,post_id)
VALUES ("try sass", 1);

INSERT INTO comments(comment,post_id)
VALUES ("u rite", 2);

INSERT INTO comments(comment,post_id)
VALUES ("no u", 2);
