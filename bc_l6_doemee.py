# we gaan aan de lijst met getallen 
# het getal 6 tevoegen en dan alles optellen
getallen = [1, 2, 3, 4, 5]

som =sum(getallen)
print(som)


# we gaan checken of in deze lijst met sporten
# een bepaalde sport zit en welke indec die heeft
sporten = ["voetbal", "basketbal", "tennis", "zwemmen", "honkbal", "volleybal", "atletiek"]

i = sporten.index("basketbal")
print(i)

# we gaan uit de volgende lijst met autos 1 halen en tonen
# en dan de rest sorteren
autos = ['BMW', 'Audi', 'Ford', 'Volvo']



lijst = []

for aantal in range(6):
    getal = int(input("geef een getal"))
    lijst.append(getal)
    print(lijst)