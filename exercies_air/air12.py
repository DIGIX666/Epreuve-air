# Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).

# Vous utiliserez une fonction de cette forme (selon votre langage) :
# my_quick_sort(array) {
# 	# votre algorithme
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py 6 5 4 3 2 1
# 1 2 3 4 5 6



# Afficher error et quitter le programme en cas de problèmes d’arguments.


# Wikipedia vous présentera une belle description de cet algorithme de tri.



import sys

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
def main():
    try:
        array = [int(i) for i in sys.argv[1:]]
        print(" ".join([str(i) for i in quick_sort(array)]))

    except ValueError:
        print("Error: Please provide a list of integers.")

if __name__ == "__main__":
    main()