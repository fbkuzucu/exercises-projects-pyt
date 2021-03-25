def nothesapla(satir):


    satir = satir[:-1]

    liste2 = satir.split(",")

    isim = liste2[0]

    not1 = int(liste2[1])

    not2 = int(liste2[2])

    not3 = int(liste2[3])

    son_not = (not1 * (0.3)) + (not2 * (0.3)) + (not3 * (0.4))

    if (son_not >= 90):
        harf = "AA"

    elif (son_not >= 85):
        harf = "BA"

    elif (son_not >= 80):
        harf = "BB"

    elif (son_not >= 75):
        harf = "CB"

    elif (son_not >= 65):
        harf = "CC"

    elif (son_not >= 60):
        harf = "DC"

    elif (son_not >= 55):
        harf = "DD"

    elif (son_not >= 50):
        harf = "FD"

    else:
        harf = "FF"


    return isim + "------>" + harf +"\n"


with open("liste.txt","r",encoding= "utf-8") as liste:

    eklenecekler = list()

    for a in liste:

        eklenecekler.append(nothesapla(a))

    with open("notlar.txt","w",encoding= "utf-8") as notlar:
        for x in eklenecekler:
            notlar.write(x)

        