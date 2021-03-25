x = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


def kactane():

    a = list()

    for b in x:
        a.append(b)

    kelimeler = dict()

    for c in a:

        if (c in kelimeler):
            kelimeler[c] += 1

        else:
            kelimeler[c] =  1

    for kelime,sayi in kelimeler.items():
        print("{} kelimesi {} defa geçmektedir".format(kelime,sayi))

        print("**************")


kactane()