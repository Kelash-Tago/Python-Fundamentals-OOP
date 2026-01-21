#class attribute and instance attribute
class Player:
    player_count=0

    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player._increment()
    def __str__(self):
        return (f"Name: {self.name} level: {self.level} ")
    @classmethod
    def _increment(cls):
        cls.player_count+=1
    

players=[
    Player("Kelash","Good"),
    Player("Aneel","Best"),
    Player("Sanjay","Well")
]

for player in players:
    print(player)

print("Total number of players: ",Player.player_count)

print(Player("Vijesh","Good").player_count) #now 4