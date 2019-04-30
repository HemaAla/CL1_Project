# Python3 program to find minimum numbers of  
# tours required 

from math import

def getMin(N, A, k): 
  
    # Iterating through each possible  
    # value of minimum Items 
    for i in range(1, max(A)+1): 
        tours = 0
        # i = float(i)
        for j in range(0, len(A)): 
            tours += ceil(A[j]/float(i));
            # if(A[j]% i == 0):# Perfectly Divisible 
            #     tours += A[j]/i 
  
            # else: 
            #     # Not Perfectly Divisible means required 
            #     # tours are Floor Division + 1 
            #     tours += A[j]//i + 1 
  
        if(tours <= k): 
            # Return First Feasible Value found, 
            # since it is also the minimum 
            return i  
    return "Not Possible"
  
# Driver Code 
N = 10
A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
k = 50
print(getMin(N, A, k)) 