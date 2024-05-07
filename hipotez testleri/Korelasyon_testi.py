import pandas as pd 
from scipy import stats
import pingouin as pg
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",13)
#print(stats.shapiro(veri["Sıcaklık"]),stats.shapiro(veri["DondurmaSatış"]))
# ikinci tür normallik testi
print(pg.normality(veri)) # bu baya iyi
import matplotlib.pyplot as plt
import seaborn as sns
# sns.scatterplot(x="Sıcaklık",y="DondurmaSatış",data=veri)
sns.lmplot(x="Sıcaklık",y="DondurmaSatış",data=veri,ci=None)

# plt.show()
#tamam biz bunu grafikte gördük ama bu korelasyon testi nasıl yapılıyor kanka ya burdan anlaşılmazki bu
korelasyon=pg.corr(veri["Sıcaklık"],veri["DondurmaSatış"],method="pearson")
print(korelasyon)

# bu yaptığımız pearson korelasyon testiydi bunun başka testide var kanka
#spearman korelasyon testi nonparemetrik
#veri lineer değilse bu kullanılır lineer değil ama aslında ona yakın doğrusal değil ama eğrisel olarak artan veya azalan olaabilir
korelasyon=pg.corr(veri["Sıcaklık"],veri["DondurmaSatış"],method="spearman") 
# şeklinde yapılır
print(korelasyon)
#tabi bu veri spearmana uygun değil ama uygun olanlarda olacaktır
print(veri.corr()) # korelasyon matrisini verecektir bize 4*4 5*5 de oabilirdi bu
pg.pairwise_corr(veri)
pg.rcorr(veri,stars=False)#hem anlamlılık hemde şey
print(pg.pairwise_corr(veri),pg.rcorr(veri,stars=False))