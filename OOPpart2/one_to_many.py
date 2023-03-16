# Here we have one DungeonMaster that can have many players how can we do that?
class DungeonMaster:
    def __init__(self,name):
        self.name = name
        self.players = []
    def partylist(self):
        for player in self.players:
            print(f'{player.name}: {player.dndclass}')

class Player:
    def __init__(self,name,dndclass):
        self.name = name
        self.dndclass = dndclass
        self.dm = None


if __name__ == '__main__':
    # Create players
    jonah = Player("Jonah","Rogue")
    abby = Player("Abby","Thief")
    gage = DungeonMaster("Gage")
    # Attatch dm to each player
    jonah.dm = gage
    abby.dm = gage
    # attatch players to dm
    gage.players = [jonah,abby]
    # Create a new player and add it to dillon
    dillon = Player("Dillon","Princess Ruffian")
    gage.players.append(dillon)
    gage.partylist()
    # Don't forget to set dillons dm to gage!
    dillon.dm = gage
    

