
def main():
    game1 = game(20)
    print(game1.moneyNodeAmount(1,0,0))
    

class game:
    def __init__(self, boardSize):
        self.boardSize = boardSize

    def moneyNodeAmount(self,passThroughs,extraMoves,bonus):
        tempPercent = 0
        extraMoveBonus = extraMoves*10
        endBonus = extraMoveBonus+bonus #could make a switch case statment to deal with bonuses if its gonna be a string card name
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
        return (100*tempPercent)+endBonus

        
main()
