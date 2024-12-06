import datetime

def log():
    nowTime = datetime.datetime.now().strftime("%H:%M:%S")
    nowDate = datetime.datetime.now().date()
    strLog = f"Date: {nowDate} Time: {nowTime}\n"
    with open('login_history.txt', 'a') as f:
        f.write(strLog)

try:
    with open('login_history.txt', 'x') as file:
        print("file create")
except FileExistsError:
    print("File already exists.")
    log()
