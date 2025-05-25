"""

Adivina el número

Genera un entero aleatorio entre 1 y 100. Deja que el usuario lo adivine indicando “muy alto” o “muy bajo”. Cuenta los intentos.

"""

import random

def main():

    BANNER = r"""
╭────────────────────────────────────────────────────────────────────────────────────────╮
│   Adivina el número                                                                    │
│                                                                                        │
│    — Adivina un número generado aleatoriamente entre 1 y 100.                          │
╰────────────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    random_number = random.randint(1, 100)

    attempts = 0

    while True:

        user_number = int(input("Escribe un número: "))

        attempts += 1

        if user_number > random_number:
            print("El número generado es más bajo.\n")
        elif user_number < random_number:
            print("El número generado es más alto.\n")
        elif user_number == random_number:
            print(f"¡Felicidades! Has ganado en {attempts} intentos.")
            break
        else:
            print("Escribe un número válido.\n")
            

if __name__ == "__main__":
    main()