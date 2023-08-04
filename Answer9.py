def factorial(n):
  
    fact = 1;
 
    for i in range(2,n+1):
        fact = fact * i;
 
    return fact;
  
 
# def to calculate p(n, r)
def npr(n, r):
  
    pnr = factorial(n) / factorial(n - r);
 
    return pnr;
  
 
# def to find the number of permutations of
# n different things taken r at a time
# with k things grouped together
def countPermutations(n, r, k):
  
    return int(factorial(k) * (r - k + 1) * npr(n - k, r - k));
  
 
# Driver code
n = 8;
r = 5;
k = 2;
 
print(countPermutations(n, r, k));
     
# this code is contributed by mits
 