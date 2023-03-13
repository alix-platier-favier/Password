import string
import hashlib
import random

petit = string.ascii_lowercase
grand = string.ascii_uppercase
nmb = string.digits
char_spe = '!$@#%^&*'
alphabet = petit + grand + nmb + char_spe
rpassword = "".join(random.choices(alphabet, k=8))
lower, upper, special, digit = 0, 0, 0, 0



def password1():
    password = input("Veuillez entrer votre mot de passe:")
    return password
pwd = password1()

if len(pwd) >= 8:
    for i in pwd:
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
    if upper < 1:
        print("Veuillez ajouter une majuscule.")
    if digit < 1:
        print("Veuillez ajouter un chiffre.")
    if special < 1:
        print("Veuillez ajouter un caractère spécial tel que !, @, #, $, %, ^, &, *")

    if lower >= 1 and upper >= 1 and digit >= 1 and special >= 1 and lower + upper + digit + special == len(pwd):
        print("Mot de passe valide.")
    else:
        print("Veuillez respecter les instructions.")
else:
    print("Le mot de passe doit contenir au moins 8 caractères.")

question_random =input("Souhaitez-vous un mot de passe aléatoire ? Y/N : ")
if question_random== "Y":
    print(rpassword)
elif question_random== "N":
    print("Très bien !")
    password1()
else:
    print("Veuillez répondre par 'Y'(Yes) ou 'N'(No)")

hasher = hashlib.sha256()
hasher.update(rpassword.encode())
hexa_hash = hasher.hexdigest()
print(f"Votre mot de passe aléatoire : {rpassword}")