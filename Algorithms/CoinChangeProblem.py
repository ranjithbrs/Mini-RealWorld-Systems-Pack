coins=[10,20,50,100]
changes=[]
amount=750
count=0
coins.sort(reverse=True)
for coin in coins:
    while amount >= coin:
        changes.append(coin)
        amount -= coin
        count+=1
if (amount == 0):
    print(changes)
    print(count)
else:
    print("Not possible to change the amount into coins")

    """
    Algorithm:
    s1: Initialize the list of coins, an empty list for store the used coins, and amount for coin changing, and count as 0.
    s2: Using sort method to sort the list of coins in descending order for reducing the number of count.
    s3: Using for loop for taking coins from list and while loop for changing the amount is greater than or equals to coin always for stopping the loop.
    s4: Using append method to add the used coins to an empty list for data storing.
    s5: everytime reduces the amount after using coins to change, and increase count by 1.
    S6: finally amoount becomes zero then print the result else print an msg for not possible to change.
    
    """