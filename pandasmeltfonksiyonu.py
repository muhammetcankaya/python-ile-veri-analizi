import pandas as pd
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",8)
veri2=pd.melt(veri,id_vars=["Mevki"],value_vars=["1Ay","3Ay","1Yıl","3Yıl ve Üzeri"])
veri2.columns=["Mevki","Süre","Performans"]
print(veri2)
#buda bizim için önemli bir fonksiyondur


#buraya ek olarak kovaryans varyans matrisini de yazayım bari
import numpy as np
x=[45,25,65,54]
y=[46,35,65,24]
veriii=np.array([x,y])
varyanscovaryansmatrisi=np.cov(veriii,bias=True) #bias=true ise popuslasyon false ise örneklem
print(varyanscovaryansmatrisi)