import time

class bilgisayar():

    def __init__(self,marka = "apple",model = "macbook pro" ,ram = 8,islemci = "intel i5",ekran_karti = "intel",cekirdek_sayisi = 4,fiyat = 10000,renk = "gri",harddisk = 128):

        self.marka = marka
        self.model = model
        self.islemci = islemci
        self.ekran_karti = ekran_karti
        self.cekirdek_sayisi = cekirdek_sayisi
        self.fiyat = fiyat
        self.ram = ram
        self.renk = renk
        self.harddisk = harddisk

    def bilgilerigoster(self):

        print("""
        
        markasi = {}
        
        modeli = {}
        
        ram = {} gb
        
        islemci = {}
        
        ekran karti = {}
        
        cekirdek sayisi = {}
        
        fiyati = {} tl
        
        renk = {}
        
        harddisk = {} gb ssd
        
        """.format(self.marka,self.model,self.ram,self.islemci,self.ekran_karti,self.cekirdek_sayisi,self.fiyat,self.renk,self.harddisk))

    def zam(self):

        zam_miktari = int(input("lutfen urunun fiyatina ek mudaheleyi yapiniz:"))
        self.fiyat += zam_miktari
        print("ekonomik sebeplerden dolayi bu bilgisayarin yeni fiyati {} tl'dir.".format(self.fiyat))


    def renk_degistir(self,):

        yeni_renk = input("lutfen istediginiz rengi yaziniz:")
        self.renk = yeni_renk
        if (yeni_renk == "uzay grisi"):
            self.fiyat += 3000

        else:
            print("bu renk bu modelde mevcut degildir.")


    def ram_degistirme(self):

        x = int(input("lutfen ram kapasitenizin kac gb olmasini istersiniz? :"))

        if (x == 16):
            self.ram = x
            self.fiyat += 4000

        elif (x == 32):
            self.ram = x
            self.fiyat += 8000

        else:
            print("bu model 32 gb den fazla kapasitesi olan ram desteklemez.")


    def newmodel(self):

        y = input("lutfen degistirmek istediginiz modeli yaziniz:")

        if (y == "macbook"):

            self.model = y
            self.ekran_karti = "islemci ile butundur"
            self.fiyat -= 3000
            self.islemci = "intel m"

        elif (y == "macbook air"):

            self.model = y
            self.fiyat -= 1500

        else:
            print("windows kullanan bilgisayarlar mevcut degildir.")


    def __len__(self):

        return self.harddisk

    def __del__(self):
        print ("girdiginiz model bilgileri silinmistir.")


comp = bilgisayar()


print("""

apple yardimci modulune hosgeldiniz! secebileceginiz islemler:

*** cikis yapmak icin 0'a basiniz... ***

1- mevcut bilgileri gosterme

2- ekonomik dalgalanmalara karsi onlem

3- renk degistirme

4- ram degistirme

5- model degistirme

6- harddisk boyutunu ogrenme

*** modulu kullandiktan sonra 7'e basarak girdiginiz bilgileri siliniz***

""")

while True:

    islem = int(input("lutfen yapmak istediginiz islemi giriniz:"))

    if (islem == 0):
        print("modulden cikis yapiliyor...")
        break

    elif (islem == 1):
        print("bilgileriniz gosteriliyor...")
        time.sleep(1)
        comp.bilgilerigoster()

    elif (islem == 2):
        comp.zam()

    elif (islem == 3):
        comp.renk_degistir()

    elif (islem == 4):
        comp.ram_degistirme()

    elif (islem == 5):
        comp.newmodel()

    elif (islem == 6):
        print(len(comp))

    elif (islem == 7):
        del comp

    else:
        print("gecersiz islem")









