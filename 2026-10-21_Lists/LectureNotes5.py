def test_function_weird(list_that_is_shared, regular_variable):
    list_that_is_shared.append(100)
    regular_variable = 100

def main():
    some_data_in_main = [1, 2, 3]
    some_regular_var = 5
    print("Before running the function, list is", some_data_in_main)
    print("Before running the function, var is", some_regular_var)
    test_function_weird(some_data_in_main, some_regular_var)

    print("After running the function, list is", some_data_in_main)
    print("After running the function, var is", some_regular_var)

if __name__ == "__main__":
    main()