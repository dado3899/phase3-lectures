# Parent - Child
# Category - Sub Category
class User:
    all_accounts = []
    all_users = []
    all_admin = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        pass
    
class Standard(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    def create_ticket(self):
        pass
    
class Admin(User):
    def __init__(self,username,password,level):
        super().__init__(username,password)
        self.level = level
    def ban_user(self):
        pass
# One to One
    # Review how to change relationships dynamically
class Key:
    def __init__(self,size,lock=None):
        self.size = size
        self.lock = lock
        if lock:
            lock.key = self
    
    def get_lock(self):
        return self._lock
    def set_lock(self,value):
        if type(value) is Lock:
            self._lock = value
        else:
            print("Not valid lock, no lock set")
            self._lock = None

    lock = property(get_lock,set_lock)
class Lock:
    def __init__(self,locktype,key=None):
        self.locktype = locktype
        self.key = key
        if key:
            key.lock = self

    def rekey(self,key):
        self.key = key
        key.lock = self

# k1 = Key(10)
# # print(k1.lock)
# l1 = Lock("Standard Pin",k1)

# k1.lock = "Help"

# print(k1.lock)

# One to Many
class Turntable:
    all_turntables = []
    def __init__(self,location):
        self.location = location
        self.records = []
        Turntable.all_turntables.append(self)
    
    def addRecords(self,records_to_add=[]):
        for record in records_to_add:
            self.records.append(record)
            record.turntable = self
    
    def printAllRecords(self):
        counter = 1
        for record in self.records:
            print(f"{counter}:{record.name}")
            counter+=1
class Record:
    def __init__(self,name,turntable=None):
        self.name = name
        self.turntable = turntable
    @classmethod
    def remove_all_records(cls,name_of_record):
        for turntable in Turntable.all_turntables:
            for record in turntable.records:
                if record.name == name_of_record:
                    record.turntable = None
                    turntable.records.remove(record)

t1 = Turntable("Flatirons")
t2 = Turntable("T2")
r1 = Record("Album 1")
r2 = Record("Fake Type")
r3 = Record("Fake Type")
t1.addRecords([r1,r2,r3])
# t1.addRecords([r1,r2,r1])
t2.addRecords([r1,r2])
t1.printAllRecords()
t2.printAllRecords()

Record.remove_all_records("Album 1")
print("||||||||||")
t1.printAllRecords()
t2.printAllRecords()
# Many to Many
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.teachers = []
    def join_class(self,teacher):
        self.teachers.append(teacher)
        teacher.students.append(self)
    
    def __repr__(self):
        return self.name
class Teacher:
    def __init__(self,name,specilty):
        self.name = name
        self.specilty = specilty
        self.students = []
    def __repr__(self):
        return self.name
david = Teacher("David","NOT Css")
sam = Teacher("Sam","Not css again")

jerrick = Student("Jerrick", 13)
mark = Student("Mark", 12)

jerrick.join_class(david)
jerrick.join_class(sam)
mark.join_class(sam)

print(mark.teachers)
print(jerrick.teachers)
print(sam.students)
print(david.students)
# isinstance() supports inheritence! Type does not
