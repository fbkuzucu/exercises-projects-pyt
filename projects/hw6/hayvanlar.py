class hayvanlar():

    def __init__(self,beslenme,hareket_bicimi,tur,ureme_sekli,iskelet_sekli,boy,uzuv):

        self.beslenme = beslenme
        self.hareket_bicimi = hareket_bicimi
        self.tur = tur
        self.ureme_sekli = ureme_sekli
        self.iskelet_sekli = iskelet_sekli
        self.boy = boy
        self.uzuv = uzuv
    def bilgilerigosterme(self):

        print("beslenme: {}\nhareket bicimleri: {}\ntur: {}\nureme sekli: {}\niskelet: {}\nuzuv: {}\nboy: {}".format(self.beslenme,self.hareket_bicimi,self.tur,self.ureme_sekli,self.iskelet_sekli,self.uzuv,self.boy))

    def __len__(self):

        return self.boy



class kuslar(hayvanlar):

    def farklibilgiler(self):

        print("en agir sinek kuslari 24 gram civarindadir")
        print("kartallar yalniz ucar")
        print("kuslar basinca dayali bir prensibe gore ucarlar.")

class kopekler(hayvanlar):

    def farklibilgilerv2(self):

        print("kopeklerin 328 farkli irki vardir")
        print("en sadik hayvanlar arasindadir")
        print("dunyada 400m kopek oldugu tahmin ediliyor")

class atlar(hayvanlar):


    def farklibilgilerv3(self):

        print ("dortnal rekoru 70 kmdir")
        print ("arap ingiliz belcika ve midilli atlari populerdir")
        print ("omru 20-30 sene arasindadir")

kus = kuslar("etcil","ucarak","kartal,kanarya,baykus,akbaba,karga","yumurtlama","omurgali","orta boy","2 kanat,2 ayak")
kus.bilgilerigosterme()
kus.farklibilgiler()




kopek = kopekler("etcil","kosarak","shuba inu,golden,kanish,kangal,av","dollenme","omurgali","kangallar en uzunlarindandir","4 ayak")
kopek.bilgilerigosterme()
kopek.farklibilgilerv2()




at = atlar("etcil,otcul","depar","arab,belcika,midilli,unicorn","dollenme","omurgali","2.4m","4 ayak")
at.bilgilerigosterme()
at.farklibilgilerv3()



