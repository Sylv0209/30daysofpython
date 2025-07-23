# Exercice: niveau 3
#1.Exemple pour différents types de données Python
    # Les nombres
Entier = 10
Float = 9.8
Complexe = 4 - 4j
print("Entier =", Entier,";", 
      "Float =", Float,";",  
      "Complexe =", Complexe)
    #String
String = "Python"
print("String =", String)
    #Boolean
Boolean = False
Boolean2 = True
print("Boolean =", Boolean,";",
      "Boolean2 =", Boolean2)
    #List   
List = ["Ablan-Silvin",10,"Orange",9.8,True]
print("List =", List)
    #Tuple
Tuple = ("Ablan-Silvin",10,"Orange",9.8,True)
print("Tuple =", Tuple)
    #Set
Set = {2,8,4,6,10,"TOGO",228, "Python"}
print("Set =", Set)
    #Dictionary
Dictionary = {"Nom": "Ablan-Silvin","Nom de famille": "ETOVENA  ","age": 21,"Pays": "TOGO",
              "Compétences": ["Fortran","Pascal","Python"],"Domaine": ["Physique","Mathématiques",
              "Informatique"],"Marier": False}
print("Dictionary =", Dictionary)

# 2. Distance euclidienne entre (2, 3) et (10, 8)
from math import sqrt
A = (2, 3)
B = (10, 8)
D = sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
print("La distance euclidienne entre A et B est : D =", D)
# Fin des exercices du jour 1