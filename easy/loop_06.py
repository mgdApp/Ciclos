"""

Máximo y mínimo dinámico

Pide números enteros indefinidamente hasta que el usuario escriba fin. Luego muestra el mayor y el menor ingresados.

"""

def main():

    BANNER = r"""
╭────────────────────────────────────────────────────────────────────────────────────────╮
│   Máximo y mínimo dinámico                                                             │
│                                                                                        │
│    — Este programa muestra el máximo y el mínimo de una lista de números ingresados.   │
╰────────────────────────────────────────────────────────────────────────────────────────╯
"""

    print(BANNER)

    list_of_numbers = []

    max = 0

    while True:

        user_number = int(input("Escribe un número: "))

        list_of_numbers.append(user_number)

        if len(list_of_numbers) >= 2:

            user_option = input("\n¿Quieres agregar más números? (s/n): ")

            if user_option == "n":
                break
            elif user_option == "s":
                continue
            else:
                print("Escribe una opción correcta.")

    for i in range(len(list_of_numbers)):

        if max < list_of_numbers[i]:
            max = list_of_numbers[i]
    
    min = max

    for j in range(len(list_of_numbers)):

        if min > list_of_numbers[j]:
            min = list_of_numbers[j]

    print("\n--------------------------------------------------\n")

    print(f"El máximo número insertado es {max} y el mínimo es {min}.")
            

if __name__ == "__main__":
    main()