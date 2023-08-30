# Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.

# Utilisez une fonction de ce genre (selon votre langage) :
# sorted_fusion(array1, array2) {
# 	# your algo
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py 10 20 30 fusion 15 25 35
# 10 15 20 25 30 35


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

def sorted_fusion(array1, array2):
    merged = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    merged.extend(array1[i:])
    merged.extend(array2[j:])
    
    return merged

def main():
    try:
        fusion_index = sys.argv.index("fusion")
        array1 = list(map(int, sys.argv[1:fusion_index]))
        array2 = list(map(int, sys.argv[fusion_index + 1:]))

        if len(array1) == 0 or len(array2) == 0:
            print("Error: Empty arrays are not allowed.")
            return

        new_array = sorted_fusion(array1, array2)
        print(" ".join(map(str, new_array)))

    except ValueError:
        print("Error: Please provide two lists of integers separated by 'fusion'.")

if __name__ == "__main__":
    main()
