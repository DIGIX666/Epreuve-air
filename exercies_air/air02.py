
# Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères.
# Espacés d’un séparateur donné en dernier argument au programme.
#
# Utilisez une fonction de ce genre (selon votre langage) :
# ma_fonction(array_de_strings, separateur) {
# # votre algorithme
# return (string)
# }


# Exemples d’utilisation :
# $> python exo.py “je” “teste” “des” “trucs” “ “
# Je teste des trucs


# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def concat_strings(array_de_strings, separateur):
    if not all(isinstance(s, str) for s in array_de_strings):
        print("Erreur : Toutes les entrées doivent être des chaînes de caractères.")
        sys.exit(1)

    return separateur.join(array_de_strings)

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) < 3:
        print("Erreur : Le programme nécessite au moins deux arguments.")
        sys.exit(1)

    separateur = sys.argv[-1]
    array_de_strings = sys.argv[1:-1]

    # Appel de la fonction
    resultat = concat_strings(array_de_strings, separateur)

    print(resultat)


