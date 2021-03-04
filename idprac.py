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
