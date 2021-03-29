# Bugs:
# - Problème indice question 50/50
# - Problème dans getNextScore
# - joker global

#import matplotlib.pyplot as plt
import random
import csv
import sys,time,os

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
    typewriter("Bienvenue à Qui veut Gagner des millions ! \n\
    \n\
    Ce jeu a été développé par Mathieu Chikli, Alexis Joudiou, Antoine Mabille, Quentin-Amaury Hammerer, Théo Tacita et Enzo Zanzarelli \n\
    dans le cadre du cours 'Digital insight: algorithmics and programming' de l'ESCP Business School ! \n\
    \n\
    Amusez-vous bien !")

    print("")
    print("")
    print("")

    start=input("Écrivez 'Commencer' pour lancer la partie ou 'Rules' pour connaître les règles du jeu!")

    while start != "Commencer" and start != "Rules":
        start=input("Écrivez 'Commencer' pour lancer la partie ou 'Rules' pour connaître les règles du jeu!")
    else:
        if start == "Commencer":
            print("")
            typewriter("Que la partie commence ! ")
        else:
            print("")
            print("Tableau des scores : ")
            print("")
            print("    15)            1.000.000€")
            print("    14)            300.000€")
            print("    13)            150.000€")
            print("    12)            100.000€")
            print("    11)            72.000€")
            print(" PALIER:     48.000€")
            print("     9)            24.000€")
            print("     8)            12.000€")
            print("     7)            6.000€")
            print("     6)            3.000€")
            print(" PALIER:     1.500€")
            print("     4)            800€")
            print("     3)            500€")
            print("     2)            300€")
            print("     1)            200€")
            print("")
            print("Règles du jeu : ")
            print("")
            print("Le but du jeu est de répondre à une suite de 15 questions de 'culture générale pour tenter de remporter le gain maximal de 1 000 000 €.")
            print("Si, à un moment ou à un autre, un joueur répond incorrectement, il retombe sur le dernier 'palier' - soit 1 000€, soit 24 000€ - et son jeu est terminé.")
            print("")
            print("Par exemple, un candidat qui échoue à la question 13 gagnera 24 000€ . Si il répond incorrectement avant d'atteindre le premier palier (1 000€), il perd tout. ")
            print("")
            print("--> 3 jokers sont à votre disposition : le 50/50 qui permet d'éliminer 2 mauvaises réponses, l'appel à un ami et le vote du public. Chaque joker n'est utilisable qu'une seule fois")
            print("")
            print("Si il y a plusieurs joueurs, le candidat qui gagne le plus grand montant remporte la partie")
            print("")
            start_after_rules=input("Écrivez 'Commencer' pour lancer la partie !")
            while start_after_rules != "Commencer":
                start=input("Écrivez 'Commencer' pour lancer la partie !")
            else:
                    print("")
                    typewriter("Que la partie commence ! ")

def QuestionUI(number_player,player_name,validated_amount,current_amount,joker_available,number_question, question, answer_A, answer_B, answer_C, answer_D):
    printSpacer(20)
    interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
    interface_question(number_question,question, answer_A, answer_B, answer_C, answer_D)

def JokerUI(jokertype,number_player,player_name,validated_amount,current_amount,joker_available,number_question,question, answer_A, answer_B, answer_C, answer_D, answer_AA, answerIndex_AA, answer_BB, answerIndex_BB,good_answer):
    if jokertype == "50/50":
        interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
        print("")
        print("                                     Vous avez utilisé le joker '50/50' : voici le résultat : ")
        print("")
        interface_question_after_50_50(number_question,question,answer_AA,answerIndex_AA,answer_BB,answerIndex_BB)
    if jokertype == "Ami":
        page_question_after_ami(number_player,player_name,validated_amount,current_amount,joker_available,number_question,question,answer_A,answer_B,answer_C,answer_D,good_answer)
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
    print("                                       ",chr(97 + answerIndex_AA),".",answer_AA, "       ",chr(97 + answerIndex_BB),".", answer_BB)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Écrivez 'A','B','C','D' pour choisir votre réponse ")
    print("ou écrivez 'Joker' pour utiliser un de vos Jokers ")

import sys,time,os

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.02)
        else:
            time.sleep(0.2)

def ask_choice_friends():
    print("Vous avez choisi de faire un Appel a un ami : voici les amis que vous pouvez appeler :")
    print("")
    print("Choix n°1 :    Enzo: 46 ans, en couple, 4 enfants, Responsable communication Darty")
    print("")
    print("Choix n°2 : Antoine : 20 ans, célibataire, 0 enfant, chômage et alcoolique")
    print("")
    print("Choix n°3 : Théa : 31 ans, célibataire, 2 enfants en bas âge, coiffeuse")
    print("")
    choice=int(input("Qui voulez-vous choisir ? (1/2/3)"))
    return choice
    

def interface_call_friend_(choice,player_name,question,answer_A, answer_B, answer_C, answer_D, good_answer):
    if choice == 1:
            typewriter(" \n\
                "+player_name+" : Allo Enzo ? Tu m'entends? \n\
                Enzo : Allo ? \n\
                "+player_name+" : Oui, bonjour Enzo, c'est "+player_name+" au téléphone, je suis en direct de Qui veut gagner des millions. J'aurais besoin de ton aide pour une question, tu es partant ? \n\
                Enzo : Salut "+player_name+" , oui pas de soucis je t'écoute ! \n\
                "+player_name+" : Ok alors la question est : "+question+ " et les réponses sont : A) "+answer_A+" B) "+answer_B+" C) "+answer_C+" D) "+answer_D+" ... tu en penses quoi ? \n\
                Enzo : Alors je dirais que la bonne réponse est "+good_answer+" ! \n\
                "+player_name+" : Super merci beaucoup, je te revaudrais ça ! À bientôt ! \n\
                Enzo : Pas de soucis, bon courage pour la suite !")
            print("")
            print("")
            print("")
    if choice == 2:
        typewriter(" \n\
            "+player_name+" : Allo Antoine ? Tu m'entends? \n\
            Antoine : Oh allo \n\
            "+player_name+" : ça fait plaisir de t'entendre ça faisait longtemps \n\
            Antoine : Haha merci moi aussi. \n\
            "+player_name+" : Je participe à l'émission 'Qui veut gagner des millions' je sais pas si tu connais. Est-ce que tu pourrais m'aider pour une question frérot c'est dans ton domaine ? \n\
            Antoine : Pas de soucis mon reuf, dis moi tout ! \n\
            "+player_name+" : Vas y alors la question c'est : "+question+" et les propositions de réponses sont : A) "+answer_A+" B) "+answer_B+" C) "+answer_C+" D)"+answer_D+" ... tu mettrais quoi ? \n\
            Antoine : Euh attends laisse moi réfléchir... Tente "+good_answer+" je croise les doigts pour toi. \n\
            "+player_name+" : Ok parfait on va tenter ça, tu vas peut-être me sauver la vie là! \n\
            Antoine : Haha avec plaisir hâte de te revoir !")                    
        print("")
        print("")
        print("")

    if choice == 3:
        typewriter(" \n\
            "+player_name+" : Allo Théa    ? \n\
            Théa : Allo ? \n\
            "+player_name+" : Oui, c'est "+player_name+" Tu peux m'aider pour une question ma belle ? \n\
            Théa : Oh bébé c'est trop bien t'es trop fort! Dis-moi tout ! \n\
            "+player_name+" : Ok alors la question est : "+question+ " et les réponses sont : A) "+answer_A+" B) "+answer_B+" C) "+answer_C+" D) "+answer_D+" ... tu mettrais quoi à ma place ? \n\
            Théa : Euh... C'est dur! Alors attends par élimination je dirais "+good_answer+" ! \n\
            "+player_name+" : Oh chérie merci beaucoup, je te revaudrais ça ! On se voit demain ! \n\
            Théa : Continue comme ça donne tout !")                 
        print("")
        print("")
        print("")

def page_question_after_ami(number_player,player_name,validated_amount,current_amount,joker_available,number_question,question, answer_A, answer_B, answer_C, answer_D,good_answer):
        interface_stats(number_player,player_name,validated_amount,current_amount,joker_available)
        choice=ask_choice_friends()
        print("")
        print("                                                                         Vous avez utilisé le joker 'Appel a un ami' , Voici le résultat :    ")
        print("")
        print("")
        interface_call_friend_(choice,player_name,question,answer_A, answer_B, answer_C, answer_D, good_answer)
        interface_question(number_question,question, answer_A, answer_B, answer_C, answer_D)

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
        if pn in range(1,maxPlayerNumber + 1):
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

#WelcomeUI()

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
                JokerUI(joker,currentPlayers.index(currentPlayer) + 1,currentPlayer.getName(),currentPlayer.getScore(),currentScore,currentPlayer.getJokersLeft(),questionnumber,currentQuestion.getQuestion(),currentQuestion.getPossibilities()[0],currentQuestion.getPossibilities()[1],currentQuestion.getPossibilities()[2],currentQuestion.getPossibilities()[3],currentQuestion.getPossibilities()[psub[0]],psub[0],currentQuestion.getPossibilities()[psub[1]],psub[1],currentQuestion.getAnswer())
                answer = input("# ")
            if currentQuestion.getPossibilities()[ord(answer.lower()) - 97] is currentQuestion.getAnswer():
                currentPlayer.setScore(currentScore)
                SuccessUI(playernumber,currentPlayer.getName(),currentPlayer.getScore(),currentScore,currentPlayer.getJokersLeft(),questionnumber,currentQuestion.getQuestion(),currentQuestion.getPossibilities()[0],currentQuestion.getPossibilities()[1],currentQuestion.getPossibilities()[2],currentQuestion.getPossibilities()[3])
            else:
                FailUI(currentPlayers.index(currentPlayer) + 1,currentPlayer.getName(),currentPlayer.getScore())
                currentPlayer.eliminate()
                if currentPlayers is []:
                    LostUI()
