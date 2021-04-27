from config import *

#Funktioner
def balance ():
    """ Beräknar saldot på kontot
    
    :retur: saldot
    """

    balance = 0
    for t in transactions:
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


def print_transactions():
    """ Skapar utrskrift av alla transaktioner

    :return: sträng med hela utskriften
     """
    line = 0
    balance = 0
    output = ("\nAlla transaktioner:"                                               #Transaktioner skrivs ut med rubriker
              "\n{:>3} {:>12} {:>12}"
              "\n_____________________________").format("Nr", "Händlese", "Saldo")
    for t in transactions:
        line += 1
        balance += t
        output += ("\n {:>2}. {:>9} kr {:>9} kr".format(line, t, balance))
    
    return output


def check_file_exists():
    """ Om filen inte finns så skapas den och sedan läggs en transaktion till 
        Eftersom "x" returnerar ett error om filen finns kan vi utnyttja detta.
        :return: None
        """
    try:
        with open(filename, "x"):
            print("Filen skapades")

        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    
    except:
        return 



def read_file():
    """ Läser in filens innehåll till transaktionslistan

    :return: None
    """ 

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transactions.append(int(rad))




def add_transaction(transaction):
    """ Lagrar transaktioner till transaktionslistan och till filen

    :return: None
    """
    transactions.append(transaction)
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))



