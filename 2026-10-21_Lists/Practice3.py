SENTINEL_HALT = -1

def calculate_average_in_list(num_list):
    sum_of_all_numbers = 0

    for num in num_list:
        sum_of_all_numbers += num
    return sum_of_all_numbers/len(num_list)

def add_to_list(num_list, item):
    num_list.append(item)

def main():
    num_list = []
    num_input = int(input("Enter an integer, or type -1 to exit: "))

    while num_input != SENTINEL_HALT:
        add_to_list(num_list, num_input)
        num_input = int(input("Enter another integer, or type -1 to exit: "))

    print("The average is", calculate_average_in_list(num_list))

if __name__ == "__main__":
    main()