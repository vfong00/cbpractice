import random
import time
from random import shuffle

# constant strings
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sep = "======================================"

# returns abstracts word to its structure alphabetically
# ex: PEOPLE -> ABCADB
# this is used to group together structurally equal words, like "that" and "else"
def structure(word):
    uniqueLetters = ""
    ans = ""
    for c in word:
        if c not in uniqueLetters:
            uniqueLetters += c
        ans += alpha[uniqueLetters.index(c)]
    return ans

# given list of words, picks random word and encrypts it randomly
# returns this word and the original
# postcondition: no letter previously in the word maps to itself
def genWord(words):
    wordSet = random.choice(words)
    word = wordSet[0]
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
    return [ans, word, wordSet[1]]

# function that's run in the loop
# basically, a checking prompt for question-answer, and tracks stats
def inLoop(words, structures, streak, correct, total, end):
    encDecStruc = genWord(words)
    pattern = encDecStruc[0]
    word = encDecStruc[1]
    wordStruc = encDecStruc[2]

    print("Pattern: " + pattern)
    start = time.time()
    inp = input("Answer: ").strip()
    elapsed = time.time() - start
    if (inp.lower() == "end"):
        print("\n" + sep)
        return streak, correct, total, True
    ans = inp.upper()
    if (ans == word or ans in structures[wordStruc]):
        print("Correct!")
        altForms = [x for x in structures[wordStruc] if x != ans]
        if len(altForms) != 0:
            print("Alternate forms: " + ", ".join(altForms))
        correct += 1
        streak += 1
        if (streak > 4):
            print(streak + " streak.")
    else:
        print("Incorrect. Correct answer(s): " + ", ".join([x for x in structures[wordStruc]]))
        streak = 0
    total += 1
    input("Press ENTER to continue.")
    print(sep)
    return streak, correct, total, elapsed, end

def initWordsAndStructs(file):
    words = []
    structures = dict()
    for w in file:
        word = w.strip().upper()
        structWord = structure(word)
        words += [[word, structWord]]
        if structWord in structures:
            structures[structWord].append(word)
        else:
            structures[structWord] = [word]
    return words, structures


def main():
    # initialization -- word list
    f = open("words.txt", "r")
    words, structures = initWordsAndStructs(f)
    f.close()

    # initialization -- variables
    inp = ""
    streak, correct, total, end = 0, 0, 0, False
    maxStreak = 0
    totalTime = 0

    # initialization -- terminal print
    print(chr(27) + "[2J")
    print("Welcome to pattern practice.")
    print("Enter 'end' at any time to close.")
    # print("Enter 'help' for more commands and usage.") (TODO)
    print(sep)

    # loop
    while not end:
        streak, correct, total, time, end = inLoop(words, structures, streak, correct, total, end)
        maxStreak = max(streak, maxStreak)
        totalTime += time

    # print ending stats
    print("SESSION SUMMARY: ")
    print("Correct: " + str(correct))
    print("Total: " + str(total))
    if total != 0:
        print("Percentage: " + str(round(correct / total * 100, 2)) + "%")
    else:
        print("Percentage: 0%")
    print("Highest streak: " + str(maxStreak))
    print("Average time: " + str(round(totalTime / total, 2)) + "s")
    print("Goodbye :)")
    print(sep + "\n")

main();
