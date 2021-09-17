class CricketTeam:
   def __init__(self, name, ranking, continent):
     self.name = name
     self.ranking = ranking
     self.continent = continent

   def add_player(self, *info):
     pass

   def __str__(self):
     s = f"Name: {self.name}\nRanking: {self.ranking}\nContinent: {self.continent}"
     return s

# Write your codes here.
class BDTeam(CricketTeam):
    def __init__(self, name, rank, cont, cup):
        super().__init__(name, rank, cont)
        self.cup = cup
        
    def asia_cup_status(self):
        return f"Hurray!!! Bangladesh has won {self.cup} Asia Cups!!!"
    def add_player(self, *args):
        self.bat = []
        self.ball = []
        self.all = []
        for i in range(len(args)):
            if i%2 != 0:
                if args[i] == "Batter":
                    self.bat.append(args[i-1])
                elif args[i] == "Bowler":
                    self.ball.append(args[i-1])
                else:
                    self.all.append(args[i-1])
            else:
                pass
                
    
    def __str__(self):
        s = f"Name: {self.name}\nRanking: {self.ranking}\nContinent: {self.continent}"
        m = f"\nPlayers: \nBowler: {self.ball} \nAll Rounder: {self.all} \nBatter: {self.bat}"
        return f"Country Details: \n{s} \nAsia Cup Win: {self.cup} {m}"
    
class AusTeam(CricketTeam):
    def __init__(self, name, rank, cont, cup):
        super().__init__(name, rank, cont)
        self.cup = cup
        
    def world_cup_status(self):
        return f"Hurray!!! Australia has won {self.cup} World Cups!!!"
    
    def add_player(self, *args):
        self.bat = []
        self.ball = []
        self.all = []
        for i in range(len(args)):
            if i%2 == 0:
                if args[i] == "Batter":
                    self.bat.append(args[i+1])
                elif args[i] == "Bowler":
                    self.ball.append(args[i+1])
                else:
                    self.all.append(args[i+1])
            else:
                pass
                
    
    def __str__(self):
        s = f"Name: {self.name}\nRanking: {self.ranking}\nContinent: {self.continent}"
        m = f"\nPlayers: \nBatter: {self.bat} \nAll Rounder: {self.all} \nBowler: {self.ball}"
        return f"Country Details: \n{s} \nWorld Cup Win: {self.cup} {m}"
   





# Do not change the following lines of code.

bangladesh = BDTeam("Bangladesh", 7, "South Asia", 1)
bangladesh.add_player("Mustafiz", "Bowler", "Mashrafee", "Bowler", "Shakib", "All Rounder", "Tamim", "Batter", "Mahmudullah", "Batter")
print('1.------------------------------------')
print(bangladesh.asia_cup_status())
print('2.------------------------------------')
print(bangladesh)
print('3.====================================')
australia = AusTeam("Australia", 3, "Oceania", 5)
australia.add_player("Batter", "Smith", "All Rounder", "Marsh", "Batter", "David", "Bowler", "Starc", "Bowler", "Hazlewood")
print('4.------------------------------------')
print(australia.world_cup_status())
print('5.------------------------------------')
print(australia)