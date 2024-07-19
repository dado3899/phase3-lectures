CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email INTEGER,
    grade_level INTEGER
);

CREATE TABLE schedules(
    id INTEGER PRIMARY KEY,
    class_name TEXT,
    period INTEGER,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(id)
)

INSERT INTO students(name,email,grade_level)
VALUES ("Justin", "j@gmail.com", 12);

INSERT INTO teacher(name,email,specialty)
VALUES ("Stephen", "s@gmail.com", "JS");

INSERT INTO schedules(class_name,period,student_id,teacher_id)
VALUES("Python 101", 1, 3, 1);
INSERT INTO schedules(class_name,period,student_id,teacher_id)
VALUES("JS 101", 2, 2, 2);

SELECT students.name, schedules.period, schedules.class_name, teacher.name
FROM schedules
JOIN students,teacher
ON students.id = schedules.student_id and teacher.id = schedules.teacher_id
WHERE students.id = 2;

