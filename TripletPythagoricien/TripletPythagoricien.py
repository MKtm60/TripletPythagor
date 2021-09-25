
# Nombre entrée par l'utilisateur pour effectuer la liste des triplet inférieur a ce nombre
n = int(input("Saisir un entier n >= 1 :"))

# coté du triangle qui forme l'angle droit
a = 1

# coté du triangle qui forme l'angle droit
b = 1

# Hypothénuse (coté opposé à l'angle droit du triangle)
c = 1

def TripletList():
    if n >= 1:
    
        for c in range(1, n+1) :
            for a in range(1, c+1) :
                for b in range(a, c+1) :
                    if (a ** 2 + b ** 2) == c ** 2 :
                        print("(" + str(a) + "," + str(b) + "," + str(c) +")" +
                              " est : " + str(a**2) + "+" + str(b**2) + "="
                              + str(c**2))
TripletList()
