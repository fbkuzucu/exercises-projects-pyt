from süpermarket import *

print("""**************

Süpermarket varitabanına hoşgeldiniz!Yapılan işlemler:

1-Ürünleri Göster

2-Ürün Ekle

3-Ürün Sorgula

4-Ürün Sil

5-Ürünlerin Birim Fiyatlarının Toplamı

6-Adet Azaltma

Çıkmak için "q" tuşuna basınız...

**************""")

supermarket = Supermarket()

while True:
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz:")

    if (islem == "q"):
        print("veritabanından çıkılıyor...")
        time.sleep(2)
        break

    elif (islem == "1"):
        print("ürünleriniz gösteriliyor lütfen biraz bekleyin...")
        time.sleep(2)
        supermarket.urunlerigoster()

    elif (islem == "2"):
        isim = input("lütfen ürünü giriniz:")
        tür = input("lütfen ürünün türünü giriniz:")
        fiyat = float(input("lütfen ürünün birim fiyatını giriniz:"))
        birim = int(input("lütfen ürünün adetini giriniz:"))
        skt = input("lütfen ürünün son kullanma tarihini giriniz:")

        x = Ürün(isim,tür,fiyat,birim,skt)
        supermarket.urunekle(x)

    elif (islem == "3"):
        isim = input("lütfen sorgulamak istediğiniz ürünün ismini giriniz:")
        print("ürününüz sorgulanıyor lütfen biraz bekleyiniz...")
        time.sleep(2)
        supermarket.urunsorgula(isim)

    elif (islem == "4"):
        isim = input("lütfen silmek istediğiniz ürünün ismini giriniz:")
        print("ürününüz siliniyor...")
        time.sleep(2)
        supermarket.urunsil(isim)

    elif (islem == "5"):
        print("ürünlerin fiyatı toplanıyor lütfen biraz bekleyiniz...")
        x = supermarket.fiyatoplami()


    elif (islem == "6"):
        ürün = input("hangi ürünün adedini azaltmak istiyorsunuz:")
        print("adet azaltılıyor lütfen biraz bekleyiniz...")
        time.sleep(2)
        supermarket.adetazalt(ürün)

    else:
        print("geçersiz işlem")


