def is_integer(data):
    try:
        int_value = int(data)
        return True
    except ValueError:
        return False
    
def is_float(data):
    try:
        float_value = float(data)
        return True
    except ValueError:
        return False
    
def is_text(data):
    words = data.split()
    for word in words:
        if not word.isalpha():
            return False
    return True


def check_datatype(data,datatype):
        if not data.strip():
            return False
        
        if datatype == "I":
            if is_integer(data):
                return True
            else:
                return False
            
        elif datatype == "F":
            if is_float(data):
                return True
            else:
                return False

        elif datatype == "T":
            if is_text(data):
                return True 
            else:
                return False
        else:
            print("Fel datatyp")
            exit()



def main_interaktion():
    while True:
        print ("1: Kontrollera heltal: ")
        print ("2: Mata in ett flyttal: ")
        print ("3: Mata in text: ")
        print ("4: Avbryt programmet")

        svar = input("\nMata in ett alternativ: ")
        if svar == '1':
            tal = input("\nMata in ett heltal: ")
            if not check_datatype(tal,'I'):
                print("Det var inte ett heltal")
            else:
                print("Input OK")
        elif svar == '2':
            tal = input("\nMata in ett flyttal: ")
            if not check_datatype(tal,'F'):
                print("Det var inte ett flyttal")
            else:
                print("Input OK")
        elif svar == '3':
            tal = input("\nMata in lite text: ")
            if not check_datatype(tal,'T'):
                print("Du måste mata in något")
            else:
                print("Input OK")
        elif svar == '4':
            break
        else:
            print("Felaktigt val")


if __name__ == "__main__":
    main_interaktion()
