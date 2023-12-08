-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
DROP TABLE students;
DROP TABLE classes;
DROP TABLE joinclasses;

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
);

CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,
    topic TEXT
);

CREATE TABLE IF NOT EXISTS joinclasses(
    id INTEGER PRIMARY KEY,
    class_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

INSERT INTO students(name,grade)
VALUES("Juan",6);

INSERT INTO students(name,grade)
VALUES("Juan",5);

INSERT INTO students(name,grade)
VALUES("Juan",5);

INSERT INTO classes(topic)
VALUES("Juan");
INSERT INTO classes(topic)
VALUES("Juan");

INSERT INTO joinclasses(class_id,student_id)
VALUES (1,1);
INSERT INTO joinclasses(class_id,student_id)
VALUES (1,2);
INSERT INTO joinclasses(class_id,student_id)
VALUES (1,3);
INSERT INTO joinclasses(class_id,student_id)
VALUES (2,2);

