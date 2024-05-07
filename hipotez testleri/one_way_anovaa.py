# H0: ortlama1=ortlama(2)=ortlama(3)....=ortlama(n)
# H1: ortlama1!=ortlama(2)!=ortlama(3)....!=ortlama(n)  [En az iki grup ortalamaları arasında fark vardır ] hangileri olduğunu past-hoc ile öğreneceğiz.
#örnek çözücez genco 
from scipy import stats

#çok basit bir örnek ile başlılayalım
grupA=[1,2,3,6]
grupB=[1,3,5,7]
grupC=[2,4,6,8]
one_vay_anova=stats.f_oneway(grupA,grupB,grupC)
if one_vay_anova.pvalue>0.05:
    pass
    #print("H0 red edilemez")
else:
    pass
    #print("H0 red edilir")
import pandas as pd
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",5)
İlkokul=veri[veri["Eğitim"]=="İlkokul"]
Lise=veri[veri["Eğitim"]=="Lise"]
Üniversite=veri[veri["Eğitim"]=="Üniversite"]
Yükseklisans=veri[veri["Eğitim"]=="Yüksek lisans"]
one_vay_anova1=stats.f_oneway(İlkokul["Tvizleme"],Lise["Tvizleme"],Üniversite["Tvizleme"],Yükseklisans["Tvizleme"])
if one_vay_anova1.pvalue>0.05:
    print("H0 red edilemez yani bu dört grup arasında tv izleme ortalamaları arasında anlamlı bir fark yoktur")
    print(one_vay_anova1.pvalue)
else:
    print(one_vay_anova1)
    print("H0 red edilir yani bu dört grup arasında tv izleme ortalamaları arasında anlamlı bir fark vardır\nYani eğitim durumunun tv izleme saati açısından farklılık gösterdiğini gözlemlemiş oluyoruz")
    #en az iki grup arasında farklılık var ama hangi eğitim düzeyleri arasında farklılık var şimdi bunu gözlemleyeceğiz
    pass

#BUNUN DEVAMINDA POSTHOC YAPALIM
#varyanlar homojense posthoc kullanılır
from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc=pairwise_tukeyhsd(veri["Tvizleme"],veri["Eğitim"],alpha=0.05)
# ===================================================================
#     group1        group2    meandiff p-adj   lower    upper  reject
# -------------------------------------------------------------------
#          Lise Yüksek lisans     -9.0 0.3867 -24.7226  6.7226  False
#          Lise    Üniversite     10.0 0.3005  -5.7226 25.7226  False
#          Lise       İlkokul     11.0 0.2283  -4.7226 26.7226  False
# Yüksek lisans    Üniversite     19.0 0.0154   3.2774 34.7226   True ANLAMLI FARK VAR YÜKSEL LİSANS ÜNİVERSİTE ARASINDA
# Yüksek lisans       İlkokul     20.0 0.0107   4.2774 35.7226   True BAK BU TRUE OLAN YERLER ANLAMLI FARK VAR DEMEK YÜKSEK LİSANS İLK OKUL ARASINDA
#    Üniversite       İlkokul      1.0 0.9978 -14.7226 16.7226  False
# -------------------------------------------------------------------
print(posthoc)
#BU TESTİN ADI TUKEY TESTİ ÖNEMLİ BİR TESTTİR SPSS DE MEVCUTTUR

#Diyelimki varyanslar homojen dağılmadı o zaman napacaz
import pingouin  as pg # bu kütüphaneyi import edeceğiz ardından burdan welchin anova testini uygulayacağız
print(pg.welch_anova(data=veri,dv="Tvizleme",between="Eğitim"))
#    Source  ddof1     ddof2         F     p-unc       np2
# 0  Eğitim      3  8.808994  4.571703  --0.033826--- 0.524035
#                                       p-unc değeri bizim için önemli 
#                                 bu değer o alan işte bununla hipotezi red edicez veyaz etmicez