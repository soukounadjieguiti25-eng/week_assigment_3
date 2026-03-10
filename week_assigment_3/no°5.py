# no°5 Rectangle Area and Perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

if area > 100:
    print("Large area")