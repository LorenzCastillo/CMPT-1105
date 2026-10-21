def main():
    ages = []
    SENTINEL_HALT = -1

    age_input = int(input("Enter an age, or enter -1 if you'd like to exit): "))

    while age_input != SENTINEL_HALT:
        if age_input < 0:
            print("Error: Please enter a valid age greater than 0")
        else:
            ages.append(age_input)
        age_input = int(input("Enter another age, or enter -1 if you'd like to exit: "))

    print("Age list", ages)
    print("Oldest age is", max(ages))

if __name__ == '__main__':
    main()

