import string
import hashlib
import random

petit = string.ascii_lowercase
grand = string.ascii_uppercase
nmb = string.digits
char_spe = '!$@#%^&*'
rpassword = "".join(random.choices(petit+grand+nmb+char_spe, k=8))

question_rng =input("Souhaitez-vous un mot de passe aléatoire ? Y/N : ")

if question_rng== "Y":
    hash = hashlib.sha256()
    hash.update(rpassword.encode())
    hexa_hash = hash.hexdigest()
    print(f"Votre mot de passe aléatoire : {rpassword}")
elif question_rng== "N":
    print("Très bien !")
else:
    print("Veuillez répondre par 'Y'(Yes) ou 'N'(No)")


def password1():
    while True:
        password = input("Veuillez entrer votre mot de passe:")
        lower, upper, special, digit = 0, 0, 0, 0
        if len(password) >= 8:
            for i in password:
                if i in petit:
                    lower += 1           
                if i in grand:
                    upper += 1     
                if i in nmb:
                    digit += 1
                if i in char_spe:  
                    special += 1

            if lower < 1:
                print("Veuillez ajouter un caractère minuscule.")
            elif upper < 1:
                print("Veuillez ajouter une majuscule.")
            elif digit < 1:
                print("Veuillez ajouter un chiffre.")
            elif special < 1:
                print("Veuillez ajouter un caractère spécial tel que !, @, #, $, %, ^, &, *")

            elif lower >= 1 and upper >= 1 and digit >= 1 and special >= 1 and lower + upper + digit + special == len(password):
                print("Mot de passe valide.")
                return password
            else:
                print("Veuillez respecter les instructions.")
        else:
            print("Le mot de passe doit contenir au moins 8 caractères.")

password1()


