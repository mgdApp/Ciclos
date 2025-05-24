"""

Suma de los primeros n números

Calcula la suma 1 + 2 + … + n usando un bucle, sin emplear la fórmula matemática directa.

"""

def main():

    BANNER = r"""
╭──────────────────────────────────────────────────────────────────────────────────╮
│   Suma de los primeros n números                                                 │
│                                                                                  │
│    — Este programa calcula la suma 1 + 2 + … + n.                                │
╰──────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    user_number = int(input("Escribe un número: "))
    total = 0

    if user_number >= 0:

        for i in range(user_number + 1):
            total += i

        print(f"El resultado de la suma es {total}.")

    else:
        print("Ingresa un número mayor o igual que 0.")

if __name__ == "__main__":
    main()