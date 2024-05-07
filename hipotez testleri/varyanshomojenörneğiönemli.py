import pandas as pd
from scipy import stats
import numpy as np
#burada kuracağımız bu yapı önemli aslında
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",2)
erkek=veri[veri["CİNSİYET"]=="ERKEK"]
kadın=veri[veri["CİNSİYET"]=="KADIN"]
#burada yaptığım şey baya önemli 
#NORMALLİK TESTİMİZ BU DEĞERLER 2 İLE -2 ARASINDA OLDUĞUNDAN ERKEKLER VE KADINLAR NORMAL DAĞILIMA UYGUNDUR
P1=[stats.kurtosis(erkek["HARCAMA"]),stats.skew(erkek["HARCAMA"])]
P2=[stats.kurtosis(kadın["HARCAMA"]),stats.skew(kadın["HARCAMA"])]
print(stats.levene(erkek["HARCAMA"],kadın["HARCAMA"],center="mean"))#P=0.806279132603805
print(stats.bartlett(erkek["HARCAMA"],kadın["HARCAMA"]))#pvalue=0.7091271052832229
#şimdi burada ne yaptık varyansların homojenliğini test etmek için bir yapı kurduk
#hipotezimiz şöyle 
#H0 ORTERKEK=ORTALAMAKADIN
#H1 ORTERKEK!=ORTLAMAAKADINİ
#LEVENE TESTİNİ ÇALIŞTIRDIĞIMIZDA P=0.806279132603805 ÇIKTIĞINDAN 0.5 DEN BÜYÜK BU YÜZDEN H0 RED EDİLEMEZ YANİ 
#VARYANSLAR HOMOJENDİR
#yine aynı hipotez testiyle bartlett testini ugguladığımızda pvalue=0.7091271052832229 0.5 den büyük h0 red edilemez
