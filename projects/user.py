

print("""***************


asiri gizli sisteme girme sekansi



*******************""")

sys_kullaniciadi = "fbk"

sys_parola = "12"

giris_sayisi = 3

while True :
    user = input("kullanici adi :")

    password = input("sifre girin:")

    if (user != sys_kullaniciadi and password == sys_parola):
        print("kullanici adiniz hatali")
        giris_sayisi -= 1

    elif (user == sys_kullaniciadi and password != sys_parola):
        print("sifre hatali")
        giris_sayisi -= 1

    elif (user != sys_kullaniciadi and password != sys_parola):
        print("hepsi yanlis")
        giris_sayisi -= 1

    else:
        print("artik ulkeyi kurtarabilirsiniz :d")

        break

    if (giris_sayisi == 0):
        print("baska bir zaman baska bir yerde belki girebilrsiniz ama şimdi degil...")
        break
