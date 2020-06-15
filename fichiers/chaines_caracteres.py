
# Conversion Chaine en liste
chaine1 = "Bonjour à tous !"
liste_chaine = chaine1.split(" ")
print(liste_chaine)

# Conversion Liste en chaine
chaine2 = "-".join(liste_chaine)
print(chaine2)

# Parcourir une liste
for word in liste_chaine:
    # print(word)
    print(word, end= " ")

