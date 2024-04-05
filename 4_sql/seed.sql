DROP TABLE if EXISTS students;
DROP TABLE if EXISTS teachers;
DROP TABLE if EXISTS classes;

CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER 
);
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,
    subject TEXT,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

INSERT INTO students(name,age)
VALUES ("Jonathan",24);
INSERT INTO students(name,age)
VALUES ("Jackson",21);
INSERT INTO students(name,age)
VALUES ("Sabrina",21);

INSERT INTO teachers(name,email)
VALUES ("David","d@flatiron.com");
INSERT INTO teachers(name,email)
VALUES ("Stephen","s@flatiron.com");

INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("CSS",1,2);
INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("PYTHON",2,1);
INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("REACT",3,1);
INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("PYTHON",1,1);
INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("PYTHON",3,1);
INSERT INTO classes(subject,student_id,teacher_id)
VALUES ("PYTHON",1,2);
