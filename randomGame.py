import random
import math

failas = open('reg.txt', 'w')

skaiciusNuo = int(1)

skaiciusIki = int(input("iveskite iki kurio skaiciaus: "))

x = random.randint(skaiciusNuo, skaiciusIki)
print("\n\tLiko ",
        round(math.log(skaiciusIki - skaiciusNuo + 1, 2)),
        " spejimu!")

count = 0


failas.write('Vartotojas ivede skaiciu: ')
failas.write(str(skaiciusIki))
failas.write('\n')
failas.write('Sugeneruotas atsitiktinis skaicius: ')
failas.write(str(x))
failas.write('\n')

while count < math.log(skaiciusIki - skaiciusNuo + 1, 2) :
    count += 1

    spejimas = int(input("Spekite skaiciu: "))

    failas.write(str(count))
    failas.write(' spejimu vartotojas ivede ')
    failas.write(str(spejimas))
    if x > spejimas:
        failas.write('. Atsakymas – sugeneruotas skaicius didesnis')
    else:
        failas.write('. Atsakymas – sugeneruotas skaicius mazesnis')
    failas.write('\n')
    if x == spejimas:
        print("Sveikinu, atspejote per ", count, " spejimu(s)")

        break
    elif x > spejimas:
        print("Jusu spejamas skaicius per mazas! Bandykite dar karta")
    elif x < spejimas:
        print("Jusu spejamas skaicius per didelis! Bandykite dar karta")

if count >= math.log(skaiciusIki - skaiciusNuo + 1, 2):
    print("\nSkaicius buvo %d" % x)
    print("\tSekmes kita karta!")


