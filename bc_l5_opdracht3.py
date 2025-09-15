from random import randint

score = 0
for _ in range(3):
    te_raden = randint(1,5)
    pogingen = 0
    while True:
        gok = int(input('Kies een getal van 1 t/m 5: '))
        pogingen += 1
        if te_raden == gok:
            print("Je hebt het getal goed geraden!")
            break
        else:
            print("Niet goed, probeer opnieuw.")
    score += 20 - (pogingen - 1)

print("Je totale score is:", score)
