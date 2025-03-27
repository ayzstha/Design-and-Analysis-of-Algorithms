# Danielson April, 2022
# Implement the BOTTOM-UP-CUT-ROD algorithm

import math

# bottom-up rod cutting
def BOTTOM_UP_CUT_ROD(p,n):
    r = [] #let r be a new empty array
    r.append(0) #a rod of length 0 earns no revenue
    for j in range(1,n+1): #solve each subproblem of size j in order of increasing size
        q = -math.inf
        for i in range(1,j+1):
            q = max(q, p[i] + r[j-i]) #directly references r[j-i]
        r.append(q)                          #instead of recursive call
    return r

def main():
    #p = [0, 1,5,8,9,10,17,17,20]
    #p = [-math.inf, 1,5,8,9,10,17,17,20,20, 25, 26, 26, 26, 28, 30, 30, 30, 42, 42, 45, 46, 47]
    p = [-math.inf, 1,5,8,9,10,17,17,20,20, 25, 26, 26, 26, 28, 30, 30, 30, 42, 42, 45, 46, 47, 50, 50, 55, 56, 57, 58, 60, 65]
    #print("Maximum length =", len(p))
    revenues = BOTTOM_UP_CUT_ROD(p,len(p)-1)
    print("l r")
    for i in range(len(p)):
        print(i, revenues[i])
    
main() 