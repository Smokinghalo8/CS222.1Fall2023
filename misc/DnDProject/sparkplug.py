import os

def main():
    tempDir=os.getcwd()
    DirectorySaveFileList = os.listdir(tempDir+"/misc/DnDProject/savedChars")
    player = playerSetup()
    player.createIMPORTANTarrays()
    #player.seeIfTheyAlreadyHaveASave() #This should see if the player is gonna use a save
    playersAnswers = player.askQuestionsForPrompt()
    player.putInfoIntoDocument(playersAnswers)  #playersAnswers are transcribed as:
    #[name(string),abilityScores(array), skillProficencys(array), class(playerClass)]
    #[name(string),abilityScores(array),smallerSkills(array)]


main()


class playerClass:
    def __init__(self,classChosen):
        self.playerClass = classChosen

    def appendClassBonus(self):     #This should check the class you chose and will give you bonuses for each one including traits and extra thingies idk
        match self.playerClass():
            case "debug":
                print("my balls")
            case _:
                print("Error 2 - Error in playerClass - appendClassBonus")



class playerSetup:
    def __init__(self):
        pass

    def askQuestionsForPrompt(self):
        print("Is this character new or are you transcribing")
        tempFlagInt1 = 0
        questionAskIfNew = input()
        if tempFlagInt1 == 0:
            match questionAskIfNew:
                case "new":
                    tempFlagInt1 = 1
                case "transcribe":
                    tempFlagInt1 = 2
                case _:
                    print("You should really print out what you want")
                    self.askQuestionsForPrompt
        elif tempFlagInt1==1:   #This is for the response "new"
            pass
        elif tempFlagInt1==2:   #This is for the response "transcribe"
            pass
        else:
            print("Error 1 - Error in new/transcribe methods")

    def getInfoFromDocument(self):
        pass

    def getInfoFromPrompt(self):
        pass

    def putInfoIntoDocument(self, arrayOfInformation):
        pass

    def createIMPORTANTarrays(self):
        self.spellbook = []
        self.items = []
        self.effects = []
        self.perks = []

    def appendSpellIntoSpellbook(self,spell):
        #Should take the spell and compare it to a file with ALL the dnd Spells, to make sure it is spelled correctly, 
        #and if it is and exsists, it should add the spell to the players spellbook with the spell slot needed, damage roll, extra things it does
        #at higher spell slot levels, what type of damage - it should get all this information from another text file that has all of it,
        #the layout of the spells is detailed in spellEffects.txt and the spells are in spells.txt, both under assets
        pass