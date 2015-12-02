name=raw_input("Enter the customer name to find orders")

with open("orders.txt") as f:
    for line in f:
        if name in line:
             print line
