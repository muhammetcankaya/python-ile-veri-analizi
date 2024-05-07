# H0: ortalama_öncesi=ortalama_sonrası 
# H1: ortalama_öncesi!=ortalama_sonrası 
# paried sample test
import pandas as pd
from scipy import stats
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",4)
#burada önce normallik varyansların homojenliği vesaire test edilir 
bağımlı_örneklem_test=stats.ttest_rel(veri["Önce"],veri["Sonra"],alternative="two-sided")#bunun içinde iki değer var 
# biri normal dağılım grafiğinde alanı bulmak için z skor dediğimiz şey
# diğeri o alan o alanla benim güven kısmını kıyaslamam lazım
guven=0.5
if bağımlı_örneklem_test.pvalue>guven:
    print("H0 red edilemez yani bunlar arasında anlamlı bir fark yoktur")
else:
    print("H0 red edilir bu olay sonrasında grupta bu olay neticesinde ortalamalar arasında anlamlı bir fark vardır")
#Bu kısımda normallik testi yaparken iki durum arasında şu mantık kurmicaz 
#olay öncesi normal dağılım varmı olay sonrası varmı diye değilde bu değerler arasındaki farkın normal dağılımını kontrol etmemiz 
#gerekmektedir bununla ilgili örnek yaparız beklide