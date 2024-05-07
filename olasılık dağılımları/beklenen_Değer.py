from scipy import stats
#kesikli olasılık dağılımı
x=[1,2,3,4,5,6]
y=[1/6,1/6,1/6,1/6,1/6,1/6]

beklenendeğer=stats.rv_discrete(values=([x],[y])).expect()
print(beklenendeğer)
#values yapusunu kullarak yapmamız gerekmektedir expect dediğim kısım sayesinde de
#bu beklenen değeri hesapladı yani kısaca beklenen değer hesaplarken kesikli olasılık yapısında bu kullanılır
#başka örnek yapabiliriz bunu üç kere yazı tura oynamakta tura gelme durumunun beklenen değerini hesaplayabiliriz
#SÜREKLİ DEĞİŞKEN İÇİN###
#BU YAPIDA DİREKT İNTEGRAL ALSAKTA OLUR
import scipy.integrate

def f(x):
    return (3/7)*x**3

beklenendeg=scipy.integrate.quad(f,1,2)
print(beklenendeg)
#Buda bu kadar basiit aslında bu yapıların hepsi aklında kalmayacak ama dönüp bakabileceksin istediğin zaman