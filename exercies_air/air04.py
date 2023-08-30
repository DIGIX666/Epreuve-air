# Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


# Exemples d’utilisation :
# $> python exo.py “Hello milady,   bien ou quoi ??”
# Helo milady, bien ou quoi ?


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys
if len(sys.argv) != 2:
    print("error")
    quit()

print(sys.argv[1][0], end="")
for i in range(1, len(sys.argv[1])):
    if sys.argv[1][i] != sys.argv[1][i-1]:
        print(sys.argv[1][i], end="")
print()





