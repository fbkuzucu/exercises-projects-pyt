from şarkı import *

print("""**************

Çalma Listenize Hoşgeldiniz! Lütfen Yapmak İstedğiniz İşlemi Seçiniz:

1-Şarkıları Göster

2-Şarkı Ekle

3-Şarkı Sorgula

4-Şarkı Sil

5-Listenin Toplam Süresini Hesapla

Listeden çıkmak için lütfen "q" tuşuna basınız

*************""")

liste = Şarkılar()

while True:

    islem = input("lütfen işlemi seçiniz:")

    if (islem == "q"):
        print("listeden çıkış yapıyorsunuz...")
        time.sleep(2)
        break

    elif (islem == "1"):
        print("şarkılarınız gösterilecek biraz bekleyiniz...")
        time.sleep(2)
        liste.sarkilarigoster()

    elif (islem == "2"):
        isim = input("lütfen şarkıyı giriniz:")
        sanatçı = input("lütfen sanatçıyı giriniz:")
        albüm = input("lütfen albümü giriniz:")
        şirket = input("lütfen prodüksiyon şirketini giriniz:")
        süre = float(input("lütfen şarkının süresini giriniz:"))

        song = Şarkı(isim,sanatçı,albüm,şirket,süre)
        liste.sarkiekle(song)

    elif (islem == "3"):
        şarkı = input("lütfen sorgulamak istediğiniz şarkının ismini giriniz:")
        print("şarkınız aranıyor...")
        time.sleep(2)
        liste.sarkisorgulama(şarkı)

    elif (islem == "4"):
        şarkı = input("lütfen silmek istediğiniz şarkının ismini giriniz:")
        x = input("ŞARKIYI SİLMEK İSTEDİĞİNİZE EMİN MİSİNİZ E/H:")

        if (x == "E"):
            print("şarkınız siliniyor...")
            time.sleep(2)
            liste.sarkisil(şarkı)

    elif (islem == "5"):
        print("çalma listenizin toplam süresi hesaplanıyor lütfen biraz bekleyiniz...")
        liste.toplamsüre()

    else:
        print("geçersiz işlem")


