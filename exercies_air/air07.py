# Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. 
# Le dernier argument est l’élément à ajouter.

# Utilisez une fonction de ce genre (selon votre langage) :
# sorted_insert(array, new_element) {
# 	# your algo
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py 1 3 4 2
# 1 2 3 4

# $> python exo.py 10 20 30 40 50 60 70 90 33
# 10 20 30 33 40 50 60 70 90


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

def sorted_insert(array, new_element):
    index = 0
    while index < len(array) and array[index] < new_element:
        index += 1
    array.insert(index, new_element)
    return array

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) < 2:
        print("Usage: python exo.py <sorted integers> <new_integer>")
        sys.exit(1)
    
    try:
        array = [int(arg) for arg in args[:-1]]
        new_element = int(args[-1])
    except ValueError:
        print("Error: Invalid input. Please provide sorted integers.")
        sys.exit(1)
    
    new_array = sorted_insert(array, new_element)
    print(" ".join(map(str, new_array)))
