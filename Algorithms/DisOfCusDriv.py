print("customer location:")
customer_location = input("Enter customer location (x y): ")
a, b = map(float, customer_location.split())
#driver details
print("Driver details: ")
n=int(input("Enter the available number of drivers: "))
drivers = []
for i in range(n):
    r, s = map(float, input("Enter driver location (x y): ").split())
    drivers.append((r, s))
#distance calculation
dis=[]
for i in drivers:
    # dist=distance formula
    dist = ((a - i[0]) ** 2 + (b - i[1]) ** 2) ** 0.5
    dis.append(dist)
#find the closest driver
min_index = dis.index(min(dis))

"""
These statements are for print the index and drivernumber
print(f"The closest driver is at index {min_index}")
print(f"The closest driver is Driver {min_index + 1}")
"""
print(f"The closest driver is Driver {min_index + 1} with distance {dis[min_index]:.2f}")