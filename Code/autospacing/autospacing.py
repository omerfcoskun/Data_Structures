kaynak = open("source.c", "r")
hedef = open("target.c", "w")

satir = kaynak.readlines()
kaynak.close()

tab = 0

for i in range(0, len(satir)):

    if satir[i-1] == "{\n":
        tab += 1
    elif satir[i] == "}\n":
        tab -= 1
    else:
        pass

    for j in range(0,tab):
        hedef.write("\t")

    hedef.write(satir[i])

hedef.close()
