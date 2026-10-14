def some_function(some_data):
    some_data = 100
    print("Even though we changed the parameter to 100", some_data)

def main():
    some_data_in_main = 5
    some_function(some_data_in_main)
    print(some_data_in_main)

if __name__ == "__main__":
    main()