#Funktioner
def balance ():
    """ Beräknar saldot på kontot
    
    :retur: saldot
    """

    balance = 0
    for t in transaktioner:
        balance += t
    return balance 

def validate_int(output, error_mess):

    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transaktioner():
    """ Skapar utrskrift av alla transaktioner

    :return: sträng med hela utskriften
     """
    line = 0
    balance = 0
    output = ("\nAlla transaktioner:"                                               #Transaktioner skrivs ut med rubriker
              "\n{:>3} {:>12} {:>12}"
              "\n_____________________________").format("Nr", "Händlese", "Saldo")
    for t in transaktioner:
        line += 1
        balance += t
        output += ("\n {:>2}. {:>9} kr {:>9} kr".format(line, t, balance))
    
    return output


#Variabler 
saldo = 1000                # Startvärde på 1000 kr
transaktioner = []          # Lista som lagrar transaktioner 
transaktioner.append(1000)  # Startvärde på 1000 kr



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
        print(print_transaktioner())
        
    elif val == 2:
        insättning = validate_int("Ange din summa: ", "Felaktig inmatning!")
        if insättning >= 0:                               # Summan måste vara större än 0
            transaktioner.append(insättning)              # Lägger till insättning i saldo
        else:
            print("Kan inte skriva negativa summor")
    elif val == 3:                                        
        uttag = validate_int("Ange din summa: ", "Felaktig inmatning!")            
        if uttag <= balance() and uttag >= 0:             # Summan behöver vara större än 0
            transaktioner.append(-uttag)                  # Tar bort summan i uttag från saldo
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
