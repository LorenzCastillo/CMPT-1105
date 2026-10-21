def main():
    all_student_ages = [10, 11, 14, 18, 20]
    print(max(all_student_ages))

    guess_of_biggest_num = all_student_ages[0]

    for age in all_student_ages:
        if age > guess_of_biggest_num:
            guess_of_biggest_num = age
    print("The biggest things we found was", guess_of_biggest_num)

    print("-------")

    all_student_ages.reverse()
    print(all_student_ages)

    all_student_ages.sort()
    print(all_student_ages)

if __name__ == '__main__':
    main()