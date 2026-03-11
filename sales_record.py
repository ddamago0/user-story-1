def sales_record():
    product = input ("Enter the product name: ")
    price = float (input("Enter the price of the product: "))
    quantity = int (input("Enter the quantity sold: "))

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }
    return sale
print (sales_record())