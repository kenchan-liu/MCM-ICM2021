import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
data=pd.read_csv("F:\\2021_ICM_Problem_D_Data\\influence_data.csv",header=None)
years=data.iloc[:,4]
a=data.iloc[:,2].value_counts()
genre=['Pop/Rock','R&B','Country','Jazz','Vocal','Blues','Folk','Reggae','Electronic','Latin','','',''
      ,'','','','','','','','']
plt.pie(a,labels=genre)
plt.show()