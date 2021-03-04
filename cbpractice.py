import patterns
import letnums
import idprac

def main():
    modes = ["patterns", "letnums", "idprac"]
    print(chr(27) + "[2J")
    print("Welcome to cbpractice.")
    while True:
        inp = input("Please choose a mode of practice. \nType 'list' for a list of implemented modes. \nType 'exit' to end session: ").strip().lower()
        if inp == "list": print("\nCurrent modes: " + ", ".join(modes) + "\n")
        elif inp == "exit": break
        elif inp == "patterns":
            end = patterns.patterns()
            if end: break
            print(chr(27) + "[2J")
        elif inp == "letnums":
            end = letnums.letnums()
            if end: break
            print(chr(27) + "[2J")
        elif inp == "idprac":
            end = idprac.idloop()
            if end: break
            print(chr(27) + "[2J")
        else: print("\nSorry, this is not a recognized mode. Try again. \n")



if __name__ == "__main__":
    main()
