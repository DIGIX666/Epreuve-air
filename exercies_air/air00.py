# Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations,
# retours à la ligne).
#
# Votre programme devra utiliser une fonction prototypée comme ceci :
# ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
# # votre algorithme
# return (tableau)
# }


# Exemples d’utilisation :
# $> python exo.py “Bonjour les gars”
# Bonjour
# les
# gars


# Afficher error et quitter le programme en cas de problèmes d’arguments.




import sys
import re

def ma_fonction(string_a_couper, string_separateur):
    try:
        tableau = re.split(string_separateur, string_a_couper)
        return tableau
    except:
        print("error")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    string_a_couper = sys.argv[1]
    string_separateur = r'[\s\t\n]+'

    resultat = ma_fonction(string_a_couper, string_separateur)
    for mot in resultat:
        print(mot)
