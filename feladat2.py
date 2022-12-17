import random
def feladat2():
    szamok = []
    ketjegyuek_szama = []
    paros_osszege = 0
    paratlan_osszege = 0
    while len(szamok) < 13:
        szam = int(random.random()*191)-40
        szamok.append(szam)
        if (szam >= 10 and szam <= 99) or (szam <= -10 and szam >= -99):
            ketjegyuek_szama.append(szam)
        if szam % 2 == 0:
            paros_osszege += szam
        else:
            paratlan_osszege += szam
    if paros_osszege > paratlan_osszege:
            eredmeny = '>'
    else:
            eredmeny = '<'
    print(f'2. a) A lista: {szamok}')
    print(f'2. b) A kétjegyű számok száma: {len(ketjegyuek_szama)}')
    print(f'2. e) A párosok összege: {paros_osszege} {eredmeny} a páratlanok összege: {paratlan_osszege}')

