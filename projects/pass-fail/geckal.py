def gec(satir):

    satir = satir[:-1]

    liste2 = satir.split(",")

    isim = liste2[0]

    not1 = int(liste2[1])

    not2 = int(liste2[2])

    not3 = int(liste2[3])

    son_not = (not1 * (0.3)) + (not2 * (0.3)) + (not3 * (0.4))

    if (son_not >= 50):
        return isim + "---" + "gecti" + "\n"
    else:
        return ""





def kal(satir):
    satir = satir[:-1]

    liste2 = satir.split(",")

    isim = liste2[0]

    not1 = int(liste2[1])

    not2 = int(liste2[2])

    not3 = int(liste2[3])

    son_not = (not1 * (0.3)) + (not2 * (0.3)) + (not3 * (0.4))

    if son_not < 50:
        return isim + "---------" + "kaldi" + "\n"

    else:
        return ""

gecenlerlistesi = list()

with open("liste.txt","r",encoding="utf-8") as liste:

    for x in liste:
        a= gec(x)

        if (a == ""):
            pass
        else:
            gecenlerlistesi.append(a)

with open("gecenler.txt","w",encoding="utf-8") as gecen:
    for a in gecenlerlistesi:
        gecen.write(a)


kalanlarlistesi = list()

with open("liste.txt","r",encoding="utf-8") as liste:

    for y in liste:
        a= kal(y)

        if (a == ""):
            pass

        else:
            kalanlarlistesi.append(a)

with open("kalanlar.txt","w",encoding="utf-8") as kalan:

    for b in kalanlarlistesi:
        kalan.write(b)









