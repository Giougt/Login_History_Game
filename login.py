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
    a = input("you must stop the time after"+str(timeToFind/1000)+"secondes, the time start when you press any touch")
    timeBegin = time.time()
    b = input("the timer stop when you press any touch")
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
    #
    pointAll = 0
    return maj(pointAll)

def menu():
    answer = str(input("What you want to do ? \n 1_ bingo \n 2_timing \n  3_..."))
    match answer :
        case _ if answer == "bingo":
            return gameOne()
    match answer :
        case _ if answer == "timing":
            return gameTwo()
    match answer :
        case _ if answer == 3:
            return gameThree()


#start menu 
menu()
