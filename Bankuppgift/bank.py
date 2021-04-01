
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
        if insättning >= 0:
            saldo += insättning 
        else:
            print("Kan inte skriva negativa summor")
    elif val == 3:                                        # Fortsätt på 4.5, summan behöver vara större än 0
        uttag = int(input("Ange din summa: "))          
        if uttag <= saldo:
            saldo -= uttag
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
