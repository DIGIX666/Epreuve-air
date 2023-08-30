# Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.


# Exemples d’utilisation :
# $> python exo.py O 5
#     O
#    OOO
#   OOOOO
#  OOOOOOO
# OOOOOOOOO


# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys

def main():
    try:
        char = sys.argv[1]
        height = int(sys.argv[2])
        for i in range(height):
            print(" " * (height - i - 1) + char * (2 * i + 1))

    except ValueError:
        print("Error: Please provide a character and a height.")

if __name__ == "__main__":
    main()