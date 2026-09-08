print("Hello, World!")
import fonctions as f

try:
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le second nombre : "))
    res = f.puissance(a, b)
    print(f"Résultat : {res}")
except (ValueError, TypeError):
    print("Erreur : Seuls les nombres entiers sont autorisés !")

