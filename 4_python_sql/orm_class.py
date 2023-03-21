# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("pokemon.db")
cursor = connection.cursor()

class Pokemon:
    all = []
    def __init__(self,name,type,size,owned, id =-1):
        self.id = id
        self.name = name
        self.type = type
        self.size = size
        #Boolean
        self.owned = owned
        # self.pushtobackend()
        Pokemon.all.append(self)
    def pushtobackend(self):
        value = f'''
        INSERT INTO pokemon (name,type,size,owned)
        VALUES ("{self.name}","{self.type}",{self.size},{self.owned});
        '''
        cursor.execute(value)
        connection.commit()
        input = self.fetchall()
        self.id = input[-1][0]
    def edit(self,var,newinput):
        if type(newinput) is str:
            value = f'''
            UPDATE pokemon
            SET {var} = "{newinput}"
            WHERE id = {self.id}
            '''
        else:
            value = f'''
            UPDATE pokemon
            SET {var} = {newinput}
            WHERE id = {self.id}
            '''
        cursor.execute(value)
        connection.commit()
        self.owned = newinput
    @classmethod
    def fetchone(cls,id):
        value = f'''
        SELECT * FROM pokemon
        WHERE id = {id}
        '''
        x = cursor.execute(value).fetchone()
        return x
    @classmethod
    def fetchall(cls):
        value = f'''
        SELECT * FROM pokemon
        '''
        x = cursor.execute(value).fetchall()
        return x


pokemonlist = Pokemon.fetchall()
for pokemon in pokemonlist:
    Pokemon(pokemon[1],pokemon[2],pokemon[3],bool(pokemon[4]),pokemon[0])
print(Pokemon.all[0].owned)
# pidgey = Pokemon("Pidgey","Flying",1,False)
# pidgey.pushtobackend()
# pidgey.edit("type","Fire")
# pidgey.edit("owned",True)