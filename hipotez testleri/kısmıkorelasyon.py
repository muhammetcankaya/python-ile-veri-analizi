import pandas as pd
from scipy import stats
import pingouin as pg
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",13)

print(veri.corr()) # korelasyon matrisini verecektir bize 4*4 5*5 de oabilirdi bu
pg.pairwise_corr(veri)
pg.rcorr(veri,stars=False)#hem anlamlılık hemde şey
print(pg.pairwise_corr(veri))
print(pg.rcorr(veri,stars=False))
# Bu kısmı az önceki örneğe uygun olduğu için aldım 
#Bu baktık yukarda her anlamda baya ii korelasyon var 
#şunu tahminleyelim öğün arttıkça kilo artar
kismukorelasyon=pg.partial_corr(veri,x="Öğün",y="Kilo",covar="Yaş")
print(kismukorelasyon)
#           n         r         CI95%     p-val
# pearson  29  0.518591  [0.18, 0.75]  0.004694
# bak kısmı korelasyon yapınca katsayı nasılda düştü yani daha az korelasyon var
#r korelasyon katsayısı bu arada