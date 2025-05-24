"""

Tabla de multiplicar

Solicita un número n (1 - 10) y muestra su tabla de multiplicar del 1 al 12.

"""

def main():

    BANNER = r"""
╭──────────────────────────────────────────────────────────────────────────────────╮
│   Tabla de multiplicar                                                           │
│                                                                                  │
│    — Este programa muestra las multiplicaciones del 1 al 12 de n.                │
╰──────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    user_number = int(input("Escribe un número: "))

    print("\n--------------------------------------------------\n")

    for i in range(1, 13): # Del 1 al 13, sin contar el 13 (es decir, hasta el 12).
        print(f"{user_number} × {i} = {user_number * i}")
    

if __name__ == "__main__":
    main()