"""

Serie de Fibonacci limitada

Pide un entero k y genera la serie de Fibonacci hasta que el siguiente término sobrepase k.

"""

def main():

    BANNER = r"""
╭───────────────────────────────────────────────────────────────────────────────────────────╮
│   Serie de Fibonacci limitada                                                             │
│                                                                                           │
│    — Este programa solicita un número y genera una serie de Fibonacci hasta sobrepasar    │
│      dicho número.                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    user_number = int(input("Escribe un número: "))

    print("\n--------------------------------------------------\n")

    fib_first = 0

    fib_second = 1

    print(fib_first, end=" ")

    print(fib_second, end=" ")

    while True:

        fib_current = fib_first + fib_second

        print(fib_current, end=" ")

        fib_first = fib_second

        fib_second = fib_current

        if fib_current > user_number:
            break

if __name__ == "__main__":
    main()