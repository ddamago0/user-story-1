from sales_record import sales_record
sales_list = []

continue_registering = True

while continue_registering:
    sale = sales_record()
    sales_list.append(sale)

    answer = input("Do you want to register another sale? (yes/no): ")
    if answer.lower() != "yes":
        continue_registering = False