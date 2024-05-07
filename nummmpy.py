# import numpy as  np

# birim matris
# bir=np.ones((x,y),dtype=int) 
# int tipinde birim matris
# bir=np.ones((x,y),dtype=int)*10 bunu tahmin edebilirsin bence

# bunun için başka yöntem
# np.full((x,y),20,dype=int)

# birim matris
# birim=np.eye(5)
# 5*5lim birim matris

# np.diag([1,2,3,4,5])
# birim matrise benzer fakat köşegen elemeanları bu yazanlardır sırasıyla

 
# np.arange(0,100,5)
# 0 dan başlayarak 5 er artarak bir dizi oluşturur 100 dahil değil

# np.linspace(0,100,5)
# 0,25,50,75,100 çıktı buysa alarsın 100 dahil

# np.random.rand(x,y)
# random bir matris üretir
# np.random.randn(x,y) böyle üretirsek normal dağılıma uyar
# np.random.randint(0,10,size=(3,4))
# 0 ile 10 arasında sayılardan oluşan 3e 4lük bir matris oluştur 

# bir numpy dizinde istediğimiz diziye ulaşabliriz

# x=np.array([1,2,3,4,5,6,7,8,9])
# x[0] 0.indeksi verir
# x[-1] son değeri verir
# x[:3] baştan üç değer x[5:] baştan 5 değer tam tersi
# [::] tüm listeyi verir
# [::-1] terster verir
# burada da for dongüsü kullanarak değerleri döndürebilirz

# çok boyutlu dizi üzerinde işlem
# x=np.array([[1,2],[3,4],[5,6],[7,8]])
# x[0] ilk matrisin ilk satırı
# x[3] 4.satır
# x[0,1]  1.satırdaki 2.indeks
# x[:,0] 1. sutunu verir
# x[:,1] 2. sutunu verir

# listede uyguladığımız yapıların bazıları için numpy
# x=np.arange(11)
# 0-10 a birer artan dizi oluşturdu
# herhangi bir ixdekse erişim ve silme
# np.delete(x,[0,4]) x dizisinde sıfır ve 4. indeksi silmiş olduk
# iki boyutlu dizidede yapabilirz
# x=np.arange(16).reshape(4,4)
# 4*4 lük sıfırdan 16 ya biri matris
# np.delete(x,[0],axis=0)
# 1.satırı siler x matrisinde
# np.delete(x,[0],axis=1)
# bu sefer satırdan değilde sutundan siler

# x=np.arange(11) dizimiz bu olsun
# y=np.appand(x,500) bu diziye en sondan değer ekler

# x=np.arange(16).reshape(4,4)
#  matris üzerinde ekleme yapalım
# y=np.append(x,[[100,200,300]],axis=0)
# son satıra bu satırı eklemiş olduk
# axis=1 olursa bu sutuna ekleme yapmaktır
# y=np.append(x,[[100],[200],[300]],axis=1)
# sutun olarak ekleme yapacaksak bu şekilde yapı kullanmalıyız


# np.sort(x) küçükten büyüğe sıralar

# x=np.array([4,5,6,7,8,4])
# y=np.array([7,5,9,6,4,5])
# bunlar arasında toplama çıkarma çarpma bölme yapılır
# np.add(x,y) toplama
# np.subract(x,y) çıkartma

# np.min
# np.max
# np.sqrt
# np.log logaritma
# np.sum hepsini topla
# np.mean ortalama
# np.median medyan değer
# np.var varyans
# np.std standart çarpma

print("dnlkdfsk")
