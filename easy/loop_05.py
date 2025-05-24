"""

Contador de vocales

Lee un texto (string) y cuenta cuántas vocales contiene.

"""

def main():

    BANNER = r"""
╭──────────────────────────────────────────────────────────────────────────────────╮
│   Contador de vocales                                                            │
│                                                                                  │
│    — Este programa muestra cuántas vocales tiene un string.                      │
╰──────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    user_string = input("Escribe un texto: ")
    vocals = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    total = 0

    print("\n--------------------------------------------------\n")

    x = 0

    while x < len(vocals):

        for y in user_string:

            if y == vocals[x]:
                total += 1

        x += 1

    print(f"El texto tiene un total de {total} vocales.")

if __name__ == "__main__":
    main()