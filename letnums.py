import random
import time

# constant strings
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sep = "======================================"

def math(streak, correct, total, end, endAll):
    return

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
    mode = input("Select mode: ")
    while mode != "math" or mode != "id":
        mode = input("Invalid argument. Select mode: ")
    print(sep)

    while not end:
        if mode == "math":
            streak, correct, total, time, end, endAll = math(streak, correct, total, end, endAll)
        elif mode == "id":
            streak, correct, total, time, end, endAll = id(streak, correct, total, end, endAll)
        maxStreak = max(streak, maxStreak)
        totalTime += time
