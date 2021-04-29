from functions import *


#Variabler 
check_file_exists()        # Kollar om filen finns, annars skapar den en 
read_file()
transactions.append(1000)  # Startvärde på 1000 kr


# programloop 
while True:
    # skriver ut menyn och frågar användaren vad den vill göra
    # Skapar en flera rader för menyn 
    meny = ( "\n"
             "\n # Bank & Meny"
             "\n # Saldo {} kr"
             "\n"                                              
             "\n 1. Visa saldo"
             "\n 2. Gör en insättning"
             "\n 3. Gör ett uttag"
             "\n 0. Avsluta program"
             "\n Gör ditt val:".format(balance()))

    val = validate_int(meny, "Felaktig inmatning!")

    if val == 0:
        break
    elif val == 1:
        print(print_transactions())
        
    elif val == 2:
        insättning = validate_int("Ange din summa: ", "Felaktig inmatning!")
        if insättning >= 0:                               # Summan måste vara större än 0
            add_transaction(insättning, True)              # Lägger till insättning i saldo
        else:
            print("Kan inte skriva negativa summor")
    elif val == 3:                                        
        uttag = validate_int("Ange din summa: ", "Felaktig inmatning!")            
        if uttag <= balance() and uttag >= 0:             # Summan behöver vara större än 0
            add_transaction(-uttag, True)                  # Tar bort summan i uttag från saldo
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
