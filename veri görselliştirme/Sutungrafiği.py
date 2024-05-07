import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
fiyat=[100,200,250,150]
marka=["A","B","C","D"]

sns.barplot(x=marka,y=fiyat)
plt.show()