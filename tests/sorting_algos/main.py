import random, time, copy
from math import log
import matplotlib.pyplot as plt
import numpy as np
# Import each one of your sorting algorithms below as follows:
# Feel free to comment out these lines before your algorithms are implemented.
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort import shell_sort1, shell_sort2, shell_sort3, shell_sort4
from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3

SIZES = [100,200,400,800,1600,3200,6400,12800,25600,51200]
# SIZES = [8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
FUNCTIONS = [insertion_sort, merge_sort, shell_sort1, shell_sort2,
             shell_sort3, hybrid_sort1, hybrid_sort2, hybrid_sort3, shell_sort4]
FUNCTIONS_STR = ["INSERTION SORT", "MERGE SORT", "SHELL SORT 1", "SHELL SORT 2",
             "SHELL SORT 3", "HYBRID SORT 1", "HYBRID SORT 2", "HYBRID SORT 3", 'SHELL SORT 4']
IGNORE_THRESHOLD = 4
TRIALS = 10

def generateLists():
    # Generate uniformly dist.
    uniform = []
    u = []
    for i in range(0, SIZES[-1]+1):
        u.append(i)
    uniform.append(u)
    for i in range(len(SIZES)-2, -1, -1):
        s = SIZES[i]
        uniform.insert(0, copy.deepcopy(u[:(s+1)]))
    for p in uniform:
        for i in range(len(p)-1,0,-1):
            j = random.randint(0, i)
            p[i], p[j] = (p[j], p[i])

    # generate almost sorted dist
    almost = []
    al = []
    for i in range(0, 50001):
        al.append(i)
    almost.append(al)
    for i in range(len(SIZES)-2, -1, -1):
        s = SIZES[i]
        almost.insert(0, copy.deepcopy(al[:(s+1)]))
    for a in almost:
        n = log(len(a), 2)
        already_swapped = set()
        for pair in range(0, int(n)):
            s1 = random.randint(0, len(a)-1)
            s2 = random.randint(0, len(a)-1)
            while s1 == s2 or s1 in already_swapped or s2 in already_swapped:
                s1 = random.randint(0, len(a)-1)
                s2 = random.randint(0, len(a)-1)
            already_swapped.add(s1)
            already_swapped.add(s2)
            a[s1], a[s2] = (a[s2], a[s1])
    
    # generate resverse sorted
    reverse = []
    r = []
    for i in range(50000, -1, -1):
        r.append(i)
    reverse.append(r)
    for i in range(len(SIZES)-2, -1, -1):
        s = SIZES[i]
        reverse.insert(0, copy.deepcopy(r[-(s+1):]))

    return (uniform, almost, reverse)

def plot_individual():
    
    with open('results.txt', 'r') as f:
        contents = f.read()
    contents = contents.split('\n')
    contents = [c.split(" ") for c in contents]
    for ct in range(0, len(FUNCTIONS)):
        # Initially, plot all x and y data points 
        title = "".join(contents[4*ct])
        x = SIZES
        y = [float(t) for t in contents[4*ct+1] if t != '']
        plt.loglog(x, y, base=2, marker='o', label='data')
        plt.title(f'{title}: Uniform Permutations ')
        plt.xlabel('Array Size')
        plt.ylabel('Time')
        
        # Ignore starting data points
        x_adj = np.array(x[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect))
        
        plt.show()

        y = [float(t) for t in contents[4*ct+2] if t != '']
        plt.loglog(x, y, base=2, marker='o', label='data')
        plt.title(f'{title}: Almost Sorted ')
        plt.xlabel('Array Size')
        plt.ylabel('Time')
        
        # Ignore starting data points
        x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect))
        plt.show()

        y = [float(t) for t in contents[4*ct+3] if t != '']
        plt.loglog(x, y, base=2, marker='o', label='data')
        plt.title(f'{title}: Reverse Order ')
        plt.xlabel('Array Size')
        plt.ylabel('Time')
        
        # Ignore starting data points
        x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect))
        plt.show()

def plot_grouped():
    
    with open('results.txt', 'r') as f:
        contents = f.read()
    contents = contents.split('\n')
    contents = [c.split(" ") for c in contents]
    for ct in range(0, len(FUNCTIONS)):
        # Initially, plot all x and y data points 
        title = "".join(contents[4*ct])
        x = SIZES
        y = [float(t) for t in contents[4*ct+1] if t != '']
        plt.figure(figsize=(10,6))
        plt.loglog(x, y, '.', base=2, label='Uniform Permutations ')
        plt.title(f'{title}')
        plt.xlabel('Array Size')
        plt.ylabel('Time')
        
        # Ignore starting data points
        x_adj = np.array(x[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect), '--', label=f'Uniform : log C(n) ~ {a: .5} log n + {b: .5} ')
        

        y = [float(t) for t in contents[4*ct+2] if t != '']
        plt.loglog(x, y, '.', base=2, label='Almost Sorted')
        
        # Ignore starting data points
        x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect), '--', label=f'Almost : log C(n) ~ {a: .5} log n + {b: .5} ')

        y = [float(t) for t in contents[4*ct+3] if t != '']
        plt.loglog(x, y, '.', base=2, label='Reverse Order')
        
        # Ignore starting data points
        x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
        y_adj = np.array(y[IGNORE_THRESHOLD:])

        # Fit curve to data
        logx, logy = np.log(x_adj), np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a, b))
        y_expect = fit(logx)
        plt.loglog(x_adj, np.exp(y_expect), '--', label=f'Reverse : log C(n) ~ {a: .5} log n + {b: .5} ')

        leg = plt.legend(loc='upper left')
        plt.show()

def plot_custom():
    with open('custom.txt', 'r') as f:
        contents = f.read()
    contents = contents.split('\n')
    contents = [c.split(" ") for c in contents]
    
    # Initially, plot all x and y data points 
    title = "SHELL UNIFORM VS ALMOST"
    x = SIZES
    y = [float(t) for t in contents[1] if t != '']
    plt.figure(figsize=(10,6))
    plt.loglog(x, y, '.', base=2)
    plt.title(f'{title}')
    plt.xlabel('Array Size')
    plt.ylabel('Time')
    
    # Ignore starting data points
    x_adj = np.array(x[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S1 Uniform : log C(n) ~ {a: .5} log n + {b: .5} ')

    y = [float(t) for t in contents[4] if t != '']
    plt.loglog(x, y, '.', base=2)
    
    # Ignore starting data points
    x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S2 Uniform : log C(n) ~ {a: .5} log n + {b: .5} ')
    y = [float(t) for t in contents[7] if t != '']
    plt.loglog(x, y, '.', base=2)
    
    # Ignore starting data points
    x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S4 Uniform : log C(n) ~ {a: .5} log n + {b: .5} ')

    y = [float(t) for t in contents[2] if t != '']
    plt.loglog(x, y, '.', base=2)
    
    # Ignore starting data points
    x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S1 Almost : log C(n) ~ {a: .5} log n + {b: .5} ')
    y = [float(t) for t in contents[5] if t != '']
    plt.loglog(x, y, '.', base=2)
    
    # Ignore starting data points
    x_adj = np.array(x[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S2 Almost : log C(n) ~ {a: .5} log n + {b: .5} ')

    y = [float(t) for t in contents[8] if t != '']
    plt.loglog(x, y, '.', base=2)
    
    # Ignore starting data points
    x_adj = np.array(SIZES[IGNORE_THRESHOLD:])
    y_adj = np.array(y[IGNORE_THRESHOLD:])

    # Fit curve to data
    logx, logy = np.log(x_adj), np.log(y_adj)
    a, b = np.polyfit(logx, logy, deg=1)
    fit = np.poly1d((a, b))
    y_expect = fit(logx)
    plt.loglog(x_adj, np.exp(y_expect), '--', label=f'S4 Almost : log C(n) ~ {a: .5} log n + {b: .5} ')

    leg = plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':

    """
    ct = 0
    for func in FUNCTIONS:

        times_uniform = [0]*len(SIZES)
        times_almost = [0]*len(SIZES)
        times_reverse = [0]*len(SIZES)

        for i in range(TRIALS):
        
            uniform, almost, reverse = generateLists()

            # Testing
            for l in range(0, len(uniform)):
                start = time.time()
                func(uniform[l])
                end = time.time()
                times_uniform[l] += (end-start)
            for l in range(0, len(almost)):
                start = time.time()
                func(almost[l])
                end = time.time()
                times_almost[l] += (end-start)
            for l in range(0, len(reverse)):
                start = time.time()
                func(reverse[l])
                end = time.time()
                times_reverse[l] += (end-start)

        times_uniform = [t/TRIALS for t in times_uniform]
        times_almost = [t/TRIALS for t in times_almost]
        times_reverse = [t/TRIALS for t in times_reverse]

        with open('results.txt', 'a') as f:
            f.write(f'{FUNCTIONS_STR[ct]}')
            f.write('\n')
            for t in times_uniform:
                f.write(str(t) + ' ')
            f.write('\n')
            for t in times_almost:
                f.write(str(t) + ' ')
            f.write('\n')
            for t in times_reverse:
                f.write(str(t) + ' ')
            f.write('\n')

        ct += 1
    """
    
    plot_custom()