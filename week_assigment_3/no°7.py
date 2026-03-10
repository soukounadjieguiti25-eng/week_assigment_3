# no°7 Parking Fee Calculation
hours = int(input("Enter parking hours: "))

if hours <= 2:
    fee = 5000
else:
    fee = 5000 + (hours - 2) * 3000

print("Total parking fee: Rp", fee)