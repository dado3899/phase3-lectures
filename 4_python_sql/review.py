# Join tables in Python
class Movies:
    def __init__(self,title):
        self.title = title
        pass
class Actors:
    def __init__(self,name):
        self.name = name
        pass
#credits.py
class Credits:
    def __init__(self,movie,actor):
        if type(movie) is Movies and type(actor) is Actors:
            self.movie = movie
            self.actor = actor
    def delself(self):
        print("Deleting")
        del self.actor
# from credits import Credits
avatar = Movies("Avatar")
cocainebear = Movies("Cocaine Bear")
spacebear = Actors("Space Bear")
bear1 = Credits(avatar,spacebear)
bear2 = Credits(cocainebear,spacebear)

bear1.delself()
# print(bear1.actor.name)
print(bear2.actor.name)
# Delete self, no can do within class

# SQL Basics


# Run sql file