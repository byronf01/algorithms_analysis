import copy

def merge_sort(input):
    temp = copy.deepcopy(input)
    answer = helper(temp)
    for i in range(0, len(input)):
        input[i] = answer[i]
    return input

def helper(input):
    if input == []:
        return []
    if len(input) == 1:
        return input
    else:
        med = int(len(input) / 2)
        l = helper(input[0:med])
        r = helper(input[med:])
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
    """
    left_2 = mid+1
    if input[mid] < input[left_2]: return # already sorted
    while left <= mid and left_2 <= right:
        if input[left] <= input[left_2]:
            left += 1
        else
    """