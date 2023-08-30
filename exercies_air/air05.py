# Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction)
# sur chaque entier d’une liste.


# Exemples d’utilisation :
# $> python3 exo.py 1 2 3 4 5 “+2”
# 3 4 5 6 7

# $> python3 exo.py 10 11 12 20 “-5”
# 5 6 7 15


# L’opération à appliquer sera toujours le dernier élément.


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

if sys.argv[-1][0] != "+" and sys.argv[-1][0] != "-":
    print("error")
    sys.exit(1)

if not sys.argv[-1][1:].isdigit():
    print("error")
    sys.exit(1)

for i in range(1, len(sys.argv) - 1):
    if not sys.argv[i].isdigit():
        print("error")
        sys.exit(1)

if sys.argv[-1][0] == "+":
    for i in range(1, len(sys.argv) - 1):
        print(int(sys.argv[i]) + int(sys.argv[-1][1:]))
elif sys.argv[-1][0] == "-":
    for i in range(1, len(sys.argv) - 1):
        print(int(sys.argv[i]) - int(sys.argv[-1][1:]))
