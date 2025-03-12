'''1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
'''
nyelvek = []

with open ('Timeline_of_ programming_languages.txt', 'r', encoding="utf-8") as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv = adatok[1]
        evszam = adatok[0]
        nyelvek.append([nyelv, evszam])

for nyelv in nyelvek:
    print(nyelv)

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
        print('Ez kerül a fájlba...', file=celfajl)  
        for adatok in celfajl:
            print(adatok.strip(), file=celfajl)
