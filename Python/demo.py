taxe_actuelle = float(input())
nouvelle_taxe = float(input())
prix_actuel = float(input())

prix_actuel_ht = prix_actuel - prix_actuel * taxe_actuelle/100

nouveau_prix_ttc = prix_actuel_ht + prix_actuel_ht * nouvelle_taxe/100

print(nouveau_prix_ttc)
