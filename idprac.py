import random
import time

# constant strings and lists
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = list(range(26))
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
bacon = ["AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB","AABBA","AABBB","ABAAA","ABAAA","ABAAB","ABABA","ABABB","ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB","BAABA","BAABB","BAABB","BABAA","BABAB","BABBA","BABBB"]
sep = "======================================"

def idprac(alphaSet, streak, correct, total, end, endAll):
    letter = random.choice(alpha)
    encode = alphaSet[alpha.index(letter)]
    letNum = [letter, encode]
    letNumInd = random.randint(0, 1)

    start = time.time()
    inp = input(str(letNum[letNumInd]) + " -> ").strip()
    elapsed = time.time() - start

    if (inp.lower() == "return" or inp.lower() == "exit"):
        print("\n" + sep)
        return streak, correct, total, 0, True, inp.lower() == "exit"

    if inp.upper() == str(letNum[(letNumInd + 1) % 2]):
        print("Correct!")
        correct += 1
        streak += 1
        if (streak > 4):
            print(str(streak) + " streak.")
    else:
        print("Incorrect. Correct answer was " + str(letNum[(letNumInd + 1) % 2]))
        streak = 0
    total += 1
    k = input("\nPress ENTER to continue. Type 'return' to return to the menu, and 'exit' to stop the program. \n> ")
    if (k.strip().lower() == "return" or k.strip().lower() == "exit"):
        print("\n" + sep)
        return streak, correct, total, elapsed, True, k.strip().lower() == "exit"
    print(sep)
    return streak, correct, total, elapsed, end, endAll

def idloop():
    # initialization -- variables
    inp = ""
    streak, correct, total, end, endAll = 0, 0, 0, False, False
    maxStreak = 0
    totalTime = 0

    # initialization -- terminal print
    print(chr(27) + "[2J")
    print("Welcome to cipher ID practice.")
    print("There are three modes: 'alpha' for letter-numbers, 'morse', and 'bacon'.")
    print("Enter 'return' at any time to return to the menu, or 'exit' to stop this program.")
    mode = input("Select mode: ").strip().lower()
    while mode != "alpha" and mode != "morse" and mode != "bacon" and mode != "return" and mode != "exit":
        mode = input("Invalid argument. Select mode: ")
    print(sep)

    while not end:
        if mode == "return" or mode == "exit":
            return mode == "exit"
        elif mode == "alpha":
            streak, correct, total, time, end, endAll = idprac(nums, streak, correct, total, end, endAll)
        elif mode == "bacon":
            streak, correct, total, time, end, endAll = idprac(bacon, streak, correct, total, end, endAll)
        elif mode == "morse":
            streak, correct, total, time, end, endAll = idprac(morse, streak, correct, total, end, endAll)
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
