from next_fit import next_fit
from first_fit import first_fit
from first_fit import first_fit_decreasing
from best_fit import best_fit
from best_fit import best_fit_decreasing
import random
import numpy as np
import matplotlib.pyplot as plt
import sys
from decimal import *

TRIALS = 150
algos = [next_fit, first_fit, first_fit_decreasing, best_fit, best_fit_decreasing]
files = ['data_nf.txt', 'data_ff.txt', 'data_ffd.txt', 'data_bf.txt', 'data_bfd.txt']
NAMES = ['NEXT FIT', 'FIRST FIT', 'FIRST FIT DECREASING', 'BEST FIT', 'BEST FIT DECREASING']
SIZES = [25000, 50000, 100000] # [10, 20, 40, 80, 160, 320, 625, 1250, 2500, 5000, 10000, 25000, 50000, 100000]
IGNORE_THRESHOLD = 3

def get_data():
    # Test each size 
    for n in SIZES:
        # Repeat trials 
        for _ in range(0, TRIALS):

            # generate list of random # 0.0-0.7 of size n
            items = np.random.uniform(0.0, 0.7, n)

            # test each algorithm on data
            for alg, file in zip(algos, files):
                with open(file, 'a') as f:
                    assignment=[0]*n
                    free_space=list()
                    alg(items, assignment=assignment, free_space=free_space)
                    waste = len(free_space) - sum(items)
                    f.write(f'{str(n)} {str(waste)}\n')

        print(f'Tests of size {str(n)} done ')

def graph_data():

    for file, alg_name in zip(files, NAMES):
        # Average data
        data = {} # stores {N: waste}
        with open(file, 'r') as f:
            for line in f:
                size, waste = line.split(" ")
                if int(size) not in data:
                    data[int(size)] = [] 
                data[int(size)].append(Decimal(waste))
        
        # average out data
        data = {n: (sum(waste)/len(waste)) for n, waste in data.items()}

        # graph k, v pairs as x, y pairs
        x = sorted(data)
        y = [float(data[k]) for k in data.keys()]

        x_adjusted = np.array(x[IGNORE_THRESHOLD:])
        y_adjusted = np.array(y[IGNORE_THRESHOLD:])

        logx, logy = np.log(x_adjusted), np.log(y_adjusted)
        # a, b = np.polyfit(logx, logy, deg=1)
        a, b, c = np.polyfit(logx, logy, deg=2)
        # fit = np.poly1d((a,b))
        fit = np.poly1d((a,b,c))
        y_expected = fit(logx)

        # Show plots
        plt.figure(figsize=(10,6))
        plt.loglog(x,y,'.',base=2)
        # plt.loglog(x_adjusted,np.exp(y_expected),'--',label=f'Approximate fit: log C(n) ~ {a:.5} log n + {b:.5} ')
        plt.loglog(x_adjusted,np.exp(y_expected),'--',label=f'Approximate fit: log C(n) ~ {a:.3} log^2 n + {b:.3} log n + {c: .3}')
        plt.title(f'{alg_name}: Alternate Fit')
        plt.xlabel('# items')
        plt.ylabel('Total waste')

        leg = plt.legend(loc='upper left')
        plt.show()

def graph_specific():

    data_m = {}
    for file, alg_name in zip(files, NAMES):
        # Average data
        data = {} # stores {N: waste}
        with open(file, 'r') as f:
            for line in f:
                size, waste = line.split(" ")
                if int(size) not in data:
                    data[int(size)] = [] 
                data[int(size)].append(Decimal(waste))
        
        # average out data
        data = {n: (sum(waste)/len(waste)) for n, waste in data.items()}

        data_m[alg_name] = data

    plt.figure(figsize=(10,6))
    plt.title(f'FF vs FFD vs BF')
    plt.xlabel('# items')
    plt.ylabel('Total waste')

    x1 = sorted(data_m['FIRST FIT'])
    y1 = [float(data_m['FIRST FIT'][k]) for k in data_m['FIRST FIT'].keys()]

    x_adj1 = np.array(x1[IGNORE_THRESHOLD:])
    y_adj1 = np.array(y1[IGNORE_THRESHOLD:])

    logx1, logy1 = np.log(x_adj1), np.log(y_adj1)
    a, b = np.polyfit(logx1, logy1, deg=1)
    fit1 = np.poly1d((a,b))
    y_exp1 = fit1(logx1)
    plt.loglog(x1,y1,'.',base=2)
    plt.loglog(x_adj1,np.exp(y_exp1),'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3} ')
    
    x2 = sorted(data_m['FIRST FIT DECREASING'])
    y2 = [float(data_m['FIRST FIT DECREASING'][k]) for k in data_m['FIRST FIT DECREASING'].keys()]

    x_adj2 = np.array(x2[IGNORE_THRESHOLD:])
    y_adj2 = np.array(y2[IGNORE_THRESHOLD:])

    logx2, logy2 = np.log(x_adj2), np.log(y_adj2)
    a, b, c = np.polyfit(logx2, logy2, deg=2)
    fit2 = np.poly1d((a,b,c))
    y_exp2 = fit2(logx2)
    plt.loglog(x2,y2,'.',base=2)
    plt.loglog(x_adj2,np.exp(y_exp2),'--',label=f'Approximate fit: log C(n) ~ {a:.3} log^2 n + {b:.3} log n + {c: .3}')

    x3 = sorted(data_m['BEST FIT'])
    y3 = [float(data_m['BEST FIT'][k]) for k in data_m['BEST FIT'].keys()]

    x_adj3 = np.array(x3[IGNORE_THRESHOLD:])
    y_adj3 = np.array(y3[IGNORE_THRESHOLD:])

    logx3, logy3 = np.log(x_adj3), np.log(y_adj3)
    a, b, c = np.polyfit(logx3, logy3, deg=2)
    fit3 = np.poly1d((a,b,c))
    y_exp3 = fit3(logx2)
    plt.loglog(x3,y3,'.',base=2)
    plt.loglog(x_adj3,np.exp(y_exp3),'--',label=f'Approximate fit: log C(n) ~ {a:.3} log^2 n + {b:.3} log n + {c: .3}')
    

    leg = plt.legend(loc='upper left')
    plt.show()
    

def difference():
    d1, d2 = ([], [])
    with open('data_bf.txt', 'r') as f1:
        for line in f1:
            d1.append(line)

    with open('data_bf.txt', 'r') as f2:
        for line in f2:
            d1.append(line)

    difference = 0
    for x, y in zip(d1, d2):
        if x != y: difference += 1

    print(f' {difference} differences found ')


if __name__ == '__main__':
    # get_data()
    # graph_data()
    graph_specific()
    # difference()

