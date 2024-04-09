-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
-- DROP TABLE test;
-- DROP TABLE test2;

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,
    topic TEXT,
    grade FLOAT,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);




