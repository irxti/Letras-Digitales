#pedir un número, indica si es nayor o menor, termina cuando se acierta.

secretnumber = 7

while True:
    usernumber = int(input("Introduzca un número: "))

    if 0 <= usernumber <= 10:
        if usernumber > secretnumber:
            print("Has introducido un número mayor.")
        elif usernumber < secretnumber:
            print("Has introducido un número menor.")
        else:
            print("¡Has acertado!")
            break  # Rompe el bucle cuando se acierta
    else:
        print("El número introducido no es válido.")
