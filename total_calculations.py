def calculate_totals (sales_list):

    product_totals = {}
    total_revenue = 0

    for sale in sales_list:
        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]

        if product in product_totals:
            product_totals[product] += quantity

        else:
            product_totals[product] = quantity

        total_revenue += price * quantity

    return product_totals, total_revenue