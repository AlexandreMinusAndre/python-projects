#On demande les 3 valeurs à l'utilisateur
a = int(input("Entrer a : "))
b = int(input("Entrer b : "))
c = int(input("Entrer c : "))


#Si a est plus grand que b et c, alors on imprime que a est le plus grand des 3 chiffres
if a > b and a > c:
    print(f"{a} est le plus grand")

#Si b est plus grand que a et c, alors on imprime que b est le plus grand des 3 chiffres
if b > a and b > c:
    print(f"{b} est le plus grand")

#Si c est plus grand que a et b, alors on imprime que c est le plus grand des 3 chiffres
if c > a and c > b:
    print(f"{c} est le plus grand")

#Le else sert quand un ou plusieurs des chiffres rentrés par l'utilisateur sont égaux.
else:
    print("Plusieurs entiers sont égaux")
