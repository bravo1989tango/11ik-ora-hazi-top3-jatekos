import random

neve = input("\nKérem a nevét: ")
probak_szama = 0
nehezseg = input("\nKérem válasszon nehézségi szintet (könnyű, közepes, nehéz): ")
eletek_szama = 0

with open("legjobbak.txt", "r") as rekord:
    lista = rekord.read().splitlines()
    print(lista)

if nehezseg == "könnyű":
    eletek_szama = 20
    szam = random.randint(1, 5)
elif nehezseg == "közepes":
    eletek_szama = 10
    szam = random.randint(1, 10)
elif nehezseg == "nehéz":
    eletek_szama = 5
    szam = random.randint(1, 20)
else:
    print("Nem értem.")

for i in range(eletek_szama):
    tipp = int(input("Kérem tippeljen: "))
    probak_szama += 1
    if tipp == szam:
        print("Eltaláltad! Valóban " + str(szam) + " a keresett szám!")
        if len(lista) == 3:
            with open("legjobbak.txt", "r") as rekord:
                adat = rekord.readlines()
                nevek = []
                pontok = []
                for sor in adat:
                    nevekpontok = sor.split()
                    nevek.append(nevekpontok [0])
                    pontok.append(nevekpontok[1])
                pontok = [int(i) for i in pontok]
                if max(pontok) > probak_szama:
                    maxindex = pontok.index(max(pontok))
                    with open("legjobbak.txt", "w") as rekord:
                        adat[maxindex] = neve + " " + str(probak_szama) + "\n"
                        rekord.writelines(adat)
                    break
        elif len(lista) < 3:
            with open("legjobbak.txt", "a") as rekord:
                lista = rekord.write(neve + " " + str(probak_szama) + "\n")
        break
    else:
        print("Nem sikerült! Még " + str(eletek_szama-(i+1)) + " életed maradt!")



#max 3 eredmény legyen a txt-ben, legkisebb szám a nagyobb! felülirja a kisebb érték
#név és szám is legyen

'''
Csaba : 2 
Laci : 5        Igy lehet elválasztásokkal beolvasni a pontokat
Tibi : 7
'''