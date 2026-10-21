def main():
    # Make this list 10 times longer by adding these variables to one array 10 times
    all_student_ages = [10, 11, 12, 13, 14] * 10
    # List slicing between (but not including) index 2 and index 4
    print(all_student_ages[2:4])

    interesting_chunk = all_student_ages[2:4]
    interesting_chunk[0] = 100

    print("Original list is still", all_student_ages)
    print("Interesting chunk was changed", interesting_chunk)


    if 10 in all_student_ages:
        print("Someone is exactly 10 years old")
    if 100 not in all_student_ages:
        print("Someone is not exactly 100 years old")

if __name__ == "__main__":
    main()