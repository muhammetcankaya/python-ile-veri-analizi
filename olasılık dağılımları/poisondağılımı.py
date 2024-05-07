from scipy import stats
#beklenen değer ve varyansları görcez
#soru şumuş ki alttaki gibi çözüm yapmışız
# dakikada 10 arama alan bir şirketin dakikada 2 arama alma olasığı nedir poisson dağılımı


# ortlama=10
# dağılım=stats.poisson(ortlama)
# p0=dağılım.pmf(2)
# #print(p0)
# #bir yılda 1825 tane satılmıştır tv önümüzdeki herhangi bir ünde satış kaç tane olur 9 adet satma olasılığımız
# ortalama=5
# dağılım1=stats.poisson(ortalama)
# p9=dağılım1.pmf(k=9)
# #en fazla 9 satma olasğılım
# hmm=dağılım1.cdf(9)
# print(p9*100,hmm*100)


# yeni örnek
#1 yılda 2 fırtına çıkıyor 1 3 ve 5 fırtına olma olasılıkları
ortalama=2
dağılım=stats.poisson(ortalama)
p1=dağılım.pmf(k=1)
p3=dağılım.pmf(k=3)
p5=dağılım.pmf(k=5)
c5=dağılım.cdf(x=5)
print(p1,p3,p5,c5)