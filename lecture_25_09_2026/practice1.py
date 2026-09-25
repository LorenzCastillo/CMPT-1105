def practice1():
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    MONDAY_TEXT = "MONDAY"
    TUESDAY_TEXT = "TUESDAY"
    WEDNESDAY_TEXT = "WEDNESDAY"
    THURSDAY_TEXT = "THURSDAY"
    FRIDAY_TEXT = "FRIDAY"
    SATURDAY_TEXT = "SATURDAY"
    SUNDAY_TEXT = "SUNDAY"

    numeric_day_of_week = int(input("Enter in what day it is 1(monday) to 7(sunday): "))

    if numeric_day_of_week < MONDAY or numeric_day_of_week > SUNDAY:
        print("Please enter a valid day of the week from 1-7")
        exit()

    if numeric_day_of_week == MONDAY:
        print(MONDAY_TEXT)
    elif numeric_day_of_week == TUESDAY:
        print(TUESDAY_TEXT)
    elif numeric_day_of_week == WEDNESDAY:
        print(WEDNESDAY_TEXT)
    elif numeric_day_of_week == THURSDAY:
        print(THURSDAY_TEXT)
    elif numeric_day_of_week == FRIDAY:
        print(FRIDAY_TEXT)
    elif numeric_day_of_week == SATURDAY:
        print(SATURDAY_TEXT)
    else:
        print(SUNDAY_TEXT)

if __name__ == "__main__":
    practice1()