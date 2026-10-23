def main():
    my_constant_sequence = (1, 2, 3, 4, 5)
    other_data = (3, 4)

    print(my_constant_sequence)
    print(my_constant_sequence[0])

    print(my_constant_sequence + other_data)

    print("The original tuple is unchanged", my_constant_sequence)

if __name__ == '__main__':
    main()