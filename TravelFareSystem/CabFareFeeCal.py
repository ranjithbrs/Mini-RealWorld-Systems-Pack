distance=float(input("Enter the distance in km: "))
time=str(input("Enter the time of day(Peek, Non-peek): ")).strip().lower()
rating=float(input("Enter the rating (for out of 5): "))
#Base price calculation
price= 50 + 10 * distance
if(time=="peek"):
    extra=0.25 * price
    price += extra
elif(time=="non-peek"):
    pass
else:
    print("Invalid time of day")
if(0<=rating<=5):
    if(rating>4.5):
        disc=0.1 *price
        price -=disc
else:
    print("rating should be between 0 and 5")
print(f"Final price: ₹{price:.2f}")

