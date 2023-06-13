from math import log

def shell_sort1(input):
    n = len(input)
    if n == 0 or n == 1:
        return input
    gaps = []
    ct = 1
    while n // (2**ct) > 0:
        gaps.append(n // (2**ct))
        ct += 1
    return shell_sort_master(input, gaps, n)

def shell_sort2(input):
    n = len(input)
    if n == 0 or n == 1:
        return input
    gaps = []
    for i in range(int(log(n, 2)), -1, -1):
        if i == 1: gaps.append(1)
        else: gaps.append(2**i+1)
    return shell_sort_master(input, gaps, n)

def shell_sort3(input):
    n = len(input)
    if n == 0 or n == 1:
        return input
    gaps = set()
    p, q = (0, 0)
    while 2**p < n:
        while 2**p * 3**q < n:
            gaps.add(2**p * 3**q)
            q += 1
        q = 0
        p += 1
    
    gaps = list(gaps)
    gaps.reverse()
    return shell_sort_master(input, gaps, n)

def shell_sort4(input):
    n = len(input)
    if n == 0 or n == 1:
        return input
    gaps = []
    even = lambda x : 9 * (2**x) - 9 * (2 ** (x/2)) + 1
    odd = lambda x: 8 * (2**x) - 6 * (2 ** ((x+1)/2)) + 1
    x = 0
    value = even(0)
    while value < n: 
        gaps.insert(0, int(value))
        x += 1
        if x % 2 == 0: value = even(x)
        else: value = odd(x)
    return shell_sort_master(input, gaps, n)

def shell_sort_master(input, seq, n):

    for g in seq:
        for i in range(g, n, 1):
            starting = input[i]
            j = i
            while j >= g and input[j - g] > starting:
                input[j] = input[j - g]
                j -= g
            input[j] = starting
    
    return input


    
        