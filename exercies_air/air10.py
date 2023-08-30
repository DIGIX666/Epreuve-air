# Créez un programme qui affiche le contenu d’un fichier donné en argument.


# Exemples d’utilisation :
# $> cat a.txt
# Je danse le mia
# $> python exo.py “a.txt”
# Je danse le mia


# Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.


import sys

def main():
    try:
        with open(sys.argv[1]) as f:
            print(f.read())

    except IndexError:
        print("Error: Please provide a file name.")
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()