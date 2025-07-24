#Jour2: 30 Days of Python Programming
#Level_1
Prenom = "Ablan-Silvin"
Nom_de_famille = "ETOVENA"
Nom_complet = "ETOVENA Ablan-Silvin"
Pays = "Togo"
'''7. Déclarer une variable municipale et attribuer une valeur à un pays.
et attribuer une valeur à lui'''
municipale = "Lomé"
Pays = "Togo"
An = 2025
Est_maried = False
Is_true = "Etudiant"
IS_light_on = True
Fruit, Sport, Anime, Jeu = "banane", "Football", "Naruto, One Piece", "Subway Surf"

#Level_2
#1. Vérifications des types de données
print(type(Prenom))
print(type(Nom_de_famille))
print(type(Nom_complet))    
print(type(Pays))
print(type(municipale))
print(type(An))
print(type(Est_maried))
print(type(Is_true))
print(type(IS_light_on))
print(type(Fruit))
print(type(Sport))
print(type(Anime))
print(type(Jeu))
#2. Longeur de mon prenom à l'aide de la fonction intégrée len()
len(Prenom)
#Comparez la longueur de votre prénom et votre nom de famille 4
len(Nom_de_famille)
if len(Prenom) > len(Nom_de_famille):
    print("La longueur de mon prénom est supérieure à celle de mon nom de famille.")
elif len(Prenom) < len(Nom_de_famille):
    print("La longueur de mon prénom est inférieure à celle de mon nom de famille.")

num_one = 4
num_two = 5
Valeur = num_one + num_two
NUM_ON = 1
valeur = num_two - NUM_ON
soustraction = num_two - num_one
multiplication = num_one * num_two
division = num_one / num_two
vaiable_reste = num_two % num_one
Floor_Division = num_two // num_one
print("Valeur =", Valeur)
print("valeur =", valeur)    
print("Soustraction =", soustraction)
print("Multiplication =", multiplication)
print("Division =", division)
print("Reste =", vaiable_reste)
print("Floor Division =", Floor_Division)   

#12. Aire du cercle
rayon = input("Entrez le rayon du cercle: ")
area_of_circle = 3.14 * float(rayon) ** 2
circum_of_circle = 2 * 3.14 * float(rayon)
print("L'aire du cercle =", area_of_circle)
print("La circonférence du cercle =", circum_of_circle)

# 13.Utilisez la fonction d'entrée intégrée pour obtenir les informations de l'utilisateur
Prenom = input("Entrez votre prénom: ")
Nom_de_famille = input("Entrez votre nom de famille: ")
Pays = input("Entrez votre pays: ")
Age = input("Entrez votre âge: ")
#14.Exécutez l'aide («mots clés») dans Python Shell
'''Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help('keywords')'''
#On peut aussi utiliser la commande suivante pour obtenir les mots clés
#python -m keyword dans le terminal ou l'invite de commande.
import keyword
print("Mots clés Python:", keyword.kwlist)