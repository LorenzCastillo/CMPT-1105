def print_evens():
    for num in range(1, 100):
        if num % 2 == 0:
            print(num, end=" ")
    print("\n---")

def main():
    print_evens()
    print_evens()
    print_evens()

if __name__ == "__main__":
    main()