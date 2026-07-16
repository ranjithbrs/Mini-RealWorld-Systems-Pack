total_days=22
present_days=int(input("Enter the present days: "))
percentage=(present_days/total_days)*100
if(percentage>=75):
    print("Your attendance is acceptable")
else:
    print("Warning, Your attendance is below 75 %")