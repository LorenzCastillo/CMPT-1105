def print_greater_than(list_to_search, minimum_val_print):
    print("Printing all elements in", list_to_search, "bigger than", minimum_val_print)

    for element in list_to_search:
        if element > minimum_val_print:
            print("We found this big element:", element)

def main():
    print_greater_than([1, 2, 3, 4, 5], 2)

if __name__ == "__main__":
    main()