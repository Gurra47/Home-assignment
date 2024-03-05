members = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']

likes = {'Augusta':['Charmain','Billie','Mandy','Charlotte','Lesley'],'Charmain':
['Augusta','Mandy'],'Billie':['Augusta','Charmain','Lesley',],'Mandy':
['Charlotte','Billie','Augusta'],'Lesley':['Billie']}

rooms_with = {'Augusta':'Charmain','Charmain':'Augusta','Billie':'Lesley','Lesley':
'Billie','Charlotte':'Mandy','Mandy':'Charlotte'}


# IMPORTER, START
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

# IMPORTER, STOP


# TILLÄGG, START
def meny_val_ett(members):
    for item in members:
        print(item)
    print("\n")


def meny_val_tva(members,likes):
    namn = input("Vem letar du efter?: ").capitalize()
    if not namn.strip():
        print("Du måste mata in något\n")
        return
    if namn not in members:
        print(f"{namn} är inte med i föreningen\n")
    elif namn in members and namn in likes:
        gillar_alla = True
        gillar_personer = likes[namn]
        for medlem in members:
            if medlem != namn and medlem not in gillar_personer:
                gillar_alla = False
                break
        if gillar_alla:
            print(f"{namn} gillar alla i föreningen\n")
        else:
            print(f"{namn} gillar:")
            for person in gillar_personer:
                print(f"- {person}")
            print("\n")    
    elif namn not in likes:
        print(f"{namn} tycker inte om någon\n")

def meny_val_tre(members,rooms_with):
    namn = input("Vem letar du efter?: ").capitalize()
    if namn not in members:
        print(f"{namn} är inte med i föreningen\n")
    elif namn in members:
        namn_delar_med = rooms_with[namn]
        print(f"{namn} delar rum med:\n- {namn_delar_med}\n")

# TILLÄGG, STOP



def check_interval(data,low,high):
# Om det inte finns någon data: returnera False
    if is_integer(data):
        if int(data) in range (low, high+1):
            return True
    return False

def menu():
    print("Här är dina val:::")
    print("1: Lista alla medlemmar i föreningen")
    print("2: Vem tycker X om?")
    print("3: Vem delar X rum med?")
    print("4: Avsluta programmet")

def main_interaktion():
    slut = False
    while not slut:
        ok = False
        while not ok:
            menu()
            some_text = input("Mata in ett tal mellan 1-4: ")
            ok = check_interval(some_text,1,4)
            if not ok:
                print("Du måste mata in något mellan 1 och 4")
                break
            ett_heltal = int(some_text)
            if ett_heltal == 4:
                print("Hejdå")
                slut = True
                break
            if ett_heltal == 3:
                meny_val_tre(members,rooms_with)
            if ett_heltal == 2:
                meny_val_tva(members,likes)
            if ett_heltal ==1:
                meny_val_ett(members)


if __name__ == "__main__":
    main_interaktion()
