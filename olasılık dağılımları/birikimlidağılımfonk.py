from scipy import stats

olasılık1=stats.norm.pdf(x=11,loc=15,scale=3)
# print(olasılık1)
#pdf demek olasılık yoğunluk fonksiyonu7 demektir
#bu yapı aslında bize bir olasılık yoğunluk fonksiyonu oluşturur
#ortalaması 15 standanrt sapması 3 olan bir yapı 
#x=11 de bizim aradığımız değer bak burda olasılık hesaplamıyoruz
#bu fonksiyonda x=11 iken y kaç çıkar diyoruz çantınmı 
#zaten alanı bulmak için z skore örnekleride var 
#yada bunun integralini alabiliriz
#Birikimli dağılım bunun neresinde mesela biz 11 den küçük olduğu olasılığı yani alanı istiyoruz 
#zaten adı üstünde birikimli olasılık dağılımı olduğundan 11 e kadar değerleri toplar peki bunu nasıl yaparız
#zaten birikimli olasılık dağılımı söyle o alosılığa kadar öncekileri toplar
olasılık2=stats.norm.cdf(x=11,loc=15,scale=3)
# print(olasılık2)
#Bu seferde o alanı buldu yani oalsılığı buldu cdf=birikimli olasılık dağılımı pdf=olasılık yoğunluk fonksiyonu
 #bunu anlağımıza göre bir kesikli kümülatif bir de sürekli kümülatif örnekleri yapalım
#KESİKLİ
import matplotlib.pyplot as pyt
import seaborn as sns
#para deneyi olsun
x=[0,1,2,3]
u=[1/8,3/8,3/8,1/8]
cum=[]
for i in range(0,len(u)):
    if len(cum)==0:
        cum.append(u[0])
    else:
        cum.append(u[i]+cum[i-1])
#pyt.bar(cum,x)
# print(cum)
# pyt.plot(x,cum,drawstyle="steps")
# pyt.show()
#burada bir parayı üç kere attığımızda tura gelme olayının birikimli olarak grafiğini yaptık
#haydi bir de normal dağılım yapalım
import numpy as np
sayılar=np.random.randn(10000)#normal dapğpğılıma uyan 10000 sayı  
pdf=stats.norm.pdf(sayılar)#şuanda bu 10000 değer için olasılık ypğumluk fonksiyonu oluşturuldu
#aşağıda daolasılık birikimli fonksiyon oluşturalım
print(pdf)
sns.lineplot(x=sayılar,y=pdf)

cdf=stats.norm.cdf(sayılar)
sns.lineplot(x=sayılar,y=cdf)
pyt.show()

#BU HİKAYEDE BÖYLECE BİTMİŞ OLDU NE ÖĞRENDİK PDF=OLASILIK YOĞUNLUK FONKSİYONU
#CDF=BİRİKİMLİ OLASILIK DAĞILIM DAĞILIM FONKSİYONU 
#BUNLARI NASIL ÇALIŞTIRACAĞIMIZI GÖRDÜK MESALA BİR SAYI DİZİSİ VAR DİYELİM 
#ONU SCİPY KÜTÜPHANESİNİ KULLANARAK BU SAYILARI PDF VEYA CDF HALİNE GETİREBİLİYORUZ :)) BU KISIMDA ÖĞRENDİKLERİMİZ 
#BU KADAR FAKAT BUNLARI YAPARKEN GRAFİK YAPMAYIDA GÖRÜYORUZ