# Danielson April, 2022
# Implement the MEMOIZED-CUT-ROD algorithm
# View a terminal window
# python3 

import math

# top-down memoized rod cutting
def MEMOIZED_CUT_ROD(p,n):
    r = []
    for i in range(0,n+1):
        r.append(-math.inf)
    return MEMOIZED_CUT_ROD_AUX(p, n, r)

# memoized rod cutting helper function
def MEMOIZED_CUT_ROD_AUX(p,n, r):
    if r[n] >= 0: # desired value already known
        return r[n]
    if n == 0: #desired value not known
        q = 0
    else:
        q = -math.inf
        for i in range(1,n+1):
            q = max(q, p[i] + MEMOIZED_CUT_ROD_AUX(p, n-i, r))
    r[n] = q #store the new value
    return q

def main():
    #p = [0, 1,5,8,9,10,17,17,20]
    #p = [-math.inf, 1,5,8,9,10,17,17,20,20, 25, 26, 26, 26, 28, 30, 30, 30, 42, 42, 45, 46, 47]
    p = [-math.inf, 1,5,8,9,10,17,17,20,20, 25, 26, 26, 26, 28, 30, 30, 30, 42, 42, 45, 46, 47, 50, 50, 55, 56, 57, 58, 60, 65]
    print("Maximum length =", len(p))
    for l in range(1,len(p)):
        #counter = 0
        max_revenue = MEMOIZED_CUT_ROD(p, l)
        print("length =", l, ": r = ", max_revenue)
    
main() 