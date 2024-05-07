import pandas as pd
#nedir
#veri analizde kullanılır 
#dosya okuyabilir
# seri=pd.Series()
# #boş bir seri
# # şimdi ise bir kaç seri oluşturalım
# sayılar=pd.Series([5,6,4,8,6,3])
# ondalık=pd.Series([4.5,4.2,1.2,3.6])
# karakter=pd.Series(["m","c","k"])
# print(sayılar) # aşağıda gördüğümüz kısımı index ve ona\
# print(ondalık)# karşılık gelen değerleri veri ve veri
# print(karakter)# tipini söyledi excele benziyor
# 0    5
# 1    6
# 2    4
# 3    8
# 4    6
# 5    3
# dtype: int64
# 0    4.5
# 1    4.2
# 2    1.2
# 3    3.6
# dtype: float64
# 0    m
# 1    c
# 2    k
# dtype: object

# biz değerlerin indexlerini değiştirebiliriz
# x=["a","b",5,7]# olsun şimde seri oluşturalım
# y=pd.Series(x,[2,3,5,6])
# print(y) indexleri bu şekilde değiştirdik
# 2    a
# 3    b
# 5    5
# 6    7
# dtype: object
# bu pandan yapısındadad istediğimiz indekslere ulaşabiliriz
#aynı mantıkda listeyle buraki avantaj indeksi sen belirler
#ve rahatça çağırabilirsin
# x=pd.Series([1,2,35,6,4])
# x.sum()
# x.mean()
# x.var()
# x.std()
# x.descibe()#tanımlayıcı istatislikler
# oluşturduğum veri otomasyondaki verileri alıp dataframe
# yaparak onları tablo haline getircem ödev...
# dataframe kısmının notlarını iyice cıkardıktan sonra 
# bu notlara bakarak kendi seçtiğin bir veri üzerinde bütün
#işlemleri uygulayacaksınnn
#dataframe aslında bir excel şeklin bir tabloyu bize 
#pytonda verir bunun üzerinde işlemler yapmak 
#için python da başka yöntemler vardır güzeidir onlar haydi
#inceleyelim
# seri1=[1,3,5,7,9]
# seri2=[0,2,4,6,8]
# başlıklıveri=dict(ürün1=seri1,ürün2=seri2)
# veriler=pd.DataFrame(başlıklıveri)
# print(veriler)# görüldüğü gibi bak bir tablo gibi birinci sutun 
# #indexler aslında 1.satır ürün kodları diğer kısımlarıda değerler
# #    ürün1  ürün2
# # 0      1      0
# # 1      3      2
# # 2      5      4
# # 3      7      6
# # 4      9      8
# df=pd.DataFrame([["elma",10],["armut",15],["kivi",20]],index=True,columps=["ürünler","fiyat"])
# print(df)
 
#        0   1
# 0   elma  10
# 1  armut  15
# 2   kivi  20
# bu kısımda sutun başlıkları giremedik columps yapısı sıkıtlı
# veri=[["elma",10],["armut",15],["kivi",20]]
# başlık=[1,2,3]
# print(pd.DataFrame(veri,index=başlık,columns=["ürünler","fiyat"])) # başlıkları sutun başlığı olarak
#koyamadım sözlük yapısıyla oluyor fakat colump yapısı 
# çalışmıyor çalışıyor düzgün yaz malmısın aq
#   ürünler  fiyat
# 1    elma     10
# 2   armut     15
# 3    kivi     20
# sözlük={"ürün":["elma","armut","kivi"],"fiyat":[10,15,20]}
# print(pd.DataFrame(sözlük,index=[1,2,3]))
#     ürün  fiyat
# 1   elma     10
# 2  armut     15
# 3   kivi     20

# csp ve excelden veri çekmek
#veri=pd.read_csv("dosyanın yolu hangi dosyayı okuyacaksan")
#excelden çekmek
#veri1=pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/NARİN KAYA.xlsx")
#yaptıktan sonra geliyor buraya yol
#örnek olarak burada narin kaya dosyasını çekmiş olduk
#ŞİMDİ BİR KAÇ METOD SATIR SUTUN İŞLEMİ ÖGRENECEĞİZ BU VERİDE UYGULARI
#             Ülkeler   LEVEL 1    LEVEL 2    LEVEL 3    LEVEL 4    LEVEL 5    LEVEL 6    LEVEL 7   LEVEL 8
# 0         Australia  1.525454   5.571776  12.530159  21.111200  25.375310  20.868243  10.329688  2.688169
# 1           Austria  0.957921   6.407249  16.258093  23.483885  26.211394  19.270051   6.672010  0.739398
# 2           Belgium  1.215191   5.991531  14.046740  22.355538  26.482681  20.361348   8.265314  1.281657
# 3            Canada  0.695237   3.099607   9.955468  20.118562  27.164958  23.973146  12.154291  2.838730
# 4             Chile  1.817807   8.868068  21.035076  29.487161  24.418887  11.778833   2.410433  0.183734
# 5          Colombia  3.799032  15.779130  30.324988  27.662931  15.811803   5.676212   0.910932  0.034972
# 6    Czech Republic  0.798219   4.962791  14.979472  24.956897  26.936234  19.129919   7.184082  1.052384
# 7           Denmark  0.579983   3.512576  11.906975  23.901207  30.107231  21.576709   7.312377  1.102941
# 8           Estonia  0.285176   2.059311   8.709795  21.159821  29.896048  24.030531  11.053392  2.805926
# 9           Finland  0.848422   3.326265   9.369840  19.249470  27.583047  25.389044  11.870714  2.363199
# 10           France  1.177895   5.737406  14.021949  22.846020  26.566999  20.452641   8.060547  1.136544
# 11          Germany  1.364761   5.747145  13.573189  21.130336  25.405790  21.472556   9.510068  1.796156
# 12           Greece  2.239636   9.322713  18.953448  27.347574  25.151832  13.334697   3.311423  0.338677
# 13          Hungary  1.283878   6.961658  17.028408  25.162039  26.323718  17.531982   5.197685  0.510632
# 14          Iceland  2.435377   8.038736  15.881787  24.609120  25.074249  16.854802   6.244739  0.861192
# 15          Ireland  0.214385   2.110986   9.473979  21.742397  30.290825  24.078890  10.329447  1.759092
# 16           Israel  5.714095  10.372669  14.975350  19.409056  21.579246  17.543290   8.358321  2.047973
# 17            Italy  1.801726   6.692366  14.773080  26.286987  28.213774  16.887359   4.878779  0.465929
# 18            Japan  0.706968   4.077847  11.994356  22.498558  28.609232  21.862572   8.596876  1.653590
# 19            Korea  1.172898   4.312066   9.623306  19.578623  27.634567  24.555220  10.805079  2.318240
# 20           Latvia  0.611166   5.218760  16.612955  27.379078  28.793708  16.565046   4.422259  0.397028
# 21        Lithuania  1.075936   6.307024  16.980336  26.107671  27.695604  16.851929   4.531708  0.449792
# 22       Luxembourg  2.504697   9.156203  17.630515  23.691511  23.463039  15.947723   6.355316  1.250996
# 23           Mexico  2.540847  13.098927  29.054227  31.735157  17.458554   5.338823   0.747096  0.026368
# 24     Netherlands*  1.466236   6.980926  15.639444  23.747949  24.286360  18.796967   7.894449  1.187669
# 25      New Zealand  1.080584   5.223512  12.659465  20.794754  24.636255  22.501637  10.749929  2.353864
# 26           Norway  1.770752   5.634923  11.887306  21.466295  26.378962  21.572065   9.642264  1.647433
# 27           Poland  0.568252   3.324113  10.783242  22.408296  27.688291  23.035428  10.083501  2.108878
# 28        Portugal*  0.913375   4.978828  14.329668  23.332379  28.178550  20.974547   6.491337  0.801317
# 29  Slovak Republic  2.390175   9.223838  19.796012  26.851725  23.531531  13.571965   4.145014  0.489740
# 30         Slovenia  0.689732   4.250369  12.940890  24.524055  29.535149  20.306574   6.777780  0.975451
# 31           Sweden  1.615502   5.140563  11.636979  20.605969  25.472850  22.254771  10.884074  2.389293
# 32      Switzerland  1.407744   7.123001  15.103314  23.420626  26.334764  18.510937   6.945758  1.153856
# 33           Turkey  0.702660   6.345473  19.084120  30.174289  26.877445  13.488857   3.126576  0.200581
# 34   United Kingdom  0.845020   4.172749  12.285327  22.981228  27.219269  21.045052   9.451283  2.000072
# 35   United States*  1.144312   5.373624  12.747906  21.090381  24.657380  21.446027  10.709324  2.831046
veri1=pd.DataFrame(pd.read_excel("C:/Users/Muhammet can/OneDrive/Masaüstü/yessir.xlsx"))
# veri1["Ülkeler"] # sutun çekme ülkeler sutununu çektim
# #birden fazla sutun çekme
# veri1[["Ülkeler","LEVEL 1"]]# iki paranteze dikkat et 
# # satır çekmek için nopacaz
# veri1.loc[0] # 1.satırı getirir yanı 0.satır
# veri1.loc[[0,1,2]]# ilk üç satırı verecektir
# #loc parametresini farklı kullanımı
# veri1.loc[5,"LEVEL 1"]#sutun ve satırın kesiştiği yerrdeki 
# #elemanı döndürür
# veri1.loc[0:5,"LEVEL 1"]
# #0ile5 satır arasındaki değeleri bu sutunda getir
# veri1.loc[0:5,"LEVEL 1":"LEVEL 2"]
# # bu iki sutundan ve satırlar arasındaki değerleri ver

# #SATIR VEYA SUTUN EKLEME
# burada verimize sutun ekledik 
#bunu yaparken görüldüğü üzere yeni sutunummuzu
# level7 ve level8 in toplamı yaptık
####veri1["LEVEL7+LEVEL8"]=veri1["LEVEL 7"]+veri1["LEVEL 8"]
# print(veri1["lvl7+lvl8"])
#PEK DİYELİM Kİ YENİ OLUŞUTRACAIMIZI 
#SUTUNU ARAYA ATACAĞIZ O ZAMAN NE YApcaz
#insert metodu ile 4.indekse hahahahaha başlıklı value değğeri yazan yani sutundaki
#değerleri yazan sutunu atadı 4.den sonrasını sağa kaydırır bunu sen merak etmiştin
#devaaaam
# veri1.insert(4,column="HAHAHAHAHA",value=veri1["LEVEL 1"])
# print(veri1)

#DİYELİMKİ BİRŞEY SİLMEK İSTİYORUZ DROP METODU KULLANACAĞIZ
# FAKAT BU METOD DİREKT OLARAK SİLMEZ KALICI SİLMEZ YANİ GEÇİÇİ SİLER
#BİZ SİLDİĞİMİZ HALİNİ BAŞKA BİR DEĞİŞKENE ATARSAKL ORDA YOK GÖRÜRÜZ SİLİNCEDE SİLİNMİŞ OLMAZ AMA
veri2=veri1.drop("Ülkeler",axis=1)
#sutundan silme işlemi yaptı silinmiş halini veri 2 ye atadı
#satırdan yapmak isteseydik axis=0 :)

#ŞİMDİDE BİR KAÇ FİLTRELEME YAPISI GÖRELİM
# veri1.head() #bize ilk beş satırı döndürecektir
# veri1.head(10) # ilk on satırı döndürecektir
# veri1.tail() # sondan beş satır
# veri1.tail(10) # sondan 10 satır
# # belirli bir sutundan belirli sayıda satır getşrne
# veri1["Ülkeler"].head(15)# ilk 15 ülkeyi getirecektir
# # şöyle yaparsak
# veri1[["Ülkeler","LEVEL 1"]].head(15)
# # ülkeler ve levevl1 sutunundan 15 satır getircektir
# veri1[5:][["Ülkeler","LEVEL 1"]].head(15)
# eğer yapıyı böyle kurarsak 5.satırdan başlar 15 satır gider 20 e kadar

#Şimdide verinin içerisindeki değerlere göre filtreleme yapalım
# veri1=="LEVEL 1" # VERİ içersinde level 1  ara bulursan
# #true bulamazsan false dönder bool değer görmek istoyrsak
# veri1[veri1=="LEVEL 1"] # SEFER LEVEL 1 BULACAK DİĞER DEĞERLERİ
# #Boş hücre olarak döndürecektşr

# #SAYISAL BAKALIM
# veri1[veri1>10] # 10 DAN BÜYÜK DEĞERLERİ GÖSTERİR OLMAYANLAR NAN
#Dikkat eğer bir filtreleme işlemi sayısal yapılacaksa
#her şeyin sayısal olması lazım o zaman sayısal olmayan kısmı cıkarır
#veya sutun bazlı arama yaparız
#hemen kendimiz için kısa bir örnek yapalım
#biz veri2 değişkeninde silme yapmıştık orda ülkeleri silelim
print(veri2[veri2>10])
 