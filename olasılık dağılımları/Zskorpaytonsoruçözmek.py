from scipy.stats import norm
from scipy import stats
import numpy as np
olasılık13=norm(loc=5.3,scale=1).cdf(4.5)
#şimdi burada yaptığımız şeye bir bakalım
#aslında bir olasılık hesabı yaptık ortalaması=13 ve std=3 olan
#normal dağılmış bir verinin içinden seçeceğimiz bir verinin 13 den küçük olma olasığını bulduk
#e 14 den küçük olmayıda buluruz 17 dende 13 den büyük olma olasılığı da 1-olasılık yapcaz
# peki 14ile 17 arasında olma ihtimailini bul deseydik 
#hatta şöyle yapim 13 15 arası olsun
olasılık15=1-norm(loc=5.3,scale=1).cdf(6.5)


#-----------ORTALAMA TAHMİNİ----------#
#GENE normal dağılan bir veri setimiz var hatta normal dağılan bir örneklemimiz var diyelim
#Bu örneklemin ortalamasını bilip popülasyon hakkında yorum yapmak istiyorsak 
#Bize bir güven aralığı verilecektir zaten bu güven aralığı ve verilen bilgiler ışığında 
#populasyon ortalamasını aralık olarak tahmin edebileceğiz bunu pythonla yapalım bakalım
n=100#örneklem sayısı 30 dan büyük olduğu için z tablosu kullanırız değilse t tablasu olur
xort=1040#örneklemin ortalaması
xstandart=25#örneklemin standart sapması
güven=0.95#güven aralığı
# bu bilgiler ışığında ben populasyon ortalamasını bir aralık olarak bulucam 
# Bulduğum bu aralık 0.95 güven verecektir 
aralık=stats.norm.interval(confidence=güven,loc=xort,scale=xstandart/n**0.5)
print(aralık)#burada gördüğümüz gibi popuslasyon ortalaması 1035  ve 1044 arasında olacaktır
#pek biz bu yapıyı neden ve ne zaman kullanacağız aslında şöyle iki madde var 
#soru şuysa bu düşünülür populasyon ortalamasının aralığını bulunuz
#diğer şart da şu ya populasyon std si verilecek yada orneklem 30 dan büyük olacak
# o zaman böyle bir uygulamayla populasyon ortalamasının aralığını yüzde 95 güvenle bulabiliriz