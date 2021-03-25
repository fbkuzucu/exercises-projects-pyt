
with open("mailler.txt","r",encoding="utf-8") as mail:

    for satir in mail:
        satir=satir[:-1]
        if satir.endswith(".com") and satir.find("@") != -1:
            print(satir)














