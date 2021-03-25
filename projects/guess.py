import random
import time


print("""lalalalalalallalal




"sayi tahmin etme oyununa hosgeldiniz"




lalalalalalalalal""")

rastgele_sayi = random.randint(1 , 41)
tahminhakki = 3



while True:

    tahmin = int(input("lutfen tahmininizi giriniz:"))

    if (tahmin < rastgele_sayi):
        print("bi sn")
        time.sleep(1)
        print("biraz yukselt")

        tahminhakki  -= 1
        print("tahmin hakkin",tahminhakki)


    elif(tahmin > rastgele_sayi):
        print("bi sn")
        time.sleep(1)
        print("biraz dusur")

        tahminhakki  -= 1

        print("tahmin hakkin", tahminhakki)


    else:

        print("bi sn...")
        time.sleep(1)
        print("tebrikler", rastgele_sayi)
        break

    if (tahminhakki == 0):
        print("tahmin hakkin bitti...")
        break

print("Tahmin etmen gereken sayı:",rastgele_sayi)