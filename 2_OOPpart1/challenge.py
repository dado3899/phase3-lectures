# Make a class for a user with:
# A username
# A password
# An Email
class User:
    all_users = []
    def __init__(self, username,password,email):
        self.username = username
        self.password = password
        self.email = email
        self.password_attempts = 0
        User.all_users.append(self)

    # def get_<variable>(self):
    #     return
    def get_email(self):
        return self._email
    def set_email(self,value):
        if type(value) is str and "@" in value:
            self._email = value
        else:
            raise ValueError("Not valid email")
    email = property(get_email,set_email)

    def get_username(self):
        return self._username
    def set_username(self,value):
        for user in User.all_users:
            if user.username == value:
                raise ValueError("USERNAME ALREADY IN USE")
        self._username = value
    username = property(get_username,set_username)

    def password_check(self,inputted_password):
        if self.password_attempts < 4:
            if self.password == inputted_password:
                print("Logging in")
            else:
                self.password_attempts +=1
                print("Not valid password")
        else:
            print("NOT TODAY HACKER")


sam = User("samoontha","123","sam@gmail.com")
kaleab = User("kdriz","123","sam@gmail.com")
david = User("kdrizzzzzz","123","sam@gmail.com")

sam.password_check("123")
# sam.password_check("2")
# sam.password_check("3")
# sam.password_check("4")
# sam.password_check("5")
# Add a property to the email to validate it has an @ in it

# Add a method that takes a password and validates it

# Bonus: Add a property to the username to check to see if it is
# already used