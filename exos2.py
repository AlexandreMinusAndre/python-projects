#On demande à l'utilisateur les valeurs de x et y
x = int(input("x : "))
y = int(input("y : "))

#Ici, on affiche une phrase indiquant les valeurs de bases des variables
print(f"x is {x} and y is {y}")

#Les lignes 9, 10, et 11, servent à interchanger les valeurs des variables grâce à une variable temporaire (tmp) qui contiendra temporairement la valeur de a
tmp = x
x = y
y = tmp



#On affiche une phrase indiquant les nouvelles valeurs des variables
print(f"x is now {x} and y is now {y}")
