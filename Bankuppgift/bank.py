
#Variabler 
saldo = 1000                # Startvärde på 1000 kr
transaktioner = []          # Lista som lagrar transaktioner 
transaktioner.append(1000)  # Startvärde på 1000 kr


# programloop
while True:

    meny = ( "\n"
             "\n #Bank & Meny"
             "\n # Saldo {} kr"
             "\n"                                              #BÖRJA PÅ 6.1
             "\n 1. Visa saldo"
             "\n 2. Gör en insättning"
             "\n 3. Gör ett uttag"
             "\n 0. Avsluta program"
             "\n Gör ditt val:".format(saldo))

    val = int(input(meny))

    if val == 0:
        break
    elif val == 1:
        line = 0
        sum = 0
        head = ("\nAlla transaktioner:"                                               #Transaktioner skrivs ut med rubriker
                "\n{:>3} {:>12} {:>12}"
                "\n_____________________________").format("Nr", "Händlese", "Saldo")
        print(head)
        for t in transaktioner:
            line += 1
            sum += t
            print("{:>2}. {:>9} kr {:>9} kr".format(line, t, sum))
    elif val == 2:
        insättning = int(input("Ange din summa: "))
        if insättning >= 0:                               # Summan måste vara större än 0
            saldo += insättning                           # Lägger till insättning i saldo
            transaktioner.append(insättning)              # 
        else:
            print("Kan inte skriva negativa summor")
    elif val == 3:                                        
        uttag = int(input("Ange din summa: "))            
        if uttag <= saldo and uttag >= 0:                 # Summan behöver vara större än 0
            saldo -= uttag                                # Tar bort summan i uttag från saldo
            transaktioner.append(-uttag)
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
