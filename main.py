from sales_record import sales_record
from total_calculations import calculate_totals
from generation_of_the_final_summary import generate_summary
sales_list = []

continue_registering = True

while continue_registering:
    sale = sales_record()
    sales_list.append(sale)

    answer = input("Do you want to register another sale? (yes/no): ")
    if answer.lower() != "yes":
        continue_registering = False

product_totals, total_revenue = calculate_totals(sales_list)

generate_summary(product_totals, total_revenue)
