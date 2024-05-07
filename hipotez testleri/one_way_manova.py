import pandas as pd 
import pingouin as pg
#burada varyansların homojenliğini show olsun diye başka kütüphane kullancaz


veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",9)

#homojenlik varsayımını kontrol edioyurz
homojenlikerkek=pg.homoscedasticity(veri,dv="ErkekTutum",group="Ürün",center="mean")#0.615585 p değerleri
homojenlikkadın=pg.homoscedasticity(veri,dv="KadınTutum",group="Ürün",center="mean")#0.284943 
#varyanslar homojen dağılmıştır
#varyanslar homojen olduğundan post-hoc yapılır

#bu kısımda covarryans matrisi varsayımını kontrol edioyruz
varcov=pg.box_m(veri,dvs=["ErkekTutum","KadınTutum"],group="Ürün")#0.371307  p değeri H0 red edilmedi corvaryans oldu
# varsayımlarımız uygun olduğundan artık manova yapısını kurabliliriz

#manova yapalım
from statsmodels.multivariate.manova import MANOVA
model=MANOVA.from_formula("ErkekTutum+KadınTutum~Ürün",data=veri)
print(model.mv_test())
#                   Multivariate linear model
# ==============================================================

# --------------------------------------------------------------
#        Intercept         Value  Num DF  Den DF F Value  Pr > F
# --------------------------------------------------------------
#           Wilks' lambda  0.0348 2.0000 56.0000 775.7027 0.0000
#          Pillai's trace  0.9652 2.0000 56.0000 775.7027 0.0000
#  Hotelling-Lawley trace 27.7037 2.0000 56.0000 775.7027 0.0000
#     Roy's greatest root 27.7037 2.0000 56.0000 775.7027 0.0000
# --------------------------------------------------------------

# --------------------------------------------------------------
#            Ürün          Value  Num DF  Den DF  F Value Pr > F
# --------------------------------------------------------------
# ÖNEMLİ    Wilks' lambda 0.9344 4.0000 112.0000  0.9655 0.4294   BURAYI İNCELEYECEĞİZ  0.9655 H0 RED EDİLEMEZ
#           Pillai's trace 0.0656 4.0000 114.0000  0.9659 0.4291
#   Hotelling-Lawley trace 0.0701 4.0000  66.1739  0.9764 0.4265
#      Roy's greatest root 0.0700 2.0000  57.0000  1.9947 0.1454
# ==============================================================
# BU SONUCA GÖRE BAĞIMSIZ DEĞİŞKENİN BAĞIMLI DEĞİŞKENLER ÜZERİNDE BİR OLUMLU ETKİSİ YOKTUR DİYEBLİRİZ


#EĞER ANLAMLI BİR FARK VARYA POST-HOC TESTİ YAPABİLİRİZ YAPALIM BAKALIM NASIIL YAPILIYOR 

posthoc1=pg.pairwise_tukey(data=veri,dv="ErkekTutum",between="Ürün")
posthoc2=pg.pairwise_tukey(data=veri,dv="KadınTutum",between="Ürün")
print(posthoc1)
print(posthoc2)
#         A       B   mean(A)   mean(B)      diff        se         T   p-tukey    hedges erkek
# 0  1.Ürün  2.Ürün  4.883604  5.370008 -0.486404  0.328266 -1.481735  0.307197 -0.487324
# 1  1.Ürün  3.Ürün  4.883604  4.766318  0.117286  0.328266  0.357290  0.932138  0.109650
# 2  2.Ürün  3.Ürün  5.370008  4.766318  0.603690  0.328266  1.839025  0.166210  0.545485
#         A       B   mean(A)   mean(B)      diff        se         T   p-tukey    hedges kadın
# 0  1.Ürün  2.Ürün  7.897250  7.997374 -0.100124  0.346519 -0.288943  0.955057 -0.107377
# 1  1.Ürün  3.Ürün  7.897250  7.910388 -0.013138  0.346519 -0.037914  0.999208 -0.011175
# 2  2.Ürün  3.Ürün  7.997374  7.910388  0.086986  0.346519  0.251028  0.965879  0.071071
#zaten bu biraz anlamsız ama burda p-tukey ile hipotezi red veya kabul edeceğiz