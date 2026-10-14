def sum_num_divisible(starting_value, dividing_value, ending_value):
    sum_of_numbers = 0

    for num in range(starting_value, ending_value):
        if num % dividing_value == 0:
            print(num, end=" ")
            sum_of_numbers += num

    return sum_of_numbers

def main():
    print("\nSum of numbers from 0-100 divisible by 3:", sum_num_divisible(0, 3, 100))
    print("---")
    print("\nSum of numbers from 0-10 divisible by 5:", sum_num_divisible(0, 5, 20))

if __name__ == "__main__":
    main()
