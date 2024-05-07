from scipy import stats
#hemen kesikli bir unüform dağılım oluşturalum
n=6 # zar örnegği basitçe
dağılım=stats.randint(1,n+1)#1 ekledik son değeri almıyor
olasılık=dağılım.pmf(4) #pmf ile gelme olasılığı hesaplanır
print(olasılık,dağılım.expect(),dağılım.var(),dağılım.cdf(3))
#sürekli olmayan yukarda o uniformla değilde randintle oluşturuluyor
#sürekli dağılım 
a=0
b=15
uniform=stats.uniform(a,b)
print(uniform.expect(),uniform.var(),uniform.cdf(12.5))
#sürekli uniform dağılımına bakabilirisin burayı hatırlamazsan
#kanka bunun alanı dümdüz kare zaten başlangıç 5 son 10 olur o alan 1 olmalı mesela ordan falan filan baya basit
