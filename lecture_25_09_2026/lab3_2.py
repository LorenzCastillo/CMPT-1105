def textDivider():
    print("------------")

def lab3_2():
    GRAVITY = 9.81
    MIN_WEIGHT = 10
    MAX_WEIGHT = 425

    while True:
        try:
            objectMass = float(input("Enter the mass of your object: "))
            # W = M * G
            weightInNewtons = objectMass * GRAVITY
            # Between 10 and 425 is a good weight. Otherwise, it's either too light or too heavy
            # And if it's less than 0, it shouldn't be possible
            if weightInNewtons < 0:
                print("Error: You can't have negative mass")
                textDivider()
                continue
            elif weightInNewtons < MIN_WEIGHT:
                print("Your object (", format(weightInNewtons, ".1f"), "N) is too light", sep="")
            elif weightInNewtons > MAX_WEIGHT:
                print("Your object (", format(weightInNewtons, ".1f"), "N) is too heavy", sep="")
            else:
                print("Your object (", format(weightInNewtons, ".1f"), "N) is just the right size!", sep="")
            break
        except ValueError:
            print("Error: Please enter a numeric value")

        textDivider()

if __name__ == "__main__":
    lab3_2()