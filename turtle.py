"""from math import pi

raadius = 60.25

print('Ümbermõõt on ', round(pi * 2 * raadius, 2), ' cm')
print('Pindala on ' + str(round(pi * (raadius ** 2), 2)) + ' cm2')

x= 'a'
y= 'b'
z = 1
w = 2
print(x+y)
print(x + str(z))
print(z + w)


print(x * w)
print('see on' + x)
print('see on', x)
print('see on', raadius)
print('see on' + str(raadius))

#nimi = input('Palun ütle, mis on sinu nimi: ')


s = 'abc'
print(len(s))
print(len(s+str(2))*2)
print(s[1],s[2],s[0])
print(s[1]+ s[2] + s[0])
print(s.upper()*3)
print(s.replace('a','d'))
s=s.replace('a','c').upper()
print(s)

f = open('test.txt')
nimi = f.readline().strip()
vanus = f.readline().strip()
aadress = f.readline().strip()

print("Nimi:", nimi)
print("Vanus:", vanus, "aastat")
print("Aadress:", aadress)

f.close()



f = open('test.txt')
print(f.read().upper().strip())

f.close()

nimi = input("nimi: ")
f = open("test.txt", "w")
f.write(nimi + '\n') #erinevalt print käsust ei tekita faili meetod write automaatselt reavahetust. "
               #Selleks, et saada eri andmeid eri ridadele, lisasime reavahetuse sümboli käsitsi.
f.close()


f = open('test.txt')
print(f.read().upper().strip())

f.close()

a1 = int(input("Arv:"))
a2 = int(input("arv: "))
if a1%a2==0:
    print("jagus")
else:
    print("ei jagunud")
print("aitäh")


kas_eurodeks =input("Kas eurodeks? Y/N")
summa = float(input("summa:"))

if kas_eurodeks == "Y":
    tagasi= summa/15.5
    valuuta = "€"
else:
    tagasi= summa*15.5
    valuuta = "krooni"
print("siin on teie raha", round(tagasi), valuuta)

from random import randint
arv = randint(1, 3)
arvamus = int(input("paku number: "))

while arv != arvamus:
    if arv > arvamus:
        print("arvuti arv oli suurem")
    else:
        print("arvuti arv oli väiksem")
    arvamus = int(input("paku uus number: "))
print("tubli, ära arvasid")
print(arv, "oli arvuti number")

vastus = int(input("kui vanaks sa said? "))
while vastus != 35:
    if vastus < 35:
        print("no kuule...")

    else:
        print("nii vana sa ka ei ole!")
    vastus = int(input("aga tegelt? "))
print("ooo, lahe, palju õnne")


# välimine tsükkel teeb ühe korduse iga rea jaoks
rea_nr = 1
while rea_nr < 10:

    # sisemine tsükkel genereerib arvud käesolevasse ritta
    veeru_nr = 1 # iga uue rea puhul alustame jälle veerust nr. 1
    while veeru_nr < 10:
        korrutis = rea_nr * veeru_nr
        print((str(korrutis)).rjust(2) + " ", end="") # end="" abil väldime väljundisse reavahetuse panemist

        # suurendame veeru numbrit
        veeru_nr += 1

    # reavahetuse paneme alles siis, kui kõik käesoleva rea numbrid on väljastatud
    print()

    # suurendame rea numbrit
    rea_nr += 1
"""

a1 = (1 == 2 and 4 == 2)
a2 = (1 < 2 and 4 > 2)
a3 = (1 == 2 and 4 > 2)
a4 = (1 == 2 or 4 > 2)
a5 = (1 == 2 or 4 == 2)
a6 = (1 < 2 or 4 > 2)
print(a1, a2, a3, a4, a5, a6)


a = ['a', 'b', 'c']
print("b" in a)
"""
Paarisarvude loendamine
Kirjuta funktsioon, mis võtab argumendiks täisarvude listi ning tagastab, kui mitu elementi antud listis olid paarisarvud.

Testi oma funktsiooni erinevate listidega (sh tühja listiga).
"""

def paaris_arvud(arvud):
    paaris = []
    for arv in arvud:
        if arv % 2 == 0:
           paaris = paaris + [arv]
    return paaris
print(paaris_arvud([1, 3, 4, 6, 7, 9, 8, 0]))


"""
2. Ruudud
Kirjuta programm, mis küsib sisendiks täisarvu ning väljastab for-tsükli abil 
kõikide arvude ruudud alates 1-st kuni sisestatud arvuni (kaasaarvatud) ja lõpuks ka kõigi nende ruutude summa.

arv = int(input("Täisarv palun: "))
i = 1
summa = 0
while i <= arv: # for i in range (1, arv +1)
    print(i, "ruut on", i ** 2)
    summa += i ** 2
    i += 1


print("ruutude summa on", summa)
"""

from operator import add, sub
d = {
    'add' : add,
    'sub' : sub
}
print(d.get('mul', add)(5, 4))