try:
    fichier_a = open("fichier_a", "r")
    print("avec readline:" + str(fichier_a.readline()))
    fichier_a.close()
except:
    print("Probleme avec l'ouverture du fichier")

try:
    with open ("fichier_a", "r") as f:
        fichier_b = open("fichier_b", "x")
        for ligne in f:
            if "5" in ligne or "6" in ligne:
                print(ligne)
                fichier_b.write(ligne)
        fichier_b.close()
except:
    pass
