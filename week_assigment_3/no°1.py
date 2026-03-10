# no°1 Shopping Discount
total_purchase = float(input("Enter total purchase amount: "))

if total_purchase >= 500000:
    discount = total_purchase * 0.20
elif total_purchase >= 250000:
    discount = total_purchase * 0.10
else:
    discount = 0

final_amount = total_purchase - discount

print("Discount:", discount)
print("Final amount to pay:", final_amount)