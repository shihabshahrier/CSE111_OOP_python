class Player:
    player = 0
    forword = 0
    defender = 0
    def __init__(self, name, team, pos = "Forward"):
        self.name = name
        self.team = team
        self.pos = pos
        Player.player += 1
        if self.pos == "Forward":
            Player.forword += 1
            print("Creating a Forward.")
        else:
            Player.defender += 1
            print("Creating a Defender.")

    def calculate_earning(self, a, b = 0):
        if self.pos == "Forward":
            self.earning = (a * 400)+ (b * 50)
        else:
            self.earning = (a * 400) + (b * 40)
        
        
    def player_info():
        print(f"Total Number of Player: {Player.player}")
        print(f"Total Number of Forward: {Player.forword}")
        print(f"Total Number of Defender: {Player.defender}")
    
    def __str__(self):
        s = f"Player No: {Player.player} \nName: {self.name} \nTeam: {self.team}"
        m = f"\nPosition: {self.pos} \nPlayer No: {self.earning.__str__()}$"
        return f" {s} {m}"



#Write your code here
Player.player_info()
print('1.========================================')
ronaldo = Player("Ronaldo", "Man United")
print('2.----------------------------------------')
ronaldo.calculate_earning(5, 7)
print('3.----------------------------------------')
print(ronaldo)
print('4.========================================')
ramos = Player("Ramos", "PSG", "Defender")
print('5.----------------------------------------')
ramos.calculate_earning(5, 1)
print('6.----------------------------------------')
print(ramos)
print('7.========================================')
pogba = Player("Pogba", "Man United")
print('8.----------------------------------------')
pogba.calculate_earning(5)
print('9.----------------------------------------')
print(pogba)
print('10.========================================')
Player.player_info()