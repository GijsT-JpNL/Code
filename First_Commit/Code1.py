import random

while True:
    command = input("Typ 'generate' om een getal te genereren of 'stop' om te stoppen: ")
    
    if command.lower() == "generate":
        number = random.randrange(1, 100)
        print(f"🎲 Je willekeurige getal is: {number}")
    elif command.lower() == "stop":
        print("Programma gestopt. Tot de volgende keer!")
        break
    else:
        print("Ongeldig commando. Typ 'generate' of 'stop'.")