#!/usr/bin/python3
""" write a method that calculates thefewest number
of operations needed to result in exactly n H characters in the file."""

def minOperations(n):
    if n < 2:
        return 0
    
    pr = 0
    
    while n % 2 == 0:
        pr += 2
        n //= 2
    
    dv = 3
    while dv * dv <= n:
        while n % dv == 0:
            pr += dv
            n //= dv
        dv += 2
        
    if n > 1:
        pr += n
    
    return pr
