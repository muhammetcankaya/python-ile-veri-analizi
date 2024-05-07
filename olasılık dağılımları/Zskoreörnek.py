import numpy as np
import matplotlib.pyplot as pyt 
import random
import seaborn as sns

np.random.seed(0)# bu yaptığım şey bir random işlem yaptığımda onu kaydeder tekrarlanmasına engel olur
veri1=np.random.normal(35,2,40000)
veri=(veri1-np.mean(veri1))/np.std(veri1)#bu satır ssayesinde bunu z skora çevirdim 
#üstteki satırı kaldırıp veri1 yerine veri yazarsan z skorsuz normal dağılım grafiği olur 
#standart normal dağılım değilde normal dağılım olur
sns.displot(veri,kde=True)
pyt.title("Veri dağılım grafiği",fontsize=15,loc="right",c="black")
pyt.xlabel("Veriler",fontsize=15,c="black")#x kordinatına isim yazdık
pyt.ylabel("frekans",fontsize=15,c="black")#y kordinatına isim yazdık fonstsize boyut c renk 
pyt.axvline(x=np.mean(veri),linestyle="-",c="red",linewidth=2.5,label="ortalama")
#aslında burada çağıtığım şey dikey çizgi cek o yüzden x ekseni kullandım e nereye çekecek tam ortaya çekeceğinden verinin ortalamasını ilk parameetre 
#olarak verdim devamıda renk çizginin stili kalınlığı gibi spesifik şeyler label da kenarda açıklama yazsın diye
pyt.axvline(x=np.mean(veri)-np.std(veri),linestyle="-",c="black",linewidth=2.5,label="ortalama-1 standart sapma")
pyt.axvline(x=np.mean(veri)+np.std(veri),linestyle="-",c="black",linewidth=2.5,label="ortalama+1 standart sapma")
pyt.axvline(x=np.mean(veri)-2*np.std(veri),linestyle="-",c="black",linewidth=2.5,label="ortalama-2 standart sapma")
pyt.axvline(x=np.mean(veri)+2*np.std(veri),linestyle="-",c="black",linewidth=2.5,label="ortalama+2 standart sapma")
pyt.legend()
pyt.show()


