# Question 1:
# Write a program that takes as input an array of positive and negative numbers (0 excluded). The objective is to
# return those items from the array whose sum is 0. If no such items exist return “No Elements found”
# Example: For an input array [-4, 1, 3, -2, -1],
# one of the possible results would be 3, -2, -1 since their sum is 0.
# Note: If there are more than 1 combination of such items, you can return any 1 of them.

lis =  [-42, 1, 3, -2, -1] 
for i in range(len(lis)):
    temp = lis[i:i+3]
    if sum(temp) == 0:
        print(temp)
        break
