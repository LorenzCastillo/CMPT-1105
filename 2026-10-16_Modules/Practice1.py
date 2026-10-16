CLASS_A_COST = 20
CLASS_B_COST = 15
CLASS_C_COST = 10

def get_total_sales(amount_class_a, amount_class_b, amount_class_c):
    total_sales = ((amount_class_a * CLASS_A_COST) +
                   (amount_class_b * CLASS_B_COST) +
                   (amount_class_c * CLASS_C_COST))
    return total_sales

def is_amount_sold_reasonable(amount_sold):
    return amount_sold > 0

def get_amount_sold(category_to_grab):
    amount_sold = int(input("How many " + str(category_to_grab) + " tickets were sold? "))

    while not is_amount_sold_reasonable(amount_sold):
        print("Please enter a valid amount sold")
        amount_sold = int(input("How many " + str(category_to_grab) + " tickets were sold? "))
    return amount_sold

def main():
    num_class_a = get_amount_sold("class a")
    num_class_b = get_amount_sold("class b")
    num_class_c = get_amount_sold("class c")

    result = get_total_sales(num_class_a, num_class_b, num_class_c)
    print("Total sales this weeks were:", result)

if __name__ == '__main__':
    main()