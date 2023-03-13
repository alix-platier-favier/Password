
"""
question_random =input("Souhaitez-vous un mot de passe aléatoire ? Y/N : ")

if question_random== "Y":
    hash = hashlib.sha256()
    hash.update(rpassword.encode())
    hexa_hash = hash.hexdigest()
    print(f"Votre mot de passe aléatoire : {rpassword}")
elif question_random== "N":
    print("Très bien !")
    password1()
else:
    print("Veuillez répondre par 'Y'(Yes) ou 'N'(No)")

"""

