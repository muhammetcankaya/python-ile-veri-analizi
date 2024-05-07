import pandas as pd
# formül 
# Ttest (xort1-xort2)/(örneklem_varyansı**2*(1/n1+1/n2))
#iki grup olduğu için ortak bir varyans bulmamız lazım
#varyans=bununda formulü var
# a okulu ve b okulu ortalamaları arasında anlamlı bir fark vardır diye bir soru varsa
#H0: MA=MB
#H1: MA!=MB
#Bakalım h0 red edebilecekmiyiz 
from scipy import stats
alfa=0.05
sayfa=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",1)
Aokulu,Bokulu=sayfa["A okulu"],sayfa["B okulu"]

thesap,p=stats.ttest_ind(Aokulu,Bokulu,alternative="two-sided")
print(thesap,p)
if p<alfa:
    print("H0 red edilir")
elif p>alfa:
    print("H0 red edilemez")