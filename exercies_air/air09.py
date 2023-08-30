# Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.

# Utilisez une fonction de ce genre (selon votre langage) :
# ma_rotation(array) {
# 	# votre algorithme
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py “Michel” “Albert” “Thérèse” “Benoit”
# Albert, Thérèse, Benoit, Michel


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

def rotate(array):
    return array[1:] + array[:1]

def main():
    try:
        array = sys.argv[1:]
        print(", ".join(rotate(array)))

    except ValueError:
        print("Error: Please provide a list of strings.")

if __name__ == "__main__":
    main()