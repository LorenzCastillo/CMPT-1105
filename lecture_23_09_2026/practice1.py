def main():
    score1 = int(input("Enter the score for test 1: "))
    score2 = int(input("Enter the score for test 2: "))
    score3 = int(input("Enter the score for test 3: "))

    scoreAverage = (score1 + score2 + score3) / 3

    if scoreAverage >= 95:
        print("Congratulations!")
        print("That is a great average!")
    else:
        print("Get help.")

if __name__ == '__main__':
    main()

