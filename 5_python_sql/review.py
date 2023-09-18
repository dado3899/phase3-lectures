# Join tables
class Student:
    def __init__(self, id):
        self.id = id
        

class JoinedClasses:
    def __init__(self, stu_id, class_id):
        self.stu_id = stu_id
        self.class_id = class_id
    

class Classes:
    def __init__(self,id):
        self.id = id
    def join_class(self):
        pass
        
# SQL Basics

# Run sql file using .read