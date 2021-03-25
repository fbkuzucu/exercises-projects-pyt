baş_harfler = " "
with open("şiir.txt","r",encoding="utf-8") as siir:

    for satir in siir:
          baş_harfler += satir[0]

    print(baş_harfler)



