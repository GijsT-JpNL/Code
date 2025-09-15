leeftijd = float(input("Wat is jouw leeftijd? "))
if leeftijd >= 18 and leeftijd == int(leeftijd):
    print("Gefeliciteerd, je mag je rijbewijs halen.")
elif leeftijd >= 16:
    print("Gefeliciteerd, je mag je brommerrijbewijs halen.")
else:
    print("Helaas, je zult nog even moeten wachten voor een rijbewijs.")
