class Sponser:
    all = []
    def __init__(self,name, product):
        self.name = name
        self.product = product
        Sponser.all.append(self)
    def getcontracts(self):
        for contract in Contract.all:
            if contract.sponser is self:
                print(f'Player: {contract.player.name} Payout:{contract.money}')

class Player:
    all = []
    def __init__(self,name,team):
        self.name = name
        self.team = team
        Player.all.append(self)

class Contract:
    all = []
    def __init__(self,money,length,sponser):
        self.money = money
        self.length = length
        self.sponser = sponser
        self.player = None
        Contract.all.append(self)
    def signcontract(self,player):
        self.player = player
    def delete(self):
        del self

nike = Sponser("Nike","Shoes")
matt = Player("Matt","Flatirons")
jonah = Player("Jonah","Asstro")
nikecontract = Contract(1,"2 Years",nike)
nikecontract.signcontract(matt)
badcontract = Contract(-100000,"6 Months",nike)
badcontract.signcontract(jonah)
nike.getcontracts()
badcontract.delete()

# adidas = Sponser()
# How do we connect the two?