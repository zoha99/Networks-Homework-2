#importing the networkx library
from audioop import avg
import networkx as nx
#importing the matplotlib library for plotting the graph
import matplotlib.pyplot as plt

import numpy as np

G1 = nx.erdos_renyi_graph(3*(10^6),0.25)
G2 = nx.erdos_renyi_graph(10*(10^3),0.1)
G3 = nx.erdos_renyi_graph(6*(10^6),0.08)

def drawG(G):
    nx.draw(G, with_labels=True)
    plt.show()

#part i
def avg_deg(G):
    return nx.average_degree_connectivity(G)

#part ii
def avg_clus(G):
    return nx.average_clustering(G)

#part iii
def apl(G):
    return nx.average_shortest_path_length(G)
# print(avg_clus(G1))
# print(avg_clus(G2))
# print(avg_clus(G3))


#Degree distribution (part iv)
def plot_degree_dist(G):
    degree_freq = np.array(nx.degree_histogram(G)).astype('float')
    plt.figure(figsize=(12, 8))
    plt.stem(degree_freq)
    plt.ylabel("Frequence")
    plt.xlabel("Degree")
    plt.show()

#plot_degree_dist(G1) 


#For Histograms
#APL
def hist(): 
    apls=[]
    for i in range(30):
        #G = nx.erdos_renyi_graph(3*(10^6),0.25)
        #G = nx.erdos_renyi_graph(10*(10^3),0.1)
        G = nx.erdos_renyi_graph(6*(10^6),0.08)
        apls.append(nx.average_shortest_path_length(G))
    print(apls)
    plt.hist(apls)
    plt.title("Frequency diagram")
    plt.xlabel("Avg Path Length")
    plt.ylabel("Frequency")
    plt.show()
    
#Avg Clustering
def hist2():
    cc=[]
    for i in range(30):
        #G = nx.erdos_renyi_graph(3*(10^6),0.25)
        #G = nx.erdos_renyi_graph(10*(10^3),0.1)
        G = nx.erdos_renyi_graph(6*(10^6),0.08)
        cc.append(nx.average_clustering(G))
    plt.hist(cc)
    plt.title("Frequency diagram")
    plt.xlabel("Avg Clustering")
    plt.ylabel("Frequency")
    plt.show()

#Avg Degree
def hist3():
    deg=[]
    for i in range(30):
        #G = nx.erdos_renyi_graph(3*(10^6),0.25)
        #G = nx.erdos_renyi_graph(10*(10^3),0.1)
        G = nx.erdos_renyi_graph(6*(10^6),0.08)
        deg.append(np.mean([i[1] for i in G.degree()]))
    print(deg)
    plt.hist(deg)
    plt.title("Frequency diagram")
    plt.xlabel("Avg Degree")
    plt.ylabel("Frequency")
    plt.show()

#hist()
hist2()
#hist3()
#plot_degree_dist(G3)
#degree_dist(G1)