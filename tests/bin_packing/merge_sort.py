import copy

def merge_sort(input, reverse=False):
    temp = copy.deepcopy(input)
    answer = helper(temp, reverse)
    for i in range(0, len(input)):
        input[i] = answer[i]
    return input

def helper(input, reverse):
    if input == []:
        return []
    if len(input) == 1:
        return input
    else:
        med = int(len(input) / 2)
        l = helper(input[0:med], reverse)
        r = helper(input[med:], reverse)
        tmp = []
        a, b = (0, 0)
        while a < len(l) and b < len(r):
            if reverse:
                if l[a] > r[b]:
                    tmp.append(l[a])
                    a += 1
                else: 
                    tmp.append(r[b])
                    b += 1
            else:
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