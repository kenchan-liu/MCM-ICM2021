import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
data=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\influence_data.csv",header=None)
# years=data.iloc[:,4]
# a=data.iloc[:,2].value_counts()
# genre=['Pop/Rock','R&B','Country','Jazz','Vocal','Blues','Folk','Reggae','Electronic','Latin','','',''
#       ,'','','','','','','','']
# plt.pie(a,labels=genre)
# plt.show()
import networkx as nx
# G = nx.DiGraph()
# Genre={'Pop/Rock':1,'R&B;':2,'Country':3,'Jazz':4,'Vocal':5,'Blues':6,'Folk':7,'Reggae':8,'Electronic':9,'Latin':10,'International':11,'Religious':12,
#        'Stage & Screen':13,'Comedy/Spoken':14,'Classical':15,'New Age':16,'Avant-Garde':17,'Easy Listening':18,'Children\'s':19,'Unknown':20,'influencer_main_genre':21}
# data1=data.drop([0])
# data1=data1.head(1000)
# for i,r in data1.iterrows():
#     G.add_node(r[0])
#     G.add_node(r[4])
#     G.add_edge(r[0],r[4])
# pos=nx.spring_layout(G,iterations=10)
#
# nx.draw_networkx_nodes(G,pos,node_size=10)
# nx.draw_networkx_edges(G,pos)
#
# plt.show()
# count = 1
# total = 0
# dict1 = {}
# for i in G.nodes():
#       total += G.degree(i)
#       dict1[i] = G.degree(i)
#
# print(total)
# dict1 = sorted(dict1.items(), key=lambda kv: (kv[1]), reverse=True)
# dict1
import numpy as np
data2=data.drop([0])
dict1={}
G2 = nx.DiGraph()
c=0
data2=data2.head(500)
Genre={'Pop/Rock':'grey','R&B;':'purple','Country':'red','Jazz':'green','Vocal':'orange','Blues':'blue','Folk':'khaki','Reggae':'moccasin','Electronic':'rosybrown','Latin':'maroon','International':'y','Religious':'navy',
       'Stage & Screen':'lavender','Comedy/Spoken':'midnightblue','Classical':'lime','New Age':'papayawhip','Avant-Garde':'springgreen','Easy Listening':'turquoise','Children\'s':'azure','Unknown':'teal','influencer_main_genre':'violet'}
for i,r in data2.iterrows():
    G2.add_node(r[0])
    dict1[r[0]]=Genre[r[2]]
    G2.add_node(r[4])
    dict1[r[4]]=Genre[r[6]]
    G2.add_edge(r[0],r[4],weight=0.01)

nx.draw_networkx(G2,font_size=0, width=0.1,node_size=np.ones(439)*30,node_color=list(dict1.values()))
plt.show()