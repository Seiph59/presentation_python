# Création d'une liste
ma_liste = [5, 6, 7]
ma_liste2 = [1, 2, 3, 4]

# Accès éléments
print(ma_liste2[1])

# Ajout
ma_liste.append(8)
print(ma_liste)
# [5, 6, 7, 8]

# Insertion
ma_liste.insert(4, 9)
print(ma_liste)

# Concatenation
ma_liste2.extend(ma_liste)
print(ma_liste2)

# Suppression par index
del ma_liste2[8]
print(ma_liste2)

# Suppression par valeur
ma_liste3 = [10, 30, 60, 25, 18, 13]
ma_liste3.remove(30)
sorted(ma_liste3)
print(ma_liste3)
ma_liste3.sort()
print(ma_liste3)

# Modification d'un élément
ma_liste3[0] = 20
print(ma_liste3)

tuple=(1, 2, 3)
print(tuple)