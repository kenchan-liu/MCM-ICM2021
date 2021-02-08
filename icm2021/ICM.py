import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
data=pd.read_csv("influence_data.csv",header=None)
import networkx as nx
import numpy as np
data2=data.drop([0])
dict1={}
G2 = nx.DiGraph()
for i,r in data2.iterrows():
    G2.add_node(r[0])
    G2.add_node(r[4])
    G2.add_edge(r[0],r[4],weight=0.01)
for i in G2.nodes():
    a=0.0
    for j in G2.nodes():
        if(i!=j and nx.has_path(G2,i,j)):
            a+=1/nx.shortest_path_length(G2, source=i, target=j)**2
    dict1[i]=a
dict1=sorted(dict1.items(),key = lambda kv:(kv[1]),reverse=True)
print(dict1)

G=nx.DiGraph()
G.add_edges_from([('A','B'),('B','C'),('A','D'),('D','E'),('E','C')])
nx.draw(G,pos=nx.spring_layout(G),node_color='steelblue',edge_color='black',with_labels=True,node_size=2000,arrowsize=20)
plt.show()

data=pd.read_csv("influence.csv")
idata=data['influencer_active_start']
fdata=data['follower_active_start']
sns.distplot(idata,bins=20,kde=False,hist_kws={'color':'steelblue'},label='influencer')
sns.distplot(fdata,bins=20,kde=False,hist_kws={'color':'purple'},label='follower')
plt.title("active_start_time_distribution")
plt.legend()
plt.show()
