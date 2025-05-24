"""

Cuenta regresiva

Imprime de "n" a 0 en la misma línea, separados por comas.

"""

def main():

    BANNER = r"""
╭──────────────────────────────────────────────────────────────────────────────────╮
│   Cuenta regresiva                                                               │
│                                                                                  │
│    — Este programa imprime de "n" a 0, donde "n" es el número ingresado.         │
╰──────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    user_number = int(input("Escribe un número: "))

    for i in range(user_number, -1, -1): # Va desde user_name hasta -1 con "saltos" de -1 (disminuye 1 a 1).
        space_between = ", "
        if i == 0:
            space_between = "\n" # Salto de línea
        print(i, end=space_between)

if __name__ == "__main__":
    main()