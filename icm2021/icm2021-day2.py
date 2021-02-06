dataf=pd.read_csv("C:\\Users\\kentl\\Desktop\\classified\\pop.csv",header=None)
import numpy as np
data=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\data_by_artist.csv")
ax=-1
for i,r in data.iterrows():
    ax+=1
    if((r[1] in dataf.iloc[:,4])==False):
        data.drop(labels=ax,inplace=True)
from  sklearn import preprocessing
data1=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\data_by_artist.csv")
dataf=pd.read_csv("C:\\Users\\kentl\\Desktop\\classified\\folk.csv",header=None)
ax=-1
for i,r in data1.iterrows():
    ax+=1
    if((r[1] in dataf.iloc[:,4])==False):
        data1.drop(index=ax,inplace=True)
print(data1)
for i in range(4):
    data1.iloc[i,2:]=preprocessing.scale(np.array(data1.iloc[i,2:]).astype(float))
data2=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\data_by_artist.csv")
datap=pd.read_csv("C:\\Users\\kentl\\Desktop\\classified\\pop.csv",header=None)
ax=-1
for i,r in data2.iterrows():
    ax+=1
    if((r[1] in datap.iloc[:,4])==False):
        data2.drop(index=ax,inplace=True)
for i in range(218):
    data2.iloc[i,2:]=preprocessing.scale(np.array(data2.iloc[i,2:]).astype(float))
t = 0
for i in range(218):
    for j in range(218):
        t+=np.linalg.norm(data2.iloc[i,2:14]-data2.iloc[j,2:14])
print(t/(218*218))
q=0
for i in range(4):
    for j in range(4):
        q+=np.linalg.norm(data1.iloc[i,2:14]-data1.iloc[j,2:14])
res=q/16
f=0
data=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\data_by_artist.csv")

for i in range(200):
    for j in range(200):
        m1= preprocessing.scale(np.array(data.iloc[i,2:]).astype(float))
        m2= preprocessing.scale(np.array(data.iloc[j,2:]).astype(float))
        f+=np.linalg.norm(m1-m2)
print(f/40000)
q=0
for i in range(20):
    for j in range(20):
        m1= preprocessing.scale(np.array(data3.iloc[i,2:]).astype(float))
        m2= preprocessing.scale(np.array(data1.iloc[j,2:]).astype(float))
        q+=np.linalg.norm(m1-m2)
print(q/400)