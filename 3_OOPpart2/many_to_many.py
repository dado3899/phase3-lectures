from faker import Faker
class Landscaper:
    def __init__(self,name,company,location):
        self.name = name
        self.company = company
        self.location = location
        self.clients = []

    def add_a_client(self,client):
        self.clients.append(client)
        client.landscapers.append(self)
    
    def print_client_names(self):
        for client in self.clients:
            print(f"{client.name} - {client.address}")

class Client:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.landscapers = []

faker = Faker()

print(faker.name())

landscapers = []
clients = [] 
for i in range(100):
    new_client = Client(
        name = faker.name(),
        address = faker.address()
    )
    clients.append(new_client)

for i in range(20):
    new_landscaper = Landscaper(
        name = faker.name(),
        company = faker.word() + " Inc",
        location = faker.address()
    )
    landscapers.append(new_landscaper)

import random

for landscaper in landscapers:
    print(landscaper.name)
    for i in range(10):
        landscaper.add_a_client(clients[random.randint(0,99)])

i1 = input("Please put what landscaper you are: ")

for landscaper in landscapers:
    if landscaper.name == i1:
        i2 = input("What would you like to do? 1) print clients, 2)add_new client")
        if i2 == "1":
            landscaper.print_client_names()
        if i2 == "2":
            print("Adding flowers")
# landscapers[0].print_client_names()
# print("__________________________________")
# landscapers[1].print_client_names()
# print("__________________________________")
# landscapers[5].print_client_names()

# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!