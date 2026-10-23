def get_amount_sold(type_of_salsa):
    result = int(input("How many jars of " + type_of_salsa + " salsa did you sell? "))

    while result < 0:
        print("Error: Must be a positive value")
        result = int(input("How many jars of " + type_of_salsa + " salsa did you sell? "))

    return result

def get_total_sales(sales_data):
    total_sales = 0
    for category in sales_data:
        total_sales += category
    return total_sales

def find_index_biggest_sales(sales_data):
    guess_of_best_sales = 0
    index_of_best_sales = -1

    for index in range(len(sales_data)):
        if sales_data[index] > guess_of_best_sales:
            guess_of_best_sales = sales_data[index]
            index_of_best_sales = index
    return index_of_best_sales

def find_index_worst_sales(sales_data):
    guess_of_best_sales = sales_data[0]
    index_of_worst_sales = 0

    for index in range(len(sales_data)):
        if sales_data[index] < guess_of_best_sales:
            guess_of_best_sales = sales_data[index]
            index_of_worst_sales = index
    return index_of_worst_sales

def main():
    all_salsa_types = ["Mild", "Medium", "Sweet", "Hot", "Zesty"]
    amount_sold_per_type = [-1, -1, -1, -1, -1]

    for index in range(len(all_salsa_types)):
        amount_sold_per_type[index] = get_amount_sold(all_salsa_types[index])
    total_sales = get_total_sales(amount_sold_per_type)
    index_of_best = find_index_biggest_sales(amount_sold_per_type)
    index_of_worst = find_index_worst_sales(amount_sold_per_type)


    print("In total, the company sold", total_sales, "types of salsas")
    print("In index of best sales, the company sold", all_salsa_types[index_of_best])
    print("In index of worst sales, the company sold", all_salsa_types[index_of_worst])

if __name__ == '__main__':
    main()