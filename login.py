import datetime
import random
import time 
# Point to add
points = 0
# Point already have
oldPoint = 0

#win points
def winPoint():
    pointwin = random.randint(1,255)
    return pointwin

# Get old point in file
def getLastPoints():
    try:
        with open('login_history.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                # Extract the last line and get the points
                last_line = lines[-1]
                # Assuming the last line format is "Date: YYYY-MM-DD Time: HH:MM:SS Point: X"
                oldPoint = int(last_line.strip().split("Point: ")[1])
                return oldPoint
            else:
                return 0  # No points if file is empty
    except FileNotFoundError:
        return 0  # No points if file does not exist

# Earn points random for login
def ResetPoint(oldPoint, newPoint):
    answer = str(input("Reset your point ? \"yes\" or \"no\""))
    if answer == "no": 
        points = oldPoint + newPoint
        print("success to add your new point")
    elif answer == "yes":
        points = 0
    return points


# Write in file
def maj(newPoint):
    nowTime = datetime.datetime.now().strftime("%H:%M:%S")
    nowDate = datetime.datetime.now().date()
    oldPoint = getLastPoints()
    points = ResetPoint(oldPoint,newPoint)
    strLog = f"Date: {nowDate} Time: {nowTime} Point: {points}\n"
    with open('login_history.txt', 'a') as f:
        f.write(strLog)

try:
    with open('login_history.txt', 'x') as file:
        print("File created")
except FileExistsError:
    print("File already exists.")


def gameOne():
    #bingo 
    answer = random.randint(1,10)
    compt = 0
    pointAll = 0
    while compt < 3:
        user = int(input("Guest the number between 1 and 10"))
        if answer == user:
            print("Nice you win")
            pointE = winPoint()
            pointAll = pointE + pointAll
            compt = compt + 1
            break
        if answer != user:
            compt = compt + 1
            print("False")
    print("you earn",pointAll)
    return maj(pointAll)


def gameTwo():
    #timing 
    #const
    pointAll = 0
    pointE = 0
    timeToFind = random.randint(10,20)*1000
    # +1s and -1s
    timeToFindMid1 = timeToFind - 1000
    timeToFindMid2 = timeToFind + 1000
    #part game
    a = input("you must stop the time after"+str(timeToFind/1000)+"secondes, the time start when you press the touch enter")
    timeBegin = time.time()
    b = input("the timer stop when you press the touch enter")
    timeToStopUser = time.time()
    timeToStop = (timeToStopUser - timeBegin)*1000
    print("time to find", timeToFind)
    print("your time",timeToStop)
    #check response
    if timeToFindMid1 < timeToStop < timeToFindMid2 : 
        pointE = winPoint()
        pointAll = pointE + pointAll
        print("you win this game and earn",pointAll,"points")
    else:
        print("You loose , you earn ",pointE,"point, sorry")
    return maj(pointAll)


def gameThree():
    #calculate
    # const
    pointAll = 0
    pointE = 0
    number1 = random.randint(1,255)
    number2 = random.randint(1,255)
    operationRandom = random.randint(1,4)
    match operationRandom:
        case _ if operationRandom == 1:
            correctResponse = number1 + number2
            response = int(input("Calcul this addition"+str(number1)+"+"+str(number2)))
        case _ if operationRandom == 2:
            correctResponse = number1 - number2
            response = int(input("Calcul this soustraction"+str(number1)+"-"+str(number2)))
        case _ if operationRandom == 3:
            correctResponse = number1 * number2
            response = int(input("Calcul this multiplication"+str(number1)+"x"+str(number2)))
        case _ if operationRandom == 4:
            division = number1 / number2
            correctResponse = int(round(division,0))
            response = int(input("Calcul this division"+str(number1)+"/"+str(number2)))
    if response == correctResponse: 
        pointE = winPoint()
        pointAll = pointE + pointAll
        print("you win this game and earn",pointAll,"points")
    else:
        print("You loose , you earn ",pointE,"point, sorry")
    return maj(pointAll)

def gameFour():
    # guest word
    pointAll = 0
    pointE = 0
    word_list_guess = ["qui ","ont","profondément", "modifié", "la", "capitale", "en", "lui", "donnant", "le" ,"visage" ,"on", "lui", "connait", "de", "nos", "jours", "tout" ,"en", "laissant","subsister", "des", "pans" ,"du" ,"tissu", "urbain", "antérieur", "au", "cours", "du", "siecle", "la", "physionomie", "de", "Paris", "a" ,"continue", "se", "transformer", "avec", "la", "mise", "en"]
    # random word to guess
    answer_guess = word_list_guess[random.randint(0,42)]
    # number of guess
    number_guess = 10
    # word are long , + guess 
    if len(answer_guess) > 10:
        number_guess = len(answer_guess) + 6
    # check and remove letter to check 
    split_word = list(answer_guess)
    word_actually = ["Your answer : " ]
    #loop complete _ for word answer
    for ele in range(len(answer_guess)):
        word_actually.append("_ ")
    #debug
    print(split_word)
    # print the word (answer)
    form_answer = ""
    for ele in word_actually:
        form_answer = form_answer + ele 
    # number of input loop
    for ele in range(number_guess):
        letter_answer = str(input("give one letter"))
        # compt how many guess
        number_guess = number_guess - 1
        if letter_answer in split_word:
            pointE = winPoint()
            pointAll = pointE + pointAll
            print("nice guess , you find a correct letter , number of guess left", number_guess)
            #find index to spot letter
            index_letter = 0
            index_letter = answer_guess.index(letter_answer)
            #debug
            print(index_letter)
            print(word_actually)
            print(form_answer)
        else:
            print("False, you don't find a correct letter, number of guess left", number_guess)
    return maj(pointAll)


def menu():
    answer = str(input("What you want to do ? \n 1_ bingo \n 2_timing \n  3_calculate \n  4_guess word \n 5_exit"))
    match answer :
        case _ if answer == "bingo":
            return gameOne()
        case _ if answer == "timing":
            return gameTwo()
        case _ if answer == "calculate":
            return gameThree()
        case _ if answer == "guess word":
            return gameFour()
        case _ :
            answer_exit = str(input("You want to exit ? \n Yes or No"))
            if answer_exit == "Yes":
                return 0
            else:
                print("no exit sucess")


#start menu 
menu()
