from graph import Graph
from graph_algorithms import get_diameter
from graph_algorithms import get_clustering_coefficient
from graph_algorithms import get_degree_distribution
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import ast
from decimal import Decimal
from scipy.optimize import curve_fit

# NOTE: do everything twice, once for Erdos-Renyi random graphs and once for Barbasi-Albert random graphs

# PART 1
TRIALS = 25 
SIZES = [10,25,50,100,200,400,800,1600,3200,6400,12800,25600,51200]
SIZES_DEGS = [1000, 10000, 100000]
IGNORE_THRESHOLD = 0

def diameter_and_cc_tests():
    for n in SIZES:
        for _ in range(TRIALS):
            G1 = generate_er(n)
            G2 = generate_ba(n)
            
            d1 = get_diameter(G1)
            d2 = get_diameter(G2)
            c1 = get_clustering_coefficient(G1)
            c2 = get_clustering_coefficient(G2)

            with open('diameter_erdos_renyi.txt', 'a') as f1:
                f1.write(f'{n} {d1}\n')

            with open('diameter_barabasi_albert.txt', 'a') as f2:
                f2.write(f'{n} {d2}\n')

            with open('cc_erdos_renyi.txt', 'a') as f3:
                f3.write(f'{n} {c1}\n')

            with open('cc_barabasi_albert.txt', 'a') as f4:
                f4.write(f'{n} {c2}\n')
        
        print(f'Tests of size {n} done ')

def plot_diameter():
    
    # ERODS-RENYI GRAPHS
    data = {}
    with open('diameter_erdos_renyi.txt', 'r') as f1:
        for line in f1:
            n, d = line.split(' ')
            n, d = (int(n), int(d))
            if n not in data:
                data[n] = []
            data[n].append(d)
    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}

    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b = np.polyfit(logx, y_adjusted, deg=1)
    
    fit = np.poly1d((a,b))
    y_expected = fit(logx)

    # Show plots
    plt.figure(figsize=(10,6))
    plt.semilogx(x,y,'.',base=2)
    plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3}')
    plt.title(f'# vertices vs Diameter (Erdos-Renyi)')
    plt.xlabel('# vertices')
    plt.ylabel('Diameter')
    leg = plt.legend(loc='upper left')
    plt.show()

    # BARABASI-ALBERT GRAPHS
    data = {}
    with open('diameter_barabasi_albert.txt', 'r') as f2:
        for line in f2:
            n, d = line.split(' ')
            n, d = (int(n), int(d))
            if n not in data:
                data[n] = []
            data[n].append(d)
    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}
    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b = np.polyfit(logx, y_adjusted, deg=1)
    
    fit = np.poly1d((a,b))
    y_expected = fit(logx)

    # Show plots
    plt.figure(figsize=(10,6))
    plt.semilogx(x,y,'.',base=2)
    # plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3}')
    plt.title(f'# vertices vs Diameter (Barabasi-Albert)')
    plt.xlabel('# vertices')
    plt.ylabel('Diameter')
    leg = plt.legend(loc='upper left')
    plt.show()
    

def plot_cc():

    # ERODS-RENYI GRAPHS
    data = {}
    with open('cc_erdos_renyi.txt', 'r') as f1:
        for line in f1:
            n, d = line.split(' ')
            n, d = (int(n), Decimal(d))
            if n not in data:
                data[n] = []
            data[n].append(d)

    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}

    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b = np.polyfit(logx, y_adjusted, deg=1)
    
    fit = np.poly1d((a,b))
    y_expected = fit(logx)

    # Show plots
    plt.figure(figsize=(10,6))
    plt.semilogx(x,y,'.',base=2)
    # plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3}')
    # plt.semilogx(np.exp(x_adjusted), y_expected, '--', label=f'Approximate fit: y = {params[0]:.3f} * exp(-{params[1]:.3f} * x)')
    plt.title(f'# vertices vs Clustering Coefficient (Erdos-Renyi)')
    plt.xlabel('# vertices')
    plt.ylabel('Clustering Coefficient')
    plt.show()

    # BARABASI-ALBERT GRAPHS
    data = {}
    with open('cc_barabasi_albert.txt', 'r') as f2:
        for line in f2:
            n, d = line.split(' ')
            n, d = (int(n), Decimal(d))
            if n not in data:
                data[n] = []
            data[n].append(d)
    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}
    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b = np.polyfit(logx, y_adjusted, deg=1)
    # a, b, c = np.polyfit(logx, y_adjusted, deg=2)
    
    fit = np.poly1d((a,b))
    # fit = np.poly1d((a, b, c))
    y_expected = fit(logx)

    # Show plots
    plt.figure(figsize=(10,6))
    plt.semilogx(x,y,'.',base=2)
    # plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3}')
    # plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log^2 n + {b:.3} log n + {c: .3}')
    plt.title(f'# vertices vs Clustering Coefficient (Barabasi-Albert)')
    plt.xlabel('# vertices')
    plt.ylabel('Clustering Coefficient')
    plt.show()

def generate_er(n: int) -> Graph:
    G = nx.erdos_renyi_graph(n, 2 * np.log(n) / n)
    return Graph(n, G.edges)

def generate_ba(n: int) -> Graph:
    G = nx.barabasi_albert_graph(n, 5)
    return Graph(n, G.edges)

# PART 2
# for n = 1000, n = 10000, n = 100000, plot degree distribution
# plot on lin-lin scale and log-log scale
# determine power law Y/N
# find exponent of power law if necessary
CUTOFF_THRESHOLD = 0.7

# P.S. explain implementation of algorithms

def degree_distribution_tests():
    for n in SIZES_DEGS:
        G1 = generate_er(n)
        G2 = generate_ba(n)
        dd1 = get_degree_distribution(G1)
        dd2 = get_degree_distribution(G2)

        with open('degree_dist1.txt', 'a') as f:
            f.write(f'{n} {dd1}\n')
        
        with open('degree_dist2.txt', 'a') as f:
            f.write(f'{n} {dd2}\n')


def plot_degree_distribution():

    for n in SIZES_DEGS:
       
        dd1 = {}
        dd2 = {}

        with open('degree_dist1.txt', 'r') as f1:
            for line in f1:
                k, deg = line.split(' ', 1)
                if n == int(k):
                    dd1 = ast.literal_eval(deg)

        with open('degree_dist2.txt', 'r') as f1:
            for line in f1:
                k, deg = line.split(' ', 1)
                if n == int(k):
                    dd2 = ast.literal_eval(deg)

        # ERDOS-RENYI
        x = sorted(dd1)
        y = [dd1[k] for k in x]
        plt.figure(figsize=(10,6))
        plt.plot(x, y, '.')
        plt.title(f'Degree Distribution lin-lin, n={n} (Erdos-Renyi)')
        plt.xlabel('Degree')
        plt.ylabel('number of vertices with degree')
        plt.show()

        logx = np.log(x)
        logy = np.log(y)

        plt.figure(figsize=(10,6))
        plt.loglog(x,y,'.',base=2)
        # plt.loglog(x_adjusted,np.exp(y_expected),'--',label=f'Approximate fit: log C(n) ~ {a:.3} log n + {b:.3}')
        plt.title(f'Degree Distribution log-log, n={n} (Erdos-Renyi)')
        plt.xlabel('Degree')
        plt.ylabel('number of vertices with degree')
        plt.show()

        # BARABASI-ALBERT
        x = sorted(dd2)
        y = [dd2[k] for k in x]
        plt.figure(figsize=(10,6))
        plt.plot(x, y, '.')
        plt.title(f'Degree Distribution lin-lin, n={n} (Barabasi-Albert)')
        plt.xlabel('Degree')
        plt.ylabel('number of vertices with degree')
        plt.show()

        # plot both on log-log (to test power)
        x_adj = x[:int(len(x)*CUTOFF_THRESHOLD)]
        # x_adj = x
        y_adj = [dd2[k] for k in x_adj]
        # logx = np.log(x)
        # logy = np.log(y)
        logx = np.log(x_adj)
        logy = np.log(y_adj)
        a, b = np.polyfit(logx, logy, deg=1)
        fit = np.poly1d((a,b))
        y_expected = fit(logx)

        # Show plots
        plt.figure(figsize=(10,6))
        plt.loglog(x,y,'.',base=2)
        plt.loglog(np.exp(logx),np.exp(y_expected),'--',label=f'Power law: {a:.3} * n + {b:.3}')
        plt.title(f'Degree Distribution log-log, n={n} (Barabasi-Albert)')
        plt.xlabel('Degree')
        plt.ylabel('number of vertices with degree')
        leg = plt.legend(loc='upper left')
        plt.show()

def plot_custom():

    # ERODS-RENYI GRAPHS
    data = {}
    with open('cc_erdos_renyi.txt', 'r') as f1:
        for line in f1:
            n, d = line.split(' ')
            n, d = (int(n), Decimal(d))
            if n not in data:
                data[n] = []
            data[n].append(d)

    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}

    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b, c, d, e = np.polyfit(logx, y_adjusted, deg=4)
    
    fit = np.poly1d((a,b,c,d,e))
    y_expected = fit(logx)

    # Show plots
    plt.figure(figsize=(10,6))
    plt.semilogx(x,y,'.',base=2,label='Barabasi-Albert')
    plt.semilogx(x_adjusted,y_expected,'--',label=f'Erdos-Renyi approximate fit')
    # plt.semilogx(np.exp(x_adjusted), y_expected, '--', label=f'Approximate fit: y = {params[0]:.3f} * exp(-{params[1]:.3f} * x)')
    

    # BARABASI-ALBERT GRAPHS
    data = {}
    with open('cc_barabasi_albert.txt', 'r') as f2:
        for line in f2:
            n, d = line.split(' ')
            n, d = (int(n), Decimal(d))
            if n not in data:
                data[n] = []
            data[n].append(d)
    # average out data
    data = {n: sum(d) / len(d) for n, d in data.items()}
    # plot data
    x = sorted(data)
    y = [float(data[k]) for k in x]

    x_adjusted = np.array(x[IGNORE_THRESHOLD:])
    y_adjusted = np.array(y[IGNORE_THRESHOLD:])

    logx = np.log(x_adjusted)
    a, b = np.polyfit(logx, y_adjusted, deg=1)
    a, b, c, d, e = np.polyfit(logx, y_adjusted, deg=4)
    
    fit = np.poly1d((a,b,c,d,e))
    # fit = np.poly1d((a, b, c))
    y_expected = fit(logx)

    # Show plots
    plt.semilogx(x,y,'.',base=2,label='Barabasi-Albert')
    plt.semilogx(x_adjusted,y_expected,'--',label=f'Barabasi-Albert approximate fit')
    # plt.semilogx(x_adjusted,y_expected,'--',label=f'Approximate fit: log C(n) ~ {a:.3} log^2 n + {b:.3} log n + {c: .3}')
    plt.title(f'Clustering Coefficient Erdos-Renyi vs. Barabasi-Albert')
    plt.xlabel('# vertices')
    plt.ylabel('Clustering Coefficient')
    leg = plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    # diameter_and_cc_tests()
    # plot_diameter()
    # plot_cc()
    # degree_distribution_tests()
    # plot_degree_distribution()
    plot_custom()
            