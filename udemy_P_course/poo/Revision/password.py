# doit se terminer par @ucad.edu.sn

# password:

def verif_email():
    start = True
    while start:
        email = input("Enter you email address ")
        if email.endswith("@ucad.edu.sn"):
            start = False
        
# verif_email()

def verif_password():
    start = True
    while start:
        password = input("Enter your password: ")
        if len(password) > 5 and len(password) < 10:
            if password.isalpha() or password.isnumeric():
                print("Mot de passe invalide")
            else:
                start = False
                print('Mot de passe valide')    
        else:
            print("Mot de passe invalide")
                    
verif_password()                