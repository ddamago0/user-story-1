def sales_record():
    # Product validation
    valid_product = False

    while not valid_product:
        product = input("Enter the product name: ").strip()

        if product == "":
            print("Error: product name cannot be empty.")

        elif product.isdigit():
            print("Error: product name cannot be a number.")

        else:
            valid_product = True


    # Price validation
    valid_price = False

    while not valid_price:
        try:
            price = float(input("Enter the price of the product: "))

            if price <= 0:
                print("Error: price must be greater than 0.")
            else:
                valid_price = True

        except ValueError:
            print("Error: please enter a valid number.")


    # Quantity validation
    valid_quantity = False

    while not valid_quantity:
        try:
            quantity = int(input("Enter the quantity sold: "))

            if quantity <= 0:
                print("Error: quantity must be greater than 0.")
            else:
                valid_quantity = True

        except ValueError:
            print("Error: please enter a valid integer.")

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }
    return sale