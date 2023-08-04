def factorial(n):
  
    fact = 1;
 
    for i in range(2,n+1):
        fact = fact * i;
 
    return fact;
  
 

def npr(n, r):
  
    pnr = factorial(n) / factorial(n - r);
 
    return pnr;
  
 

def countPermutations(n, r, k):
  
    return int(factorial(k) * (r - k + 1) * npr(n - k, r - k));
  
 

n = 8;
r = 5;
k = 2;
 
print(countPermutations(n, r, k));
     

 
