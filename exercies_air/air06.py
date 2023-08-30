# Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.

# Utilisez une fonction de ce genre (selon votre langage) :
# ma_fonction(array_de_strings, string) {
#   votre algorithme
# return (nouvel_array_de_strings)
# }


# Exemples d’utilisation :
# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
# Michel

# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
# Michel, Thérèse, Benoit


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def ma_fonction(array_de_strings, string):
    nouvel_array_de_strings = [s for s in array_de_strings if string.lower() not in s.lower()]
    return nouvel_array_de_strings

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: python3 air06.py reference_string string1 string2 ...")
        sys.exit(1)

    reference_string = args[-1]
    strings = args[:-1]

    nouvel_array = ma_fonction(strings, reference_string)
    if nouvel_array:
        print(", ".join(nouvel_array))
    else:
        print("Tous les éléments contiennent la chaîne de référence.")

