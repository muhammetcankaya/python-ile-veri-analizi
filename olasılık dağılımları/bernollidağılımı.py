import numpy as np
from scipy import stats
import matplotlib.pyplot as pyt 
#bernollinin ne olduğunu biliyoruz tam br olay olsun olma durumu 0.2 olmama zıttı zaten bunu bernolli yapalım
#bernolli=pmf

p=0.2
bernolli=stats.bernoulli(p)
print(bernolli.pmf(0))# 1 olma durumunun olasılığı 0 versem olmamayı verir
print(bernolli.expect())#beklenen değer
print(bernolli.var())#varyans