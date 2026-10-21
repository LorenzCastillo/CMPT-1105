def main():
    all_students_ages = [1, 2, 3, 10, 5]
    all_students_ages.append(10)
    print(all_students_ages)

    print("Starting ages", all_students_ages)
    all_students_ages.remove(10)

    if 100 in all_students_ages:
        all_students_ages.remove(100)

    print("is now: ", all_students_ages)


if __name__ == "__main__":
    main()