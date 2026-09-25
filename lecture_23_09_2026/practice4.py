def practice4():
    testScore = int(input("Enter your test score: "))

    if (0 <= testScore <= 100) and (testScore % 2 == 0):
        print("That's a cool test score")
    else:
        print("Your test score isn't cool")
        if testScore > 100:
            print("That test score is above 100")
        if testScore < 0:
            print("That test score is below 0")
        if testScore % 2 == 1:
            print("That test score is odd")



if __name__ == "__main__":
    practice4()