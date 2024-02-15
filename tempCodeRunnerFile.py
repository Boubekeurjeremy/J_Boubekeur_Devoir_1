from random import random
import re
import time


class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"


# Fonction pour afficher du texte coloré (print, input)


def PrintColoredText(text, color, end="\n"):
    colored_text = f"{color}{text}{Color.RESET}"
    print(colored_text, end=end)


def InputColoredText(prompt, color):
    UserInput = input(f"{color}{prompt}{Color.RESET}")
    return UserInput


#####################################################################################################################

# Tuples
# Clarifiez ce que l'utilisateur doit faire en entrant des informations sur input.
StartMessage = f"Veuillez saisir un"

GameMessageInput = (
    (f"{StartMessage} entier strictement plus grand que 1 : "),
    (f"{StartMessage} nombre entre 0 et 100 : "),
    (f"{StartMessage} entier positif ou nul : "),
    (
        f"Veuillez, s'il vous plaît, appuyer sur la touche Entrée pour activer le jeu numéro 5 : "
    ),
)
##############
# Message erreur.
ErrorMessageNumber = (
    (
        f"Saisie incorrecte. Assurez-vous de saisir un entier strictement plus grand que 1."
    ),
    (f"Saisie incorrecte. Assurez-vous de saisir un nombre entre 0 et 100."),
    (f"Saisie incorrecte. Assurez-vous de saisir uniquement des chiffres."),
)
###############
# Info déroulement des jeux.
InfoMessage = (
    (f"😺😃  Bonjour, découvrez ces six jeux de calcul : 😃😺"),
    (f"Nombre entier entre 0 et n tiré au hasard :"),
    (f"Merci pour avoir participé, vous pouvez passer au jeu suivant."),
    (f"Division par deux :"),
    (f"Plus petit ou plus grand :"),
    (f"Tableau des puissances de 2 jusqu'à"),
    (f"Tableau des puissances de 2 :"),
    (f"Moyenne de tirage de nombre au hasard :"),
    (f"À très bientôt ! "),
)
#######################################################################################################################
# Fonction renvoyant chaque élément des tuples.
# Variables globales.


def GetMessage(message):
    return message


########
def InputMessage(use):
    use = GetMessage(GameMessageInput)
    return use


UseMsgOne, UseMsgTwo, UseMsgThree, UseMsgFour = InputMessage(GameMessageInput)


########
def RecoverMessage(versus):
    versus = GetMessage(ErrorMessageNumber)
    return versus


ErrMsgOne, ErrMsgTwo, ErrMsgThree = RecoverMessage(ErrorMessageNumber)


########
def InfoMessageUser(info):
    info = GetMessage(InfoMessage)
    return info


(
    InMsgOne,
    InMsgTwo,
    InMsgThree,
    InMsgFour,
    InMsgFive,
    InMsgSix,
    InMsgSeven,
    InMsgEight,
    InMsgNine,
) = InfoMessageUser(InfoMessage)

########
# Comptez le nombre de jeux.
GlobalCounter = 0
######################################################################################################################
# Fonction Message de pésentation des exercices.


def MessageIntroduction():
    print()
    j = 0
    while j < 19:
        if j + 1 == 19:
            PrintColoredText(f"{InMsgOne}", Color.CYAN)
        else:
            print(" ", end=" ")
        j += 1
    print("")


MessageIntroduction()
######################################################################################################################
# Fonction récupérant les valeurs des tests
# pour les fournir aux fonctions de calcul des exercices 1 et 2.


def EnterCorrectValue():
    while True:
        n = InputColoredText(f"{UseMsgOne}", Color.YELLOW)
        result = StrictValidCondition(n)

        if (result) is not None:
            return result


######################################################################################################################
# Fonction controle de saisie par l'utilisateur.


def KeyBoardControl(n):
    reGex = r"^\d+$"
    if re.match(reGex, n):
        KeyBoard = int(n)
        return KeyBoard
    else:
        return None


print()


####################################################################################################################
# Fonction condition stictement supérieure à 1 (n > 1) exercice 1, 2.
def StrictValidCondition(n):
    print()
    StrictValid = KeyBoardControl(n)
    if StrictValid is not None and StrictValid > 1:
        return StrictValid
    elif StrictValid is None:
        PrintColoredText(
            f"{ErrMsgThree}",
            Color.RED,
        )
    else:
        PrintColoredText(
            f"{ErrMsgOne}",
            Color.RED,
        )
    print()


#######################################################################################################################
# Fonction compteur pour le nombre de jeux.


def GameCounter():
    global GlobalCounter
    GlobalCounter += 1
    PrintColoredText(f"Jeu numéro {GlobalCounter} terminé.", Color.CYAN)


########
# Fonction affichant des émojis lors du changement d'exercice.
def Emojis():
    i = 0
    n = 11
    while i < 2:
        j = 0
        while j < 2 * n:
            if (i + j + 1 == n) or (-i + j + 1 == n):
                print("🐶", end=" ")
            else:
                print("😺", end=" ")
            j += 1
        print("")
        i += 1
    print()


########
# Fonction affichant les informations lors du changement d'exercice + compteur.
def FinishedGame():
    GameCounter()
    PrintColoredText(f"{InMsgThree}", Color.CYAN)
    print()
    Emojis()


########################################################################################################################
# Exercice 1
# Fonction affichant un nombre entier aléatoire entre 0 et n (itérations affichant 5 nombres entiers aléatoires).


def RandomNumber():
    PrintColoredText(f"{InMsgTwo}", Color.BLUE)
    print()
    RdUser = EnterCorrectValue()
    for i in range(1, 6):
        RdNumber = int(RdUser * random())
        PrintColoredText(
            f"({i}) : Nombre au hasard entre 0 et {RdUser} : {RdNumber}",
            Color.PURPLE,
        )
    print()
    FinishedGame()


RandomNumber()

########################################################################################################################
# Exercice 2
# Fonction calculant la moyenne de valeurs aléatoires entre 0 et n.


def AverageCalcul(n, NumIterations):
    total = 0
    for _ in range(NumIterations):
        total += int(n * random())
    average = total / NumIterations
    return average


##########
# Fonction itérations de calcul de moyenne, puis affichage.


def AverageIteration():
    PrintColoredText(f"{InMsgEight}", Color.BLUE)
    print()
    n = EnterCorrectValue()
    iterations = [25, 1000, 10000, 100000, 1000000, 10000000]
    for iteration in iterations:
        averageIt = AverageCalcul(n, iteration)
        PrintColoredText(
            f"Moyenne pour {iteration} tirages entre 0 et {n} : {averageIt}",
            Color.PURPLE,
        )
    print()
    FinishedGame()
    print()


AverageIteration()
#######################################################################################################################
# Exercice 3
# Fonction récupérant les valeurs des tests
# pour les transmettre à la fonction de calcul et d'affichage de l'exercice 3.


def CheckCorrectValue():
    print()
    while True:
        n = InputColoredText(f"{UseMsgTwo}", Color.YELLOW)
        result = ValidConditionCent(n)
        if (result) is not None:
            return result


##########
# Fonction condition nombre entre 0 et 100 inclus.


def ValidConditionCent(n):
    print()
    ZeroCent = KeyBoardControl(n)
    if ZeroCent is not None and 0 <= ZeroCent <= 100:
        return ZeroCent
    elif ZeroCent is None:
        PrintColoredText(
            f"{ErrMsgThree}",
            Color.RED,
        )
    else:
        PrintColoredText(
            f"{ErrMsgTwo}",
            Color.RED,
        )
    print()


###########
# Fonction générant un nombre aléatoiresel et condition (plus grand ou plus petit)


def FindCorrectValue():
    nTwo = int(100 * random())
    Attempts = 0
    LessMore = -1
    PrintColoredText(f"{InMsgFive}", Color.BLUE)
    while LessMore != nTwo:
        LessMore = CheckCorrectValue()
        Attempts += 1

        if LessMore < nTwo:
            PrintColoredText("🐶😲 PLUS GRAND 🐶😲", Color.PURPLE)
        elif LessMore > nTwo:
            PrintColoredText("🐶😲 PLUS PETIT 🐶😲", Color.PURPLE)
        else:
            PrintColoredText(f"👏👏 BRAVO, c'était le nombre {nTwo} 👏👏", Color.PURPLE)

    PrintColoredText(f"👏👏  Nombre de tentative(s) : {Attempts}  👏👏", Color.PURPLE)
    print()
    FinishedGame()
    print()


FindCorrectValue()


#######################################################################################################################
# Exercice 4
# Fonction récupérant les valeurs des tests
# pour les fournir aux fonctions de calcul des exercices 4 et 6.


def CheckValueNumber():
    while True:
        n = InputColoredText(f"{UseMsgThree}", Color.YELLOW)
        result = DivisionForTwo(n)

        if (result) is not None:
            return result


##########
# Fonction condition entier saisi positif ou nul.


def DivisionForTwo(n):
    StrictValid = KeyBoardControl(n)
    if StrictValid is not None and StrictValid >= 0:
        return StrictValid
    elif StrictValid is None:
        print()
        PrintColoredText(
            f"{ErrMsgThree}",
            Color.RED,
        )
    else:
        PrintColoredText(
            f"{ErrMsgThree}",
            Color.RED,
        )
    print()


##########
# Fonction calculant et affichant le résultat converti en entier de la division de n par 2
def ResultDivision():
    PrintColoredText(f"{InMsgFour}", Color.BLUE)
    print()
    DivResult = CheckValueNumber()
    print()
    result = DivResult // 2
    PrintColoredText(
        f"Résultat de la division de {DivResult} par 2 : {result}", Color.PURPLE
    )
    print()
    FinishedGame()
    print()


ResultDivision()


#####################################################################################################################
# Exercice 5
# Fonction utilisant une structure répétitive pour afficher des étoiles.
def Star():
    InputColoredText(
        f"{UseMsgFour}",
        Color.YELLOW,
    )
    print()

    for i in range(1, 6):
        PrintColoredText("*" * i, Color.PURPLE)

    print()
    FinishedGame()
    print()


Star()


################################################################################################################
# Exercice 6
# Fonction des puissances de 2 successives de 0 jusqu'à n et affichage.
def PowerOfTwo():
    PrintColoredText(
        f"{InMsgSeven}",
        Color.BLUE,
    )
    print()
    nPower = CheckValueNumber()
    print()
    while nPower < 0:
        print()
    PrintColoredText(f"{InMsgSix} : {nPower}", Color.PURPLE)
    print()
    for i in range(nPower + 1):
        result = 2**i
        PrintColoredText(f" {i}:{result}", Color.PURPLE, end=",")
    print()
    print()
    GameCounter()
    print()


PowerOfTwo()


####################################################################################################################
# Fin des jeux
# Fonction indiquant avec message la fin des jeux.
def MovieEmoji():
    emojis = [
        "\U0001F600",
        "\U0001F603",
        "\U0001F44B",
        "\U0001F605",
        "\U0001F601",
        "\U0001F44B",
        "\U0001F606",
        "\U0001F605",
        "\U0001F44B",
        "\U0001F602",
        "\U0001F923",
    ]

    j = 0
    print()
    while j < 24:
        if j + 1 == 24:
            for emoji in emojis:
                print(f"{emoji}", end=" ")
                time.sleep(1.0)
        else:
            print(" ", end=" ")
        j += 1
    print("")
    print()


if __name__ == "__main__":
    MovieEmoji()
##########


def MovieGoodBye():
    GoodBye = [
        "Merci",
        " d'avoir",
        " joué,",
        " c'est",
        " l'heure",
        " de",
        " nous",
        " dire",
        " au",
        " revoir",
        "...",
    ]
    j = 0
    print()
    while j < 18:
        if j + 1 == 18:
            for Good in GoodBye:
                PrintColoredText(f"{Good}", Color.CYAN, end="")
                time.sleep(1.5)
        else:
            print(" ", end=" ")
        j += 1
    print("")
    print()


if __name__ == "__main__":
    MovieGoodBye()
############


def GameOver():
    j = 0
    print()
    while j < 28:
        if j + 1 == 28:
            PrintColoredText(f"{InMsgNine}", Color.CYAN, end="")
            time.sleep(1.5)
        else:
            print(" ", end=" ")
        j += 1
    print("")
    print()
    print()


GameOver()
