price=int(input("Enter the price: "))
print("Demand levels: High, Medium, Low")
demand=str(input("Enter the demand level: "))
if(demand=="High" or demand=="high"):
    print("Membership levels: Normal, Premium")
    membership=str(input("Enter the membership: "))
    if(membership=="Normal" or membership=="normal"):  
        surge_fee=0.2 * price
        price+=surge_fee
    print("Final price: ", price)
else:
    print("Final price: ",price)
    