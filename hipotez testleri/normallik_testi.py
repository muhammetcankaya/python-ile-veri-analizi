from scipy import stats
import matplotlib.pyplot as plt
import seaborn
import numpy as np

np.random.seed(10) #bu yapı random olarak gelen değerlerin değişmemesi için kullanılır
veri=stats.norm.rvs(loc=40,size=1000)
#skewnes kurtosis
if -1.5<stats.kurtosis(veri)<1.5 and -1.5<stats.skew(veri)<1.5:
    print("Dağılım normaldir")
else:
    print("Dağılım normal değildir")
#Bu kullandığımız birinci teknik olan skewnes and kurtusis değerleri ile yapılan analizdi
#Farklı ve ilgimi çeken yöntem

stats.probplot(veri,dist="norm",plot=plt)
plt.show()#şimdi bu yapıyla bize bir görsel çıkacaktır 
#bir doğru ve bu doğrunun etrafında noktalar bu noktalar bizim verimizdeki değerlerdir
#bu noktalar o doğruya yakınsıyorlarsa verimiz normal dağılmıştır o doğrudan uzaklaştığı yerler
#aykırı noktalardır ama buraya geleceğiz
#Kolmogorov-Smirnow ve Shapiro-milk testi 
#Burada skewnes kurtosise nazaran bu aslında bir hipotez testidir burada bizim bir 
#guven katsayısına ihtiyacımız var diyelimki yüzde 95 güvenle bu sınamayı yapıyoruz 
guven=0.5#güven kat sayımız
#kstest=stats.kstest(veri,cdf="norm") eğer yapıyı böyle kurarsak bu bize normal dağılım testi yapacak amak ortalama 0 std 1 olarak düşünerek yapacaktır 
#bu yüzden veri normal dağılmamış zannedeceğiz o yuzden ortalama ve std yi de yazmamız lazım
#kolmogorov
kstest=stats.kstest(veri,cdf="norm",args=(veri.mean(),veri.std()))#testi uygularken veri girdik ne testi yapacaz girdik kendi verimizin ortlamsı std si girdik
print(kstest) #şimdi biz normallik testini yapan if yapısını kuracağız 
if kstest.pvalue>guven:
    print("veri normal dağılmıştır")
else:
    print("Normal dağılmamıştır")
#Shapiro testi aynı mantık
smtest=stats.shapiro(veri)#burada ıvır zıvıra çok gerek yok direkt algılıyor 
print(smtest)
if smtest.pvalue>guven:
    print("veri normal dağılmıştır")
else:
    print("Normal dağılmamıştır")