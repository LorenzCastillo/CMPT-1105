def main():
    students_table = [
        ["Name", "Age", "Test Score"],
        ["Jill", 18, 75],
        ["Jack", 25, 65],
    ]

    print(students_table)
    print(len(students_table))
    print(students_table[0])
    print(students_table[0][0])

    for row in students_table:
        for col in row:
            print(col, end=" ")
        print("")

    goal_number_column = 5
    goal_number_row = 3



if __name__ == '__main__':
    main()