-- Use .read filename to run this file!
-- We'll use this table to create a bunch of test data!
DROP TABLE students;
DROP TABLE teachers;
DROP TABLE schedules;

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    emergency_phone INTEGER
);

CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email INTEGER,
    specialty TEXT
);

CREATE TABLE IF NOT EXISTS schedules(
    id INTEGER PRIMARY KEY,
    classname TEXT,
    period INTEGER,
    grade FLOAT,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

INSERT INTO students(name, emergency_phone)
VALUES("Justin", 2222222222);
INSERT INTO students(name, emergency_phone)
VALUES("Grey", 1111111111);
INSERT INTO students(name, emergency_phone)
VALUES("Ben", 1000000000);

INSERT INTO teachers(name,email,specialty)
VALUES("David","d@gmail.com", "Python");

INSERT INTO teachers(name,email,specialty)
VALUES("Stephen","S@gmail.com", "JS");

INSERT INTO schedules(classname,period,student_id,teacher_id,grade)
VALUES ("Python 101",1,1,1,2.7);
INSERT INTO schedules(classname,period,student_id,teacher_id,grade)
VALUES ("Flask 101",2,1,1,4.0);
INSERT INTO schedules(classname,period,student_id,teacher_id,grade)
VALUES ("Big O",3,1,2,1.5);

