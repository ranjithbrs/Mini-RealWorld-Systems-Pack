base_price=float(input("Enter the base price: "))
cust_type=str(input("Enter the customer type(regular, premium, new): ")).lower()
time_of_pur=str(input("Enter the time of purchase(morning, afternoon, night): ")).lower()
fest_seas=str(input("Enter the festival season(yes, no): ")).lower()
cust_rating=float(input("Enter the rating(<=5.0): "))
discount=0
if(cust_type=="premium"):
    #after 15 % disc
    discount+=15
    base_price=base_price-(0.15*base_price)
elif(cust_type=="new"):
    discount+=5
    base_price=base_price-(0.05*base_price)
if(time_of_pur=="night"):
    base_price=base_price+(0.1*base_price)
if(fest_seas=="yes"):
    base_price=base_price+(0.2*base_price)
if(0<=cust_rating<=5):
    if(cust_rating>=4.7):
        discount+=5
        base_price=base_price-(0.05*base_price)
        print(f"Final_price: ₹{base_price:.2f}")
else:
    print("Rating should be between 0 and 5")
if(discount>=15):
    print("Best deal for you")
else:
    print("Standard pricing applied")
    