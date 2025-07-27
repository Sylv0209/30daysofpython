# Opération sur les listes
#Level 1
Liste, Lst = [],list() # Liste vide
print("Liste vide:", Liste)
print("Liste vide:", Lst)
# Liste avec plus de 5 éléments
Liste = [1, 2, 3, 4, 5, 6]
len_Liste = len(Liste)  # Longueur de la liste
print("Longueur de la liste: Longueur =", len_Liste)
print("Liste avec plus de 5 éléments est: Liste =", Liste)
element_1 = Liste[0]  # Premier élément
element_moyen = Liste[4]  # Element moyen
element_last = Liste[-1]  # dernier élément
print("Premier élément de la liste: Element_1 = ", element_1)
print("Element moyen de la liste: Element_moyen = ", element_moyen)
print("Dernier élément de la liste: Element_last = ", element_last)

#Liste mixte
mixtes_data_types = ["ETOVENA", 21, 1.76 , "Célibataire", "Didjolé"]
print("Liste mixte:", mixtes_data_types)

# Liste IT_COMPANIES
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Liste IT_COMPANIES:", IT_COMPANIES)
print("Nombre d'entreprise dans la liste IT_COMPANIES est :", len(IT_COMPANIES))
First_company = IT_COMPANIES[0]  # Premier élément
Last_company = IT_COMPANIES[-1]  # Dernier élément
midle_company = IT_COMPANIES[3]  # Element moyen
print("Frist_company:", First_company, "Last_company:", Last_company, "midle_company:", midle_company)

#Modification d'une compagnie
IT_COMPANIES[3] = "Meta"
print("Liste IT_COMPANIES après modification:", IT_COMPANIES)
# Ajout d'une nouvelle compagnie
IT_COMPANIES.append("Twitter")
print("Liste IT_COMPANIES après ajout de Twitter:", IT_COMPANIES)

#Insertion d'une société au milieu de la liste
# Insertion de "Tesla" à l'index 3
IT_COMPANIES.insert(3, "Tesla")   

#Changement du nom d'une copagnie en majuscule sauf IBM, exemple : Facebook
IT_COMPANIES = IT_COMPANIES[0].upper()

#Vérification de l'existence d'une compagnie
DOID_EXISTE = "15" in IT_COMPANIES
print("15 existe-t-il dans IT_COMPANIES ?", DOID_EXISTE)

# Tri des élémznts de la liste IT_COMPANIES
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Meta", "IBM", "Oracle", "Amazon", "Twitter"]
IT_COMPANIES.sort()
print("Liste IT_COMPANIES triée:", IT_COMPANIES)

# Reverse de la liste IT_COMPANIES
IT_COMPANIES.sort(reverse=True)
print("Liste IT_COMPANIES inversée:", IT_COMPANIES)

#1Éliminez les 3 premières sociétés de la liste
del IT_COMPANIES[0:3]
print("Liste IT_COMPANIES après suppression des 3 premières sociétés:", IT_COMPANIES)

# Élimination des 3 dernières sociétés de la liste
del IT_COMPANIES[-3:]
print("Liste IT_COMPANIES après suppression des 3 dernières sociétés:", IT_COMPANIES)

IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Meta", "IBM", "Oracle", "Amazon", "Twitter"]
IT_COMPANIES.sort
N = len(IT_COMPANIES)
start = (N - 1) // 2
end = (N // 2) + 1
print("Liste IT_COMPANIES après suppression de la société du milieu:", IT_COMPANIES[start:end])

# Remove de la prémière société
IT_COMPANIES.remove(IT_COMPANIES[0])
print("Liste IT_COMPANIES après suppression de la première société:", IT_COMPANIES)
# Remove de la société sociét du milieu
IT_COMPANIES.remove(IT_COMPANIES[len(IT_COMPANIES) // 2])
print("Liste IT_COMPANIES après suppression de la société du milieu:", IT_COMPANIES)
# Remove de la dernière société
IT_COMPANIES.remove(IT_COMPANIES[-1])
print("Liste IT_COMPANIES après suppression de la dernière société:", IT_COMPANIES)

# Remove de toutes les sociétés
IT_COMPANIES.clear()
print("Liste IT_COMPANIES après suppression de toutes les sociétés:", IT_COMPANIES)

# Déstruction de la liste IT_COMPANIES
del IT_COMPANIES

# Concaténatin de deux listes
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end + back_end
print( front_end + back_end)
#Copie de la liste front_end dans full_stack
full_stack = front_end + back_end
print("Liste full_stack:", full_stack)
# Insertion de 'Python' et 'SQL' à la liste full_stack
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print("Liste full_stack après insertion:", full_stack)

#Level 2
Âges = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Tri de la liste des âges
Âges.sort()
print("Liste des âges triée:", Âges)
# Âge minimum et maximum
min_age = min(Âges)
max_age = max(Âges)
print("Âge minimum:", min_age, "Âge maximum:", max_age)
# Ajout de l'âge minimum et maximum à la liste
Âges.append(min_age)
Âges.append(max_age)
print("Liste des âges après ajout:", Âges)  
#Âge median
start = (len(Âges) - 1) // 2
end = (len(Âges) // 2) + 1
median = Âges[start:end]
print("Âge médian:", median)
#Moyenne des âges
age_moyen = sum(Âges) / len(Âges)
print("Âge moyen:", age_moyen)
# Plage d'âge
age_range = max_age - min_age
print("Plage d'âge:", age_range )
#comparaison des âges
print("Âge minimum égal à l'âge moyen:", abs(min_age) == abs(age_moyen))
print("Âge maximum égal à l'âge moyen:", abs(max_age) == abs(age_moyen))
print("Age maximum supérieur à l'âge moyen:", abs(max_age) > abs(age_moyen))
# Midle country
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

n = len(countries)
start = (n - 1) // 2
end = n // 2 + 1
middle_countries = countries[start:end]
# Séparation de la liste
first_half = countries[:(n + 1) // 2]
second_half = countries[(n + 1) // 2:]

print("1ère moitié :", first_half)
print("2e moitié :", second_half)

#Dépachement de la liste
counties = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *Scandinav_countries = counties
print("Scandinav countries:", Scandinav_countries)

















































