import pandas as pd
veri=pd.DataFrame(pd.read_excel("dosya uzantısı",usecols=["sutun1","sutun2"]))
#bu yapıu bize sutun bir ve sutun ikiyi okur sutun adları tabikide farklı olabilir
veri.describe()#tanımlayıcı istetislikleri verecektir
veri.std()
veri.mean()
veri.medyan()
veri.mod()
veri.quantile(q=0.25)
veri.var()#varyans
veri.kurtosis()#basıklık
veri.skew()#çarpıklık
#15-16.videodan not çıkartılacak 