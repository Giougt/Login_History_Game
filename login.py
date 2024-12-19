import datetime
import random

# Point to add
points = 0
# Point already have
oldPoint = 0

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
def EarnPoint(oldPoint):
    answer = str(input("Reset your point ? \"yes\" or \"no\""))
    if answer == "no": 
        points = random.randint(1, 255)
        points = points + oldPoint
    elif answer == "yes":
        points = 0
    return points

# Write in file
def maj():
    nowTime = datetime.datetime.now().strftime("%H:%M:%S")
    nowDate = datetime.datetime.now().date()
    oldPoint = getLastPoints()
    points = EarnPoint(oldPoint)
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
    user = int(input("Guest the number between 1 and 10"))
    if answer == user:
        pointE = random.randint(1,255)
    if answer != user and compt > 3:
        pointE = 0
    return 

def menu():
    maj()
    answer = str(input("What you want to do ? \n Play a game ..."))
    match answer :
        case _ if answer == 1:
            return gameOne()
    match answer :
        case _ if answer == 2:
            return gameTwo()
    match answer :
        case _ if answer == 3:
            return gameThree()


#start menu 
menu()
