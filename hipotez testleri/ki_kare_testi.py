# şimdi frekanslı halinde gelmeyen bir veriyi frekans tablosu haline getireyim
#frekans haline gelmemiş yapıyı frens haline getirelim 
#unutma ki kare testi frekans tablosundan yapılır
import pandas as pd
import numpy as np
from scipy import stats
veri=veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",10)
frekans=pd.Series(veri["Kilo"]).value_counts()
kikare=stats.chisquare(frekans)
#print(kikare)  # Power_divergenceResult(statistic=0.016, pvalue=0.9920319148370607) 
#pvalue 0.05 den büyük olduğundan H0 red ediilemez yani benim gözlemlediğim değer ve beklenen değer arasında anlamlı bir fark yoktur
#Bu kısım uyum testiydi tek değişken iken yapılır çok önemli değildi 
#Ki kare bağımsızlık testi
#Burada bir tablo olacak kare tablo ve kare olmayan tablolar vardır
#bak şimdi baba burda satırların kategorik ve sutun başlıklarının kategorik olduğunu düşün dur yapıcam ya aşağıda
#         kısa boy        orta boy        uzun boy
# erkek     veri            veri            veri
# kadın     veri            veri            veri
#yukarıdaki gibi bir veri yapısına sahip isek ne 
#Ki kare bağımsızlık testi bize şunu şöyleyecek cinsiyet değişkeni boy ile bağımlımıdır değilmidir 
#H0 Bu iki değişken arasında ilişki yoktur 
#H0 Bu iki değişken arasında ilişki vardır
#Şimdi biz burada sutun ve satır sayıları 2 ye eşitse yani 2*2 likse bu başka bundan daha büyükse başka şekilde çözüm yapacağız
#2*2 için beklenen değer 25den büyük ise
#pearson ki kare testi uygulanır 
#5 ile 25 arasında ise yates kikare testi uygulanır
#5 den küçükse fisherin ki kare testi kullanılır
#herhangi bir veri ayarlayacağım ve bu veri 2*2 lik olacak ondan sonra bu veriyi okuyup bunu tablo haline getircem
#sonra beklenen değeri bulcam ordan yapmam gereken testin ne olduğunu konuşadacağız
veri1=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",11)
tablo=pd.crosstab(index=veri1["Cinsiyet"],columns=veri1["El"])
#şimdi bu veri biraz dağınıktı biz bu veriyi aldık düzenledik test yapılır hale getirdik
test,p,sd,beklenen=stats.chi2_contingency(tablo)#şimdi biz 
#bu 2*2 lik tablodan en küçük beklenen frekans değerine göre hangi testi yapacağımızı seçeceğiz
#2*2 için beklenen değer 25den büyük ise
#pearson ki kare testi uygulanır 
#5 ile 25 arasında ise yates kikare testi uygulanır
#5 den küçükse fisherin ki kare testi kullanılır
#6.17821782 olduğuna göre uygulamamız gereken test yates ben şurda bir if yapısıyla halledicem şimdi bu işi
if np.min(beklenen)>25:
    #pearson
    test,p,sd,beklenen=stats.chi2_contingency(tablo,correction=False)
    print(test,p)
elif np.min(beklenen)<25 and np.min(beklenen)>5:
    test,p,sd,beklenen=stats.chi2_contingency(tablo,correction=True)
    print(test,p)
elif np.min(beklenen)<5:
    fisher=stats.fisher_exact(tablo)
    print(fisher)



#ŞİMDİ r*c lik haline bakalım
#Bu aq şeyi burdan yapmak çok mantıksız 
#bunu araştırmak lazım spss ile bu iş baya kolay