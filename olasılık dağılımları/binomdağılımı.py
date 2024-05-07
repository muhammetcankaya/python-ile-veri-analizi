import numpy as np
from scipy import stats
import matplotlib.pyplot as pyt 
#bernolli=pmf
#cdf=birikimli olasılık dağılımı
p=0.2
n=40
dağılım=stats.binom(n,p)
yazı=dağılım.pmf(k=5)#5 defa olma olayı
yazı1=dağılım.cdf(10)#10 ve 10dan az gelme olasılığı
yazı2=1-dağılım.cdf(10)#18 den fazla gelme olasığışı
print(yazı,yazı1,yazı2)
#şimdi burada şunıu yaptık binom dağılımını oluşturduk 10 deneme ve 0.5 olasılık başarı oranı e bunu bernolli ile olasılık yoğunlık fonksiyonu
#halinde yazıp içine değerini verdiğimizde 10 denemede 5 başarı oranınını verecektir başarı oranı biz belirledik p 