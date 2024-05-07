#örnek 
#bir doktor kandaki x değerinin 200 den farklı olması gerektiğini söylüyor 
#rastsal olarak 20 hasta seçilir x ortalaması 311.2 olarak çıkıyor stdsi örnekleklemin 64.4 olduğu söylenir
#200 den farklı olduğu yüzde 95 güvenle teest edilsin yüzde 95 anlamlılık
# xort=311.2
# xstd=64.4
# n=20
# #H0:M=200
# #H1:M!=200 çift  taraflı olacak t testi
# Thesap=(xort-200)/(xstd/n**0.5)
# #burada alanı kıyaslamadığımız için ikinci çözümü aşağı yazıcam
# #şimdi bizim Tkıyas [tablo değeri] değerini tablodan bulmamız lazım n-1 yani 19 serbestlik derecesinde 0.05 anlamlılık düzeyinin çift taraflı halindeki halini bulcaz
# #oda 2.093 dür
# Tkıyas=2.093
# if Thesap>Tkıyas:
#     print("H0 red edilir")
# else:
#     print("H0 red edilemez")

#şimdi alanlar üzerinde kıyas yapalım
#şimdi bu kısımda p ile guven derecesini kıyaslayarak çözeceğiz pythonu aktif kullanarak daha doğrusu
    
#diğer örnek
#bir sınavda geçmiş veriler değerlendirip ortalması 228 dir 
#yeni sınav sisteminde bu değişiyor mu
#bunun için 12 tane öğrenci seçiliyor yüzde 95 güvenle
#ÖRNEKLEM ortalması
#örneklem standart sapması falan bunları bulcaz
#H0 M=28
#H1 M!=28
#burada biz t hesap ile p yi kıyaslayacaz
import pandas as pd
from scipy import stats
sınav=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/sadas.xlsx")
alfa=0.05
xort=sınav.mean()
xstd=sınav.std()
thesap,p=stats.ttest_1samp(sınav,popmean=28,alternative="two-sided")
print(thesap,p)
#[2.74619412] [0.01901964]
#p eşittir t hesaba karşılık gelen p değeri
#bak şimdi coni burada iki tane değer çıkıyor thesap dediğmiz şey bizim tabloda bulmak için kullandığımız şey işte bu 
#burada önemli olan p değeri p değeri ile güven alanını kıyaslayacağım
#bu kıyas neticesinde h0 red veya kabul edilecek e şunu biliyor 
#p<alfa ise h0 red edilir p>alfa ise h0 red edilemez
if p<alfa:
    print("h0red edilir")
else:
    print("red edilemez")