import pandas as pd
from scipy import stats
veri=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx",3)
evet=veri[veri["CEVAP"]=="evet"]
hayır=veri[veri["CEVAP"]=="Hayır"]
levene=stats.levene(evet["SİGARA"],hayır["SİGARA"],center="mean")
bartler=stats.bartlett(evet["SİGARA"],hayır["SİGARA"])
iki_örneklem_t_test,p=stats.ttest_ind(evet["SİGARA"],hayır["SİGARA"],alternative="two-sided")
print(levene.pvalue,bartler.pvalue,p)
alfa=0.05
#H0 sigara içen ve içmelenlerin nefeslerini tutmaları arasında anlamlı bir fark yoktur
#H1 sigara içen ve içmelenlerin nefeslerini tutmaları arasında anlamlı bir fark VARDIR
if levene.pvalue>alfa:
    if p<alfa:
        print("""H0 RED EDİLİR
Bu iki verinin aralarında anlamlı fark vardı
YANİ BURADA SİGARA İÇENLERİN NEFESLERİNİ DAHA AZ TUTTUĞU GÖZLEMLENEBİLİR """)
    else:
        print("H0 red edilemez")
else:
    print("varyanslar homojen değil")
# YANİ BURADA ŞHOW OLSUN DİYE LEVENE BARTLETT FALAN YAPTIK 
# shapiro p değeri 0.05 den büyükse normal dağılım H0 red edilemez
# levene 0.05 den büyükse varyanslar homojen H0 red edilemez
# independent two test 0.05 den büyükse anlamlı bir fark varmı p>guven H0 red edilemez p<guven HO red edilir
# bu testi yapmadan önce normal dağılım varyanslar homojenmi ardından testi yap bunlar önemli
# varyanslar homojen değilse şu taktiği uygulacaz 
print(stats.ttest_ind(evet["SİGARA"],hayır["SİGARA"],alternative="two-sided",equal_var=False))
print(stats.ttest_ind(evet["SİGARA"],hayır["SİGARA"],alternative="two-sided"))
#yapıyı bu şekilde kurmamız gerekiyor bu varyanslar homojen değil ona göre test yapıyorum demek