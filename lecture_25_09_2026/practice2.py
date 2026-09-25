def practice2():
    MAX_INFANT_AGE = 1
    MAX_CHILD_AGE = 13
    MAX_TEENAGER_AGE = 20

    userAge = int(input("How old are you? "))

    if userAge < 0:
        print("Cannot be negative years old")

    if userAge <= MAX_INFANT_AGE:
        print("You are an infant")
    elif userAge <= MAX_CHILD_AGE:
        print("You are a child")
    elif userAge <= MAX_TEENAGER_AGE:
        print("You are a teenager")
    else:
        print("You are an adult")

if __name__ == "__main__":
    practice2()