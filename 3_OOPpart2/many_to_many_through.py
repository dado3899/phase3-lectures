class Landscaper:
    def __init__(self,name,company,location):
        self.name = name
        self.company = company
        self.location = location
        self.projects = []
    
    def create_project(self,client,price,materials):
        new_proj = Project(client=client, price=price, materials=materials, landscaper=self)
        self.projects.append(new_proj)
        return new_proj

class Client:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.projects = []
    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and len(value) > 5:
            self._name = value
        else:
            raise ValueError("Not a name")
    name = property(get_name,set_name)



class Project:
    def __init__(self, client, landscaper, price, materials):
        self.client = client
        self.landscaper = landscaper
        self.price = price
        self.material = materials

    def get_client(self):
        return self._client
    def set_client(self,value):
        if type(value) is Client:
            self._client = value
        else:
            raise ValueError("Not a Client")
    client = property(get_client,set_client)