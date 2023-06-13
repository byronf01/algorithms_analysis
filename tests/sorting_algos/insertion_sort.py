def insertion_sort(input):
    if len(input) <= 1: return input
    for i in range(1, len(input), 1):
        for j in range(i, 0, -1):
            if input[j] < input[j-1]:
                input[j-1], input[j] = (input[j], input[j-1])
            else:   break
    return input
