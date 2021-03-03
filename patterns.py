import random
from random import shuffle

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sep = "======================================"

def genWord(words):
    word = random.choice(words)
    ans = ""
    uniqueMaps = False
    while not uniqueMaps:
        uniqueMaps = True
        shuffleAlphaList = list(alpha)
        shuffle(shuffleAlphaList)
        shuffleAlpha = ''.join(shuffleAlphaList)
        for c in word:
            if (shuffleAlpha[alpha.index(c)] != c):
                ans += shuffleAlpha[alpha.index(c)]
            else:
                uniqueMaps = False
                ans = ""
                break
    return [ans, word]

def inLoop(words, streak, correct, total, end):
    encDec = genWord(words)
    print(encDec[0])
    inp = input("Answer: ")
    if (inp.lower() == "end"):
        print("\n" + sep)
        return streak, correct, total, True
    if (inp.strip().upper() == encDec[1]):
        print("Correct!")
        correct += 1
        streak += 1
        if (streak > 4):
            print(streak + " streak.")
    else:
        print("Incorrect. Correct answer is: " + encDec[1])
        streak = 0
    total += 1
    print(sep)
    return streak, correct, total, end

def main():
    # initialization -- word list
    f = open("words.txt", "r")
    words = []
    for word in f:
        words += [word.strip().upper()]
    f.close()

    # initialization -- variables
    inp = ""
    streak, correct, total, end = 0, 0, 0, False
    maxStreak = 0

    # initialization -- terminal print
    print(chr(27) + "[2J")
    print("Welcome to pattern practice.")
    print("Enter 'end' at any time to close.")
    print("Enter 'help' for more commands and usage.")
    print(sep)

    # loop
    while not end:
        streak, correct, total, end = inLoop(words, streak, correct, total, end)
        maxStreak = max(streak, maxStreak)

    # print ending stats
    print("SESSION SUMMARY: ")
    print("Correct: " + str(correct))
    print("Total: " + str(total))
    if total != 0:
        print("Percentage: " + str(round(correct / total * 100, 2)) + "%")
    else:
        print("Percentage: 0%")
    print("Highest streak: " + str(maxStreak))
    print("Goodbye :)")
    print(sep + "\n")



main();
