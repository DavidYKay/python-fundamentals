def guess():
    #upper = 1000000
    upper = 100
    lower = 0
    num_guesses = 0
    found = False

    while not found:
        g = (upper + lower) / 2
        print("My guess is: %d" % g)
        s = input("(G)reater/(L)esser/(C)orrect?\n")
        s = s.strip().upper()
        if s == "G":
            lower = g
            num_guesses += 1
        elif s == "L":
            upper = g
            num_guesses += 1
        elif s == "C":
            found = True
        else:
            print("Unknown input. Please try again")

    print("I guessed your number, %d, in %d guesses" % (g, num_guesses))

def main():
    print("Think of any number between 0 and 100")
    guess()

main()
