def print_and_sum_evens():
    sum_of_evens = 0

    for num in range(1, 100):
        if num % 2 == 0:
            print(num, end=" ")
            sum_of_evens += num
    return sum_of_evens

def main():
    print("\nThe sum of all even numbers from 1-100 is:", print_and_sum_evens())

if __name__ == "__main__":
    main()