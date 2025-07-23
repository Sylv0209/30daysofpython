# Exercice: niveau 2
#1. Vérification la version Python que j' utilise
import sys
print(version := sys.version)  # Affiche la version de Python utilisée
''' On peut aussi utiliser la commande suivante pour vérifier la version de Python
python --version dans le terminal ou l'invite de commande.'''
#2. Afficher le résultat de quelques opérations arithmétiques
print("Les résultats des opérations arithmétiques entre 3 et 4 sont :")
print("addition(+):", 3 + 4) #addition(+)
print("Soustraction(-):", 3 - 4) # Soustraction(-)
print("Multiplication(*):", 3 * 4) # Multiplication(*)
print("module(%):", 3 % 4) #module(%)
print("division(/):", 3 / 4) # division(/)
print("exponentiel(**):", 3 ** 4) # exponentiel(**)
print("Floor Division Operator (//):", 3 // 4) # Floor Division Operator (//)

#  3. Chaînes sur la coque interactive Python
print("Nom: Ablan-Silvin") #nom
print("Nom de famille: ETOVENA") #nom de famille
print("Pays: TOGO") #pays
print("Je profite de 30 jours de python")

# 4. Vérification des types de données
print("10", type(10)) #Entier
print("9.8", type(9.8)) # float
print("3.14", type(3.14)) # float
print("4 - 4j", type(4 - 4j)) # complexe
print("['Asabeneh', 'Python', 'Finlande']", type(['Asabeneh', 'Python', 'Finlande']))
print("Ablan-Silvin", type ("Ablan-Silvin")) # string
print("ETOVENA", type ("ETOVENA")) # string
print("TOGO", type ("TOGO")) # string