
#could make a game where this is an online tool soley used for creating a document full of information :?
from random import randint


def main():
    
    player1 = playerCreation("Player1Name")
    player2 = playerCreation("Player2Name")
    game1 = game(20, player1, player2)

    print(game1.moneyNodeAmount(player1,1,1,0)) #self,player,passThroughs,extraMoves,bonus - bonus; 0=nothing 1=ExtraRouter
    #game1.printShop(player1)
    #player1.printItems(player1)
    

class playerCreation:
    def __init__(self, playerName):
        self.money = 0
        self.name = playerName
        self.items = []

    def addMoney(self,amount):
        self.money+=amount

    def printItems(self,player):
        print(player.items)

    def buySomething(self, player, item):
        match item:
            case "Firewall Bypass"|1:
                if player.money >= 25:
                    player.money -= 25
                    player.items.append("Firewall Bypass")
                else:
                    print("Not enough Money!!!")
            case "Extra Router"|2:
                if player.money >= 50:
                    player.money-=50
                    player.items.append("Extra Router")
                else:
                    print("Not enough Money!!!")
            case "None"|0:
                print("Nothing bought...")
            case _:
                print("Error 2 - in buySomething function")




class game:
    def __init__(self, boardSize, player1, player2):
        self.boardSize = boardSize
        self.player1Name = player1.name
        self.player2Name = player2.name
        

    def moneyNodeAmount(self,player,passThroughs,extraMoves,bonus):
        tempPercent = 0
        tempBonus = 0
        tempBONUSPERCENT = (randint(0,10)/10)
        extraMoveBonus = extraMoves*10
        endBonus = extraMoveBonus #could make a switch case statment to deal with bonuses if its gonna be a string card name
        match passThroughs:
            case 1:
                tempPercent=1
            case 2:
                tempPercent=.50
            case 3:
                tempPercent=.25
            case _:
                tempPercent=0
                print("Error 0 - Can't pass through "+str(passThroughs)+" times")


        match bonus:
            case 1|"ExtraRouter":
                tempPercent+=.25
                tempBonus+=10
            case 0|"None":
                tempBonus+=0
            case _:
                tempBonus+0
                print("Error 1 - bonus error")
        endBonus+=tempBonus
        print("tempBonus-"+str(tempBonus)+"\ntempPercent-"+str(tempPercent)+"\nendMoney-"+str(100*tempPercent+endBonus)+"\nTempBONUSPERCENT-"+str(tempBONUSPERCENT))  #debug line
        tempPercent+=tempBONUSPERCENT
        player.addMoney((100*tempPercent)+endBonus)
        return (100*tempPercent)+endBonus   #prints money amount not need to keep note of
    

    def printShop(self, player):
        print("\n\n\n\n\n\n\n------------------SHOP------------------\n\nMoney:"+str(player.money)+"\nFirewall Bypass - Bypass 1 Firewall - 25\nExtra Router - Gives more money for the next money node attacked! - 50\n")
        print("Would you like to buy anything?\n")
        tempString = input()
        player.buySomething(player,tempString)   #testing the buying something

main()
