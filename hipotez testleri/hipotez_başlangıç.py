#örnek
#z skor tablodan çözülecek 
# z istatisliği formolü 
# (örneklem ortalaması- populasyon ortalaması)/(standart sapma / örneklem sayının karekökü)
#bir fabrikada üretilen vidaların boylarının ortalama olarak 100 mm olduğu tespit edilmiştir standar sapması 2 mm makinede
#çıkan bir sıkıtıdan sonra yapılan araştırmada 9 tane örneklem üzerinden ortalama 102 tespit ediliyor
#makinede bir sıkıntı varmı yokmu 
#yüzde 95 güven düzeyi
#alfa=0.05
#H0=100
#H1!=100
zhesap=(101.3-100)/(2/(9**0.5))
print(zhesap)
#burada çizeceğim normal dağılım şeyinde iki kuyruk boyalı olacak o zaman benim bu z hesap değerimiz #
#o alanlarınn içindemi değilmi diye kontrol etmem laızm
#o değeri bulalım
#o değer yani 0.025 alanlara uçlardan gelen değer 
q=1.96#negatifi diğer taraf
#bu durumda 
if zhesap>q:
    print("ho red edililir yani vidaların boyları 100 e eşit değildir")
else:
    print("h0 red edilemez")
#basitçe bu böyleydi ama bunun devamı var bu sadece giriş kısmı olduğundan devamı gelecektir 
