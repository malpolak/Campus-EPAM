#zip function

imiona = ["Ania", "Bartek", "Jadzka", "Jan"]
punkty = [ 18, 2, 34, 54]

wyniki = list(zip(imiona, punkty)) #zmienic od razu na liste, zeby bylo mozna ponownie wykorzystac, bo po iteratorze mozna przejsc tylko raz

for imie,punkt in wyniki:
    print(f'{imie} zdobyla/zdobyl {punkty} punktow.')

print(wyniki)


wyniki_slownik = dict(zip(imiona, punkty))
print(wyniki_slownik)


produkty = ["chleb", "mleko", "jajka", "ser"]
ceny = [5.99, 3.49, 12.00, 8.50]
total = 0


oferta = list(zip(produkty, ceny))

for produkt, cena in oferta:
    if cena > 6:
        print(f'{produkt} kosztuje {cena} zł')

    total += cena

print(total)

posortowane = sorted(oferta, key = lambda x: x[1], reverse=True)
print(posortowane)


#map funcion
