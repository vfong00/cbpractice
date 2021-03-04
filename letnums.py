import random
import time

# constant strings
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sep = "======================================"

def math(streak, correct, total, end, endAll):
    letter1 = random.choice(alpha)
    letter2 = random.choice(alpha)
    addSub = random.randint(0, 1)
    operators = [" + ", " - "]
    start = time.time()
    inp = input("\'" + letter1 + "\'" + operators[addSub] + "\'" + letter2 + "\'?\n")
    elapsed = time.time() - start
    if (inp.lower() == "return" or inp.lower() == "exit"):
        print("\n" + sep)
        return streak, correct, total, 0, True, inp.lower() == "exit"
    if addSub == 0:
        sum = alpha[(alpha.index(letter1) + alpha.index(letter2)) % 26]
    else:
        sum = alpha[(alpha.index(letter1) - alpha.index(letter2)) % 26]
    if inp.upper() == sum:
        print("Correct!")
        correct += 1
        streak += 1
        if (streak > 4):
            print(streak + " streak.")
    else:
        print("Incorrect. Correct answer was " + sum)
        streak = 0
    total += 1
    k = input("\nPress ENTER to continue. Type 'return' to return to the menu, and 'exit' to stop the program. \n> ")
    if (k.strip().lower() == "return" or k.strip().lower() == "exit"):
        print("\n" + sep)
        return streak, correct, total, elapsed, True, k.strip().lower() == "exit"
    print(sep)
    return streak, correct, total, elapsed, end, endAll

def id(streak, correct, total, end, endAll):
    return

def letnums():
    # initialization -- variables
    inp = ""
    streak, correct, total, end, endAll = 0, 0, 0, False, False
    maxStreak = 0
    totalTime = 0

    # initialization -- terminal print
    print(chr(27) + "[2J")
    print("Welcome to letter-numbers practice.")
    print("There are two modes: 'math' for addition/subtraction practice, and 'id' to quick id")
    print("Enter 'return' at any time to return to the menu, or 'exit' to stop this program.")
    mode = input("Select mode: ").strip().lower()
    while mode != "math" and mode != "id" and mode != "return" and mode != "exit":
        mode = input("Invalid argument. Select mode: ")
    print(sep)

    while not end:
        if mode == "return" or mode == "exit":
            return mode == "exit"
        elif mode == "math":
            streak, correct, total, time, end, endAll = math(streak, correct, total, end, endAll)
        elif mode == "id":
            streak, correct, total, time, end, endAll = id(streak, correct, total, end, endAll)
        maxStreak = max(streak, maxStreak)
        totalTime += time

    # print ending stats
    print("SESSION SUMMARY: ")
    print("Correct: " + str(correct))
    print("Total: " + str(total))
    if total != 0:
        print("Percentage: " + str(round(correct / total * 100, 2)) + "%")
        print("Average time: " + str(round(totalTime / total, 2)) + "s")
    else:
        print("Percentage: 0%")
        print("Average time: 0s")
    print("Highest streak: " + str(maxStreak))
    print("Goodbye :)")
    print(sep + "\n")
    if not endAll:
        input("(Press ENTER to return)")
    return endAll
