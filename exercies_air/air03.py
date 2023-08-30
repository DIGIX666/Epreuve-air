# Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.


# Exemples d’utilisation :
# $> python exo.py 1 2 3 4 5 4 3 2 1
# 5

# $> python exo.py bonjour monsieur bonjour
# monsieur


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

def find_unique_value(lst):
    if not all(isinstance(x, str) for x in lst):
        print("Erreur : Tous les éléments doivent être du même type (chaîne de caractères ou nombre).")
        sys.exit(1)

    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item, count in counts.items():
        if count == 1:
            return item

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : Le programme nécessite au moins un argument.")
        sys.exit(1)

    lst = sys.argv[1:]

    reslt = find_unique_value(lst)

    print(reslt)


