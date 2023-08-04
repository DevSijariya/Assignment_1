# Python3 implementation of the above approach
 
# Function to find number of cards needed
def noOfCards(n):
    return n * (3 * n + 1) // 2
 
# Driver Code
n = 3
print(noOfCards(n))
 
# This code is contributed by mohit kumar 29