import sqlite3
import time
from functools import reduce

class Ürün():

    def __init__(self,isim,tür,fiyat,birim,skt):

        self.isim = isim
        self.tür = tür
        self.fiyat = fiyat
        self.birim = birim
        self.skt = skt

    def __str__(self):
        return "Ürün: {}\nTürü: {}\nFiyat: {}\nAdeti(kg,tane vb.): {}\nSon Kullanma Tarihi: {}".format(self.isim,self.tür,self.fiyat,self.birim,self.skt)


class Supermarket():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.connect = sqlite3.connect("süpermarket.db")
        self.cursor =  self.connect.cursor()
        sorgu = "create table if not exists supermarket(Ürün TEXT,Tür TEXT,Fiyat FLOAT,Birim INT, SKT TEXT)"
        self.cursor.execute(sorgu)
        self.connect.commit()

    def urunlerigoster(self):

        sorgu = "select * from supermarket"
        self.cursor.execute(sorgu)
        urunler = self.cursor.fetchall()

        if(len(urunler) == 0):
            print("Veritabanında ürün bulunmamaktadır...")


        else:
            for a in urunler:
                x = Ürün(a[0],a[1],a[2],a[3],a[4])
                print(x)

    def urunekle(self,ürün):

        sorgu = "insert into supermarket values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(ürün.isim,ürün.tür,ürün.fiyat,ürün.birim,ürün.skt))
        self.connect.commit()

    def urunsorgula(self,ürün):

        sorgu = "select * from supermarket where Ürün = ?"
        self.cursor.execute(sorgu,(ürün,))
        urunler = self.cursor.fetchall()

        if(len(urunler) == 0):
            print("Veritabanda böyle bir ürün bulunmuyor veya bittiği için silindi...")

        else:
            x = Ürün(urunler[0][0], urunler[0][1], urunler[0][2], urunler[0][3], urunler[0][4])
            print(x)

    def urunsil(self,ürün):

        sorgu = "delete from supermarket where Ürün = ?"
        self.cursor.execute(sorgu,(ürün,))
        self.connect.commit()

    def fiyatoplami(self):

        sorgu = "select Fiyat from supermarket"
        self.cursor.execute(sorgu)
        fiyatlar = self.cursor.fetchall()

        x = reduce(lambda a , b : a+b,fiyatlar)
        y = reduce(lambda a , b : a+b,x)
        print("şu an veritabanındaki ürünlerin toplamı {} tl'dir ".format(y))


    def adetazalt(self,isim):

        sorgu = "select * from supermarket where Ürün = ?"
        self.cursor.execute(sorgu,(isim,))
        ürünler = self.cursor.fetchall()

        if (len(ürünler)== 0):
            print("böyle bir ürün bulunmamaktadır...")

        else:
            adet = ürünler[0][2]
            adet -= 1

            sorgu2 = "update supermarket set Birim = ? where Ürün = ? "
            self.cursor.execute(sorgu2,(adet,isim))
            self.connect.commit()

