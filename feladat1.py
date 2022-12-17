def beker():
    i = 0
    hely = 0
    legkisebb_szam = 9999
    szamok = []
    while len(szamok) < 3:
        szam = int(input(f'Kérem a(z) {i + 1}. páros számot! '))
        while szam % 2 == 1:
            szam = int(input(f'Ez nem PÁROS!  Kérem a(z) {i + 1}. páros számot! '))
        szamok.append(szam)
        if legkisebb_szam > szam:
            legkisebb_szam = szam
            hely = i

        i += 1
    print(f'{hely + 1}. lépésben adta meg a legkisebb páros számot, melynek értéke: {legkisebb_szam}')