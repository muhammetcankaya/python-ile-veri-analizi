import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd 
from scipy import stats
# burada yapacağım örneği kesinlikle çok anlamadım sadece kopyala yapıştır yapıcam ama bilmiş olmak için elimizde bulunsun
veri1=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",6)

model="Verim ~ C(Gübre) + C(Tohum) + C(Gübre) : C(Tohum)"
test=ols(model,data=veri1).fit()
anova=sm.stats.anova_lm(test,type=2)

#                      df     sum_sq   mean_sq         F    PR(>F)
# C(Gübre)            2.0   1.908320  0.954160  0.580127  0.569956
# C(Tohum)            3.0   1.642776  0.547592  0.332934  0.801651
# C(Gübre):C(Tohum)   6.0   4.390924  0.731821  0.444945  0.839091
# Residual           18.0  29.605403  1.644745       NaN       NaN
#PR(>F) DEĞELERİ BİZİM TESTİ UYGULAYACAĞIMIZ DEĞERLER BU VERİ İÇİN H0 RED EDİLEMİYOR YANİ GÜBREİNİN ETKİSİ TOHUMUN ETKİSİ 
#GÜBRE VE TOHUMUN ETKİSİ OLARKA BAKTIĞIMIZDA HO RED EDİLEMİYOR YANİ BU ORTALAMALAR ARASINDA ANLAMLI BİR FARK YOKYUR
#Örnek diğer
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",7)
print(veri)
#KANAKA BU 77. VİDEOYU TEKRAR İZLEMEN LAZIM YA