def main():
    all_students_in_class = ["Izabelle", "Lorenz", "Owen", "Fred", "Sid"]

    for student_name in all_students_in_class:
        print(student_name)

    print("----------")

    student_ages = [18, 25, 36]
    # Testing to see if this method would change the value inside the array
    for student_age in student_ages:
        student_age += 1
        print(student_age)
    # Proof that the original array never changed
    print(student_ages)

    # Do this instead
    for index in range(len(student_ages)):
        student_ages[index] += 1
    print(student_ages)


    print("----------")

if __name__ == '__main__':
    main()