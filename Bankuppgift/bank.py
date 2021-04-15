
#Variabler 
saldo = 1000              # startvärde på 1000 kr


# programloop
while True:

    meny = ( "\n"
             "\n #Bank"
             "\n #Meny"
             "\n"
             "\n 1. Visa saldo"
             "\n 2. Gör en insättning"
             "\n 3. Gör ett uttag"
             "\n 0. Avsluta program"
             "\n Gör ditt val:")

    val = int(input(meny))

    if val == 0:
        break
    elif val == 1:
        print(f"Saldot är: {saldo}kr")      #printar saldo
    elif val == 2:
        insättning = int(input("Ange din summa: "))
        if insättning >= 0:                               # Summan måste vara större än 0
            saldo += insättning                           # Lägger till insättning i saldo
        else:
            print("Kan inte skriva negativa summor")
    elif val == 3:                                        
        uttag = int(input("Ange din summa: "))            
        if uttag <= saldo and uttag >= 0:                 # Summan behöver vara större än 0
            saldo -= uttag                                # Tar bort summan i uttag från saldo
        elif uttag <= 0:
            print("Uttaget kan inte vara negativt")
        else:
            print("Du har inte tillräckligt med pengar, sorry mate.")
    else: 
        print("Felaktigt val")
    
print("Tack för ditt besök")
    # visa saldo 
    # gör en insättning 
    # gör ett uttag 
    # avsluta programmet
# fil att lagra transaktioner 
