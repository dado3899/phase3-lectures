SELECT *
FROM joinclasses
JOIN classes,students
ON joinclasses.student_id = students.id AND joinclasses.class_id=classes.id;