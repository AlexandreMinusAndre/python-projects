print("Pour calculer le rendement énergétique d'un système électrique, on divise la puissance utilisée par le système, par la puissance qu'on lui fournis")

# On demande à l'utilisateur de rentrer la puissance utilisée et la puissance fournis

pUtile = float(input("Puissance utilisée (en watt) : "))
pFournis = float(input("Puissance fournie (en watt) : "))

rendement = pUtile/pFournis  # Cette variable exécute le calcul du rendement
pourcent = rendement * 100  # Cette variable multiplie le rendement par 100 pour l'obtenir en pourcent

# Ce if permet de ne pas afficher la variable rendement quand la puissance utile est supérieur à la puissance fournis. On met celà en place car le rendement ne peux pas être supérieur à 1
if pUtile > pFournis:
    print("Impossible, la puissance utilisée ne peux pas être supérieur à la puissance fournie")
else:
    print(f"Le rendement de ce système est de {rendement}, sois {pourcent} %")
    # On affiche le rendement une fois normalement et une autre fois en pourcentage