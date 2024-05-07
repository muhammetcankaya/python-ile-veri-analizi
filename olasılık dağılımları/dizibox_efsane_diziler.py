import requests
from bs4 import BeautifulSoup
import re
import time
import textwrap
class Efsanediziler:
    def __init__(self):
        self.dongu=True
    def program(self):
        secim=self.menu()
        if secim=="1":
            print("Efsane diziler çağırılıyor..")
            time.sleep(2)
            self.dizisimleri()
        if secim=="2":
            #time.sleep(2)
            self.dizihikayesi()
        if secim=="3":
            print("Çıkıs yapılıyor...")
            time.sleep(2)
            self.cıkıs()
    def menu(self):
        
        def kontrol(secim):
            if not re.search("[1-3]",secim):
                raise Exception("Lütfen 1 ve 3 arasında bir sayı giriniz")
            elif (len(secim))!=1:
                raise Exception("Lütfen 1 ve 3 arasında bir sayı giriniz")
        while True:
            try:
                secim=input("""------------------EFSANE DİZİLER------------------\n[1]Efsae dizi isimlerini görmek için 1'e basınız\
                            \n[2]Dizilerden biri hakkında bilgi için 2'ye basınız\n[3]Çıkmak için 3'e basınız\n\n""")
                kontrol(secim)


            except Exception as hata:
                print(hata)
            else:
                break
        return secim
    def dizisimleri(self):
        url=requests.get("https://yabancidiziizle.pro/trendler-hd-izle").content
        soup=BeautifulSoup(url,"html.parser")
        diziler=soup.find("table",{"class":"ui inverted unstackable table"}).find("tbody").find_all("tr")

        for dizismi in diziler:
            print(dizismi.find("td",{"class":"details"}).find("a").string)
    def dizihikayesi(self):
        url=requests.get("https://yabancidiziizle.pro/trendler-hd-izle").content
        soup=BeautifulSoup(url,"html.parser")
        diziler=soup.find("table",{"class":"ui inverted unstackable table"}).find("tbody").find_all("tr")
        diziİD=list()
        dizilink=list()
        for dizismi in diziler:
            diziİD.append(dizismi.find("td",{"class":"details"}).find("a").string.lower())
        for dizilınk in diziler:
            dizilink.append(dizilınk.find("td",{"class":"details"}).find("a").get("href"))
        kaynak=dict(zip(diziİD,dizilink))
        while True:
            try:
                hangidizi=input("Araştırmak istediğiniz diziyi yazınız").lower()
                dizi_sitesi=requests.get(kaynak[hangidizi]).content
                soup2=BeautifulSoup(dizi_sitesi,"html.parser")
                dizi_tür=soup2.find("div",{"class":"genre-item"}).find_all("a")
                print("Tür:")
                for i in dizi_tür:
                    x=i.string
                    print("--"+x)
                oyuncular=soup2.find("div",{"class":"ui middle aligned divided list"}).find_all("div",{"class":"item"})
                print("Oyuncular:")
                for x in oyuncular:
                    karakter_ismi=x.find("div",{"class":"content"}).find("div").string.upper()
                    gerçek_ismi=textwrap.fill(x.find("div",{"class":"content"}).find("h5").string).upper()
                    print(f"{karakter_ismi} ,{gerçek_ismi}")
                
                print("Hikaye:"+textwrap.fill(soup2.find("p",{"id":"tv-series-desc"}).find("div",{"class":"modal-body"}).text))
                self.menudon()
            except Exception:
                print("Lütfen envanterde olan bir film giriniz")



    def cıkıs(self):
        self.dongu=False

cagırma=Efsanediziler()
while cagırma.dongu:
    cagırma.program()
