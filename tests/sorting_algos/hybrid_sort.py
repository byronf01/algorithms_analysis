from math import ceil
import copy

def hybrid_sort1(input):
    if len(input) == 0 or len(input) == 1:
        return input
    n = len(input) ** (1/2)
    temp = copy.deepcopy(input)
    answer = hybrid_sort_master(temp, ceil(n))
    for i in range(0, len(input)):
        input[i] = answer[i]
    return input

def hybrid_sort2(input):
    if len(input) == 0 or len(input) == 1:
        return input
    n = len(input) ** (1/4)
    temp = copy.deepcopy(input)
    answer = hybrid_sort_master(temp, ceil(n))
    for i in range(0, len(input)):
        input[i] = answer[i]
    return input

def hybrid_sort3(input):
    if len(input) == 0 or len(input) == 1:
        return input
    n = len(input) ** (1/6)
    temp = copy.deepcopy(input)
    answer = hybrid_sort_master(temp, ceil(n))
    for i in range(0, len(input)):
        input[i] = answer[i]
    return input

def hybrid_sort_master(input, threshold):
    if len(input) < threshold:
        for i in range(1, len(input), 1):
            for j in range(i, 0, -1):
                if input[j] < input[j-1]:
                    input[j-1], input[j] = (input[j], input[j-1])
                else:   break
        return input
    else:
        med = int(len(input) / 2)
        l = hybrid_sort_master(input[:med], threshold)
        r = hybrid_sort_master(input[med:], threshold)
        tmp = []
        a, b = (0, 0)
        while a < len(l) and b < len(r):
            if l[a] < r[b]:
                tmp.append(l[a])
                a += 1
            else: 
                tmp.append(r[b])
                b += 1
        while a < len(l):
            tmp.append(l[a])
            a += 1
        while b < len(r):
            tmp.append(r[b])
            b += 1
        return tmp 