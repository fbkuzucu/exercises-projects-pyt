def gs(satir):

    satir = satir[:-1]

    satir2 = satir.split(",")

    isim = satir2[0]

    takim = satir2[1]

    if (takim == "Galatasaray"):
        return isim + ":" + takim + "\n"

    else:
        return ""


def fb(satir):

    satir = satir[:-1]

    satir2 = satir.split(",")

    isim = satir2[0]

    takim = satir2[1]

    if (takim == "Fenerbahçe"):
        return isim + ":" + takim + "\n"

    else:
        return ""


def bjk(satir):

    satir = satir[:-1]

    satir2 = satir.split(",")

    isim = satir2[0]

    takim = satir2[1]

    if (takim == "Beşiktaş"):
        return isim + ":" + takim + "\n"
    else:
        return ""


gsliler = list()

with open("futbolcular.txt","r",encoding="utf-8") as liste:

    for a in liste:
        x = gs(a)

        if (x == ""):
            pass

        else:
            gsliler.append(x)

with open("gs.txt","w",encoding="utf-8") as gs:

    for a in gsliler:
        gs.write(a)

fbliler = list()

with open("futbolcular.txt", "r", encoding="utf-8") as liste:
    for a in liste:
        x = fb(a)

        if (x == ""):
            pass

        else:
            fbliler.append(x)

with open("fb.txt","w",encoding="utf-8") as fb:

    for a in fbliler:
        fb.write(a)

bjkliler = list()

with open("futbolcular.txt", "r", encoding="utf-8") as liste:
    for a in liste:
        x = bjk(a)

        if (x == ""):
            pass

        else:
            bjkliler.append(x)

with open("bjk.txt","w",encoding="utf-8") as bjk:
    for a in bjkliler:
        bjk.write(a)







