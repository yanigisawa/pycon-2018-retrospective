# The inventory file lists a series of parts, prices and quantities. The price change file lists the same series of parts with changes in price.
#
# Calculate the current value of the inventory, taking the price * the quantity for each part and summing the value for all the parts.
#
# Calculate the change in value of the inventory by calculating the new price for each part based on the price change (positive or negative) and multiplying by the quantity of parts and summing across all the parts.
#
# For example, given the following lists:
#
# nut    0.05 100
# washer 0.03  10
# ---------------
#     total: 5.30
# nut    +0.01 ---> +1.00
# washer -0.01 ---> -0.10
# ---------------
# new_total: 6.20
# Yields a final price of $6.20
# For your answer, you would enter 6.20

parts = {}
total_inv = 0
with open('inventory.txt') as f:
    for line in f:
        l = line.split()
        cost = float(l[1]) * int(l[2])
        total_inv += cost
        parts[l[0]] = {'cost': float(l[1]), 'quantity': int(l[2]), 'total': cost }
    print(total_inv)

delta_sum = 0
with open('price_change.txt') as f:
    for line in f:
        item, change = line.split(',')
        change = float(change.replace('+', ''))
        i = parts[item]
        delta = i['quantity'] * change
        delta_sum += delta
        total_inv += delta
        print(f'Total: {total_inv} Item: {item} quantity: {i["quantity"]} change: {change} delta: {delta}')

    print(f'Total after price change: {total_inv}')

