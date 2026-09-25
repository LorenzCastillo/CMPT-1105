def practice3():

    MIN_SALARY = 30000
    MIN_YEARS_ON_JOB = 2

    salary = int(input("Enter your salary: "))

    if salary >= MIN_SALARY:
        yearsOnJob = int(input("How long have you been working there? "))

        if yearsOnJob >= MIN_YEARS_ON_JOB:
            print("You qualify for the loan!")
        else:
            print("You must be working on this job for at least 2 years to qualify")

    else:
        print("You must earn at least $30,000 per year to qualify")


if __name__ == '__main__':
    practice3()