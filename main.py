# Importation des bibli 
import string
import hashlib
import random
import json

#Definition des variables avec les cara possible pour les mdp
smol = string.ascii_lowercase
big = string.ascii_uppercase
nmb = string.digits
char_spe = '!$@#%^&*'

#Génère un mdp random avec au moins 1 cara de chaque type, le mdp random est stocké dans "rpassword"
rng1 = random.sample(smol, 1) + random.sample(big, 1) + random.sample(nmb, 1) + random.sample(char_spe, 1)
rng2 = random.choices(smol + big + nmb + char_spe, k=4)
rpassword = "".join(rng1 + rng2)

#Demande au user s'il veut un mdp random avec une boucle while et des instructions de conditions
while True:
    question_rng =input("Souhaitez-vous un mot de passe aléatoire ? Y/N : ")

    if question_rng in ['Y', 'y', 'oui', 'O', 'Oui']:  #Si oui, utilise hashlib pour crypter le mdp en Sha256 et affiche le mdp
        hash = hashlib.sha256()
        hash.update(rpassword.encode())
        hexa_hash = hash.hexdigest()
        print(f"Votre mot de passe aléatoire : {rpassword}")
        exit()
    elif question_rng in ['N', 'n', 'non', 'Non']:    #Si non, la boucle se termine et ça passe à la fonction suivante
        print("Très bien!")
        break
    else:
        print("Veuillez répondre par 'Y'(Yes) ou 'N'(No)")

def password1():    #user saisit un mdp et vérifie si les exigences sont respectés
    while True:
        password = input("Veuillez entrer votre mot de passe:")
        lower, upper, special, digit = 0, 0, 0, 0
        if len(password) >= 8:
            for i in password:
                if i in smol:
                    lower += 1           
                if i in big:
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
            print("Le mot de passe doit contenir au moins 8 caractères.")   #Si le mdp est valide, la fonction renvoie le mdp. Sinon affichage d'un message d'erreur spécifique au problème

password = password1()

def hashpwd(password):    #Crypte le mdp en sha256 avec la bibli hashlib et renvoie le hash
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def savepwd(password):    #Prend le mdp du user, le crypte avec "hashpwd" puis écrit le hash dans le fichier json. Affiche le mdp clair et le hash pour que le user puisse l'enregistrer
    hashed = hashpwd(password)
    with open("Pwd.json", "a") as file:
        file.write(hashed + "\n")
        print("Mot de passe enregistré avec succès!")
        print(f"Votre mot de passe crypté '{password}' : {hashed}") 

hashed = hashpwd(password)
savepwd(password)

def addpwd():            #Demande de saisir un nouveau mdp, puis utilise "checkpwd" pour vérif si le mdp est existant dans "Pwd.json"
    password = input("Entrez un nouveau mot de passe: ")
    checkpwd(password)


def listpwd():           #Lit le fichier "Pwd.json" et affiche la liste des hashes des mdp enregistrés
    with open("Pwd.json", "r") as file:
        hashed_passwords = file.readlines()
        if hashed_passwords:
            print("Liste des mots de passe enregistrés:")
            for hashed_password in hashed_passwords:
                print(hashed_password.strip())
        else:
            print("Aucun mot de passe enregistré.")


def checkpwd(password):  #vérifie si le mdp existe dans le json en comparant le hash du mdp du user avec les hashes enregistrés.
    with open("Pwd.json", "r") as file:
        hashed_passwords = file.readlines()
        hashed_password = hashpwd(password)
        if hashed_password + "\n" in hashed_passwords:
            print("Ce mot de passe existe déjà.")
        else:
            savepwd(password)  #Si le mdp est nouveau, "savepwd" pour enregistrer
while True:                    #Afficher le menu avec les trois options
    print("Que voulez-vous faire ?")
    print("1 - Ajouter un mot de passe")
    print("2 - Afficher les mots de passe enregistrés")
    print("3 - Quitter")
    choice = input("> ")
    if choice == "1":
        addpwd()
    elif choice == "2":
        listpwd()
    elif choice == "3":
        break
    else:
        print("Choix invalide.")