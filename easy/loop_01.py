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

    for i in range(user_number):
        print(f"{user_number - i}", end=", ")
    else:
        i += 1
        print(f"{user_number - i}")

if __name__ == "__main__":
    main()