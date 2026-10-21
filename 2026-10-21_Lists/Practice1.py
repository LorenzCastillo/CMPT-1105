def main():
    student_age_list = [0, 0, 0, 0, 0]

    for index in range(len(student_age_list)):
        # Indexes start at 0, so add +1 just for formating for the user
        print("How old is student #", index+1 ,"?", sep="", end=" ")
        student_age = int(input())

        # Error check to see if the user put a number 0 and under
        while student_age < 0:
            print("Error: Must be a positive value, please try again\n")
            print("How old is student #", index + 1, "?", sep="", end=" ")
            student_age = int(input())

        student_age_list[index] = student_age

    print(student_age_list)

if __name__ == '__main__':
    main()

