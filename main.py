# - Fonction getNextPlayer() dans Phase
# - Modifier l'ordre des questions Excel
# - Créer une fin de jeu
# - Créer un tableau des scores à chaque Phase
# - Fonction checkPlayerNumber() dans Checks
# - Fonction getPlayerRank() dans Phase
# - Ajouter le paramètre reward à la classe Question
# -
# -

import random
import csv
import inflect

#________ Question class

class Question:

    def __init__(self,q,a,p):
        self.question = q
        self.answer = a
        self.possibilities = p
        self.reward = 0

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getPossibilities(self):
        return self.possibilities

    def getReward(self):
        return self.reward

#________ Player class

class Player:

    def __init__(self,n):
        self.name = n
        self.score = 0
        self.playing = True

    def getName(self):
        return self.name

    def increaseScore(self, n):
        self.score += n

    def getScore(self):
        return self.score

    def isPlaying(self):
        return self.playing

    def eliminate(self):
        if self.playing = True:
            self.playing = False
            currentplayers.remove(self)
            return True
        else:
            return False

#________ Phase class

class Phase:

    def __init__(self,n,m):
        self.number = n
        self.possibleQuestions = []
        self.questionHistory = []
        self.playerHistory = []
        self.message = m

    def getNextQuestion(self):
        nextNumber = random.randint(0,len(questions) - 1)
        nextQuestion = questions[nextNumber]
        while nextNumber in self.questionHistory:
                nextQuestion = questions[nextNumber]
                nextNumber = random.randint(0,len(questions) - 1)
        self.number -= 1
        self.questionHistory.append(nextNumber)
        return nextQuestion

    def getNextPlayer(self):

    def getPlayerRank(self,p):

    def isFinished(self):
        return self.number <= 0

    def getMessage(self):
        return self.message

#________ Utils

def loadFromCSV(url):
    questions = []
    with open(url) as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
        data.pop(0)
        for row in data:
            cells = row[0].split(";")
            question = Question(cells[0],"a",[cells[1],cells[2],cells[3],cells[4]])
            questions.append(question)
    return questions

def printSpacer(x):
    for i in range(1,x):
        print("")

#________ Checks

def checkPlayerNumber(playernumber):
    return True

#________ Dump

inflectEngine = inflect.engine()

#________ Game parameters

    # Questions CSV File URL

questionsURL = ""

    # General parameters

game = []
phasesNumber = 1
welcomeMessage = ""

    # Phase 1

phase1 = Phase(10,"Ceci est la 1ère phase")
game.append(phase1)

    # Phase 2

phase2 = Phase(10,"Ceci est la 2ème phase")
game.append(phase2)

    # Phase 3

phase3 = Phase(10,"Ceci est la 3ème phase")
game.append(phase3)

#________ Main program

questions = loadFromCSV(questionsURL)

print(welcomeMessage)
printSpacer(3)

players = []
playernumber = input("How many people are playing ? ")
printSpacer(1)
if checkPlayerNumber():
    for i in range(1,playernumber + 1):
        name = input("What is Player " + i + "'s name ? ")
        player = Player(name)
        players.append(player)
        print("Hello " + name + "!")
        printSpacer(1)
players = currentplayers

for phase in game:
    printSpacer(20)
    print(phase.getMessage())

    while phase.isFinished() is False:
        currentQuestion = phase.getNextQuestion()
        currentPlayer = phase.getNextPlayer()
        print("[" + currentPlayer.getName() + "] " + currentQuestion.getQuestion())

        i = 0
        for possibility in currentQuestion.getPossibilities():
            print(char(97 + i) " - " + possibility)
            i += 1

        if input("Your answer: ") is currentQuestion.getAnswer():
            currentPlayer.increaseScore(currentQuestion.getReward())
            print("Well played! Your score is now " + currentPlayer.getScore() + " (" + inflectEngine.ordinal(phase.getPlayerRank(currentPlayer)))
        else:
            print("Wrong, " + currentPlayer + " is eliminated :(")
            currentPlayer.eliminate()
