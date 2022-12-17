def beolvas(fajl):
    f = open(fajl, "r", encoding="utf-8")
    fejlec = f.readline().strip()
    print(fejlec)
    sorok = f.readlines()
    f.close()
    feldolgozas(sorok)
    print(f"Csapatok száma: {len(csapatok)}")



stadionok = []
varosok = []
csapatok = []
elso_merkozes = []
utolso_merkozes = []

def feldolgozas(sorok):
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split(";")
        stadionok.append(sor[0])
        varosok.append(sor[1])
        csapatok.append(int(sor[2]))
        elso_merkozes.append(sor[3])
        utolso_merkozes.append(sor[4])
        i += 1



def NewYork():
    i = 0
    while len(varosok) > i:
        if varosok[i] == "New York":
            print(f"a stadion neve: {stadionok[i]}")
            print(f"\ta stadion helyszínének városa: {varosok[i]}")
            print(f"\ta stadionnak hányas csapata: {csapatok[i]}")
            print(f"\tmikor léptek előszőr pályára: {elso_merkozes[i]}")
            print(f"\tmikor léptek utoljára pályára: {utolso_merkozes[i]}")
        i += 1



