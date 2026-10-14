def print_evens():
    sum_of_evens = 0

    for num in range(1, 101):
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens

def main():
    print("The sum of all even numbers from 1-100 is:", print_evens())

if __name__ == "__main__":
    main()