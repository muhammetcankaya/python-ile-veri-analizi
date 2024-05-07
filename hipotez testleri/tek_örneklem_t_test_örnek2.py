import pandas as pd
from scipy import stats
#örnek
#bir otomobil parçası üreliyor bu üretim bandında günlük hatalı üretim ortlama 20 
#bu sayı hakkında şüpheye düşülüyor test lazım
#25 gün veri topluyoruz 
#hatalı ürün sayıları örneklemde verilmiştir
#bu 20 değerini test etmek istiyoruz
#95 güvenle
#H0: M=20
#H1: M!=20
alfa=0.05
sınav=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx")["sınav1"]
thesap,p=stats.ttest_1samp(sınav,popmean=20,alternative="two-sided") #less veya greater 
print(thesap,p)
if p<alfa:
    print("H0 red edilir\nYani günlük hatalı üretim ortlaması aslında 20 ye eşit değildir")
else:
    print("H0 red edilemez yani günlük hataı üretim ortalaması 20 dir %95lik anlam düzeyinde")
