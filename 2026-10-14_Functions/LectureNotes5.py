def sum_num_divisible(starting_value, dividing_value, ending_value):
    sum_of_numbers = 0

    for num in range(starting_value, ending_value):
        if num % dividing_value == 0:
            print(num, end=" ")
            sum_of_numbers += num

    return sum_of_numbers, 15

def say_hi_with_assumptions(greeting="Hello world!"):
    print(greeting)

def main():
    the_answer, other_answer = sum_num_divisible(0, 10, 100)
    print("\nSum of those numbers are", the_answer)
    print("The other answer is", other_answer)

    print("-----")

    say_hi_with_assumptions()
    say_hi_with_assumptions("The user specified something more specific")

if __name__ == "__main__":
    main()
