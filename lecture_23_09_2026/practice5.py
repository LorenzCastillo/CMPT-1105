def main():
    gradeInput = int(input("What is your grade? "))

    if gradeInput > 85:
        print("Your grade is A")
    elif gradeInput > 75:
        print("Your grade is B")
    elif gradeInput > 65:
        print("Your grade is C")
    elif gradeInput > 50:
        print("Your grade is D")
    elif gradeInput > 0:
        print("Your grade is F")
    else:
        print("You cannot have negative grade")


if __name__ == "__main__":
    main()