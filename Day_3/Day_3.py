#1.
Age = 21
Taille = 1.75
complex = 1 + 2j

#Le triangle
h = input("Entrez la hauteure du triangle: ")
b = input("Entrez la base du triangle: ")
Zone = 0.5 * float(b) * float(h)
print("La zone du triangle est: Zone = ", Zone)
A = input("Entrez la longeur du côté A du triangle: ")
B = input("Entrez la longeur du côté B du triangle: ")
C = input("Entrez la longeur du côté C du triangle: ")
périmetre = A + B + C
print("Le périmètre du triangle est: Périmètre = ", périmetre)
 
# LE rectangle
Longueur = input("Entrez la longeur du rectangle: ")
Largeur = input("Entrez la largeur du rectangle: ")
       # La surface du rectangle
surface = float(Longueur) * float(Largeur)
print("La surface du rectangle est: Surface = ", surface)
      # Le périmètre du rectangle 
perimetre = 2 * (Longueur + Largeur)
print("Le périmètre du rectangle est: Périmètre = ", perimetre)

# Le cercle
pi = 3.14
r = input("Entrez le rayon du cercle: ")
        # La zone du cercle
zone = pi * float(r) * float(r)
print("La zone du cercle est: Zone = ", zone)
        # Le périmètre du cercle
perimetre = 2 * pi * float(r)
print("Le périmètre du cercle est: Périmètre = ", perimetre)

# La pente 
X = (5, 4)
y = (2* X[0] + 3, 2* X[1] + 3)
m = (y[1] - y[0]) / (X[1] - X[0])
print("La pente de la droite est: m = ", m)
#Calccul de la pente et de la distance entre deux points
A = (2, 2)
B = (6, 10)
pente = (B[1] - A[1]) / (B[0] - A[0])
distance = ((B[0] - A[0])**2 + (B[1] - A[1])**2)**0.5
print("La pente de la droite passant par les points A et B est: m = ", pente)
print("La distance entre les points A et B est: Distance = ", distance)

# Comparaison des pentes
print(m == pente)
print(m != pente)
print(m > pente)
print(m < pente)    
print(m >= pente)   
print(m <= pente) 

#11.
# Calcul de y = x^2 + 6x + 9 pour différentes valeurs de x
# Détermination de la valeur de x pour laquelle y = 0
# Résolution de l'équation x^2 + 6x + 9 = 0
# C'est une équation du second degré : (x + 3)^2 = 0 donc x = -3
x = (-10,-6,-3,-1,0,1,2,3,6,10)
for i in range(len(x)):
    y = x[i] ** 2 + 6 * x[i] + 9
    print(x[i], y)
print("La valeur de x pour laquelle y = 0 est x =", -3.0)
#12.
len("Python")
len("Dragon")
print(not(len("Python") == len("Dragon")))
print(len("Python")<3 or len("Dragon") > 3)
print("on" in "Python" and "on" in "Dragon")
texte = "I hope this course is not full of jargon"
print("jargon" in texte)
print ("on"not in "Dragon"and "on" not in "Python")

len =float(len("Python"))
print("len = ", len)
#17
N = int(input("Entrez un nombre entier: "))
print(N % 2 == 0)
#18
print(7//3 == int(2.7))
#19
print(type("10") == type(10))
#20
print(int(9.8) == 10)
#21 
#Heure
heure = float(input("Entrez l'heure: "))
#Taux horaire
taux = float(input("Entrez le taux horaire: "))
# Valeur
Valeur = heure * taux
print("La valeur de l'heure est: Valeur = ", Valeur)
#22 âge et seconde
age = int(input("Entrez votre âge: "))
if age<100:
    seconde = age * 365 * 24 * 60 * 60
    print("Vous avez vécu", seconde, "secondes.")
    print("Vous êtes vivant depuis", seconde, "secondes.")
else:
    print("Entrée invalide. Veuillez entrer un âge inférieur à 100 ans.")
#23
#Table de multiplication
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)

    
                                 
