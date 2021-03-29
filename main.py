# Bugs:
# - Problème indice question 50/50
#

#import matplotlib.pyplot as plt
import random
import csv

#________ Question class

class Question:

    def __init__(self,question,answer,possibilities,difficulty):
        self.question = question
        self.answer = answer
        self.possibilities = random.sample(possibilities,len(possibilities))
        self.difficulty = int(difficulty)

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getPossibilities(self):
        return self.possibilities

    def getDifficulty(self):
        return self.difficulty

    def retrieveAnswerIndex(self):
        for i in range(0,3):
            if self.answer is self.possibilities[i]:
                return i

#________ Player class

class Player:

    def __init__(self,name):
        self.name = name
        self.score = 0
        self.jokers = jokers
        self.playing = True

    def getName(self):
        return self.name

    def setScore(self, amount):
        self.score = amount

    def getScore(self):
        return self.score

    def getJokersLeft(self):
        return self.jokers

    def isJokerLeft(self,joker):
        return joker in self.jokers

    def useJoker(self,joker):
        self.jokers.remove(joker)

    def isPlaying(self):
        return self.playing

    def eliminate(self):
        if self.playing is True:
            self.playing = False
            currentPlayers.remove(self)
            return True
        else:
            return False

#________ Joker intermediate functions

# 50/50
def getTwoPossibilities(answerIndex):
    sample = [0,1,2,3]
    sample.pop(sample.index(answerIndex))
    p = [answerIndex, random.choice(sample)]
    return random.sample(p,len(p))

# TO DO
#def friendSuggestion():

# Help from the public
def getGraphValues(answerIndex):
    graphValues = [random.randint(30,100)]
    remainder = 100 - graphValues[0]
    for i in range(0,3):
        gV = random.randint(0,remainder)
        graphValues.append(gV)
        remainder -= gV
    orderedGraphValues = [0,0,0,0]
    orderedGraphValues[answerIndex] = graphValues[0]
    graphValues.pop(0)
    i = 0
    for oGV in orderedGraphValues:
        if oGV == 0:
            orderedGraphValues[i] = graphValues[i]
            i += 1
    return orderedGraphValues

#________ Phase class

class Phase:

    def __init__(self,levels,difficulty):
        self.number = len(levels) + 1
        self.levels = levels
        self.difficulty = difficulty
        self.possibleQuestions = []

        for question in questions:
            if question.getDifficulty() == self.difficulty:
                self.possibleQuestions.append(question)

    def getNextQuestion(self):
        nextQuestion = self.possibleQuestions[random.randint(0,len(self.possibleQuestions) - 1)]
        self.possibleQuestions.pop(self.possibleQuestions.index(nextQuestion))
        return nextQuestion

    def getNextScore(self):
        self.number -= 1
        return int(self.levels[len(self.levels) - self.number])

    def isFinished(self):
        return self.number <= 0

    def getMessage(self):
        return self.message

#________ Interfaces

def WelcomeUI():
    print("")

def QuestionUI(number_player,player_name,validated_amount,current_amount,joker_available,number_question, question, answer_A, answer_B, answer_C, answer_D):
    printSpacer(20)
    interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
    interface_question(number_question,question, answer_A, answer_B, answer_C, answer_D)

def JokerUI(jokertype,number_player,player_name,validated_amount,current_amount,joker_available,number_question,question, answer_A, answer_B, answer_C, answer_D, answer_AA, answerIndex_AA, answer_BB, answerIndex_BB):
    if jokertype == "50/50":
        interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
        print("")
        print("                                     Vous avez utilisé le joker '50/50' : voici le résultat : ")
        print("")
        interface_question_after_50_50(number_question,question,answer_AA, answerIndex_AA, answer_BB, answerIndex_BB)
#    if jokertype == "Ami":
#    if jokertype == "Public":


def SuccessUI(number_player, player_name, validated_amount, current_amount, joker_available, number_question, question, answer_A, answer_B, answer_C, answer_D):
    printSpacer(20)
    interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
    interface_good_answer(player_name,validated_amount,current_amount)

def FailUI(number_player, player_name, validated_amount):
    printSpacer(20)
    print("Joueur n°",number_player, " : ",player_name)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("            Oh non ", player_name, "ce n'était pas la bonne réponse ... Malheureusement l'aventure se termine ici pour vous !" )
    print("                                Vous repartez avec ", validated_amount,"€ , Félicitation !" )
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Écrivez 'Relancer' pour relancer une partie")

def WonUI():
    printSpacer(20)
    print("")

def LostUI():
    printSpacer(20)
    print("")

def interface_stats(number_player,player_name,validated_amount,current_amount,joker_available):
    print("Joueur n°",number_player, ": ", player_name)
    print("Jokers restants : ", joker_available)
    print("Montant minimal gagné : ", validated_amount)
    print("Palier en cours : ", current_amount )
    print("")
    print("")
    print("")
    print("")

def interface_question(number_question, question, answer_A, answer_B, answer_C, answer_D):
    print("                                  Question n°",number_question,": ", question," ? ")
    print("")
    print("                                       a.",answer_A, "       b.", answer_B)
    print("                                       c.",answer_C, "       d.", answer_D)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Écrivez 'A','B','C','D' pour choisir votre réponse ")
    print("ou écrivez 'Joker' pour utiliser un de vos Jokers ")

def interface_good_answer(player_name,validated_amount,current_amount):
    print("                          Bravo", player_name, " vous avez répondu juste ! Vous venez de gagner", validated_amount, "€ !" )
    print("                        Vous pouvez tenter de gagner ", current_amount, "€ en répondant à la prochaine question" )
    print("")
    print("                        Attention si vous répondez faux vous ne repartirez qu'avec ", validated_amount, "€ ..." )
    print("                                                       Alors, on continue ? " )
    print("")
    print("")
    print("")
    print("")
    print("Écrivez 'Continuer' pour continuer ou 'Stop' pour partir avec le montant minimal gagné")

def interface_question_after_50_50(number_question, question, answer_AA, answerIndex_AA, answer_BB, answerIndex_BB):
    print("                                  Question n°",number_question,": ", question," ? ")
    print("")
    print("                                       ",chr(96 + answerIndex_AA),".",answer_AA, "       ",chr(96 + answerIndex_BB),".", answer_BB)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Écrivez 'A','B','C','D' pour choisir votre réponse ")
    print("ou écrivez 'Joker' pour utiliser un de vos Jokers ")

#________ Utils

def loadFromCSV(url):
    questions = []
    with open(url, encoding='utf-8') as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
        data.pop(0)
        for row in data:
            cells = row[0].split(";")
            question = Question(cells[0],cells[1],[cells[1],cells[2],cells[3],cells[4]],cells[5])
            questions.append(question)
    return questions

def printSpacer(lines):
    for i in range(1,lines):
        print("")

#________ Checks

def checkPlayerNumber(playernumber):
    try:
        pn = int(playernumber)
        if pn in range(1,maxPlayerNumber):
            return True
        else:
            return False
    except ValueError:
        return False

#________ Game parameters

    # Questions CSV File URL

questionsURL = "C:/Users/Mathi/iCloudDrive/Documents/Algorithmics and programming/Question pour un champion/data.csv"
questions = loadFromCSV(questionsURL)

    # General parameters

game = []
phasesNumber = 1
maxPlayerNumber = 2
jokers = ["50/50","Ami","Public"]
welcomeMessage = "Ceci est le message de bienvenue"

    # Phase 1

phase1 = Phase(["200","300","500","800","1500"],1)
game.append(phase1)

    # Phase 2

phase2 = Phase(["3000","6000","12000","24000","48000"],2)
game.append(phase2)

    # Phase 3

phase3 = Phase(["72000","100000","150000","300000","1000000"],3)
game.append(phase3)

#________ Main program

players = []
currentPlayers = []
playernumber = input("Combien de personnes jouent ? ")
printSpacer(1)
while checkPlayerNumber(playernumber) == False:
    playernumber = input("Erreur, veuillez entrer un nombre entre (1-4): ")
for i in range(1,int(playernumber) + 1):
    name = input("Quel est le nom du joueur n°" + str(i) + " ? ")
    player = Player(name)
    players.append(player)
    print("Bonjour " + name + "!")
    printSpacer(1)
currentPlayers = players

questionnumber = 0
for phase in game:
    while phase.isFinished() is False:
        currentScore = phase.getNextScore()
        questionnumber += 1

        for currentPlayer in currentPlayers:
            currentQuestion = phase.getNextQuestion()

            QuestionUI(currentPlayers.index(currentPlayer) + 1,currentPlayer.getName(),currentPlayer.getScore(),currentScore,currentPlayer.getJokersLeft(),questionnumber,currentQuestion.getQuestion(),currentQuestion.getPossibilities()[0],currentQuestion.getPossibilities()[1],currentQuestion.getPossibilities()[2],currentQuestion.getPossibilities()[3])
            answer = input("# ")
            if answer.lower() == "joker":
                joker = input("Quel Joker voulez vous utiliser parmi " + str(currentPlayer.getJokersLeft()) + ": ")
                while joker not in currentPlayer.getJokersLeft():
                    joker = input("Erreur, veuillez choisir un Joker parmi " + str(currentPlayer.getJokersLeft()) + ": ")
                currentPlayer.useJoker(joker)
                psub = getTwoPossibilities(currentQuestion.retrieveAnswerIndex())
                JokerUI(joker,currentPlayers.index(currentPlayer) + 1,currentPlayer.getName(),currentPlayer.getScore(),currentScore,currentPlayer.getJokersLeft(),questionnumber,currentQuestion.getQuestion(),currentQuestion.getPossibilities()[0],currentQuestion.getPossibilities()[1],currentQuestion.getPossibilities()[2],currentQuestion.getPossibilities()[3],currentQuestion.getPossibilities()[psub[0]],psub[0],currentQuestion.getPossibilities()[psub[1]],psub[1])
                answer = input("# ")
            if currentQuestion.getPossibilities()[ord(answer.lower()) - 97] is currentQuestion.getAnswer():
                currentPlayer.setScore(currentScore)
                SuccessUI(playernumber,currentPlayer.getName(),currentPlayer.getScore(),currentScore,currentPlayer.getJokersLeft(),questionnumber,currentQuestion.getQuestion(),currentQuestion.getPossibilities()[0],currentQuestion.getPossibilities()[1],currentQuestion.getPossibilities()[2],currentQuestion.getPossibilities()[3])
            else:
                FailUI(currentPlayers.index(currentPlayer) + 1,currentPlayer.getName(),currentPlayer.getScore())
                currentPlayer.eliminate()
                if currentPlayers is []:
                    LostUI()
