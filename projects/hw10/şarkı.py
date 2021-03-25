import sqlite3
import time
from functools import reduce

class Şarkı():

    def __init__(self,isim,sanatçı,albüm,prodüksiyon_şirketi,süre):

        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.süre = süre

    def __str__(self):

        return "Şarkı: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nSüre: {}".format(self.isim,self.sanatçı,self.albüm,self.prodüksiyon_şirketi,self.süre)


class Şarkılar():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarkilar.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "create table if not exists playlist (isim TEXT, sanatçı TEXT , albüm TEXT, şirket TEXT , süre FLOAT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def sarkilarigoster(self):

        sorgu = "select * from playlist"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("şu an çalma listenizde şarkı bulunmuyor...")

        else:
            for a in sarkilar:
                sarki = Şarkı(a[0],a[1],a[2],a[3],a[4])
                print(sarki)


    def sarkiekle(self,sarki):

        sorgu = "insert into playlist values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatçı,sarki.albüm,sarki.prodüksiyon_şirketi,sarki.süre))
        self.baglanti.commit()

    def sarkisorgulama(self,sarki):

        sorgu = "select * from playlist where isim = ?"
        self.cursor.execute(sorgu,(sarki,))
        sarki = self.cursor.fetchall()

        if (len(sarki) == 0):
            print("böyle bir şarkı çalma listenizde bulunmamaktadır...")

        else:
            x = Şarkı(sarki[0][4],sarki[0][1],sarki[0][2],sarki[0][3],sarki[0][4])
            print(x)


    def sarkisil(self,isim):

        sorgu = "delete from playlist where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()


    def toplamsüre(self):

        sorgu = "select süre from playlist "
        self.cursor.execute(sorgu)
        süreler = self.cursor.fetchall()

        x = reduce(lambda x,y: x+y,süreler)
        y= reduce(lambda a,b:a+b,x)
        print(y)




