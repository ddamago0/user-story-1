def generate_summary(product_totals, total_revenue):
    
    print ("\n SALES SUMMARY OF THE DAY \n")

    for product, quantity in product_totals.items():
        print ("product:", product)
        print ("total quantity sold:", quantity)
        print ()
    
    print ("TOTAL REVENUE: $", total_revenue)

