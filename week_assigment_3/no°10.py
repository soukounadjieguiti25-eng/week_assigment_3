# Average Speed Calculation
distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hours): "))

speed = distance / time

print("Average speed:", speed, "km/h")

if speed > 80:
    print("High speed")