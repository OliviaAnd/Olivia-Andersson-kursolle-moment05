from functions import *
read_file()                # Läser in och/eller skapar fil med transaktioner 

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
             "\n 4. Nollställ konto"
             "\n 0. Avsluta program"
             "\n Gör ditt val:".format(balance()))

    val = validate_int(meny, "Felaktig inmatning!")

    if val == 0:                        # Avsluta
        break

    elif val == 1:                      # Visa transaktioner 
        print(print_transactions())
        
    elif val == 2:                      # Gör insättning
        insättning = validate_int("Ange din summa: ", "Felaktig inmatning!")
        if insättning >= 0:                               # Summan måste vara större än 0
            add_transaction(insättning, True)              # Lägger till insättning i saldo
        else:
            print("Kan inte skriva negativa summor")

    elif val == 3:                      # Gör uttag              
        uttag = validate_int("Ange din summa: ", "Felaktig inmatning!")            
        if uttag <= balance() and uttag >= 0:             # Summan behöver vara större än 0
            add_transaction(-uttag, True)                  # Tar bort summan i uttag från saldo
        elif uttag <= 0:
            print("Uttaget kan inte vara negativt")
        else:
            print("Du har inte tillräckligt med pengar, sorry mate.")

    elif val == 4:            # Nollställer konto
        os.remove(filename)   # Tar bort filen 
        transactions.clear()  # Töm listan 
        read_file()           # Skapa filen och läs in den
   
    else:                     # Alla felaktiga val
        print("Felaktigt val")
    
print("Tack för ditt besök")
   