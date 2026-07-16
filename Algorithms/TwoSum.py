arr=[1,2,3,4,5,6,7,8,9]
ans=[]
tar=13
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == tar:
            ans.append((arr[i], arr[j])) 
print(ans)
""" 
Algorithm:
s1: Intialize the list, target value and one empty list for stores the data.
s2: Using two for loops for linearly get the values using i and j indeces.
s3: Using if loop to check the added value of two values to target to find the values.
S4: Using append method to add the data to empty list for storing data.
S5: finally print the result in out of all foops.

Complexity:
time complexity is O(n*n) bcz of 2 loops.
space complexity is O(K) bcz of the number of valid pairs stored.
"""         