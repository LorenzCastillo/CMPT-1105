def tryCatchPractice():

    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Please enter a number")
        tryCatchPractice()


if __name__ == "__main__":
    tryCatchPractice()