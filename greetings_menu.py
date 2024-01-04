while True:
    print("1) Salir")
    print("2) Saludar en castellano")
    print("3) Saludar en inglés")
    print("4) Saludar en francés")
    user_option: str = input()
    
    if user_option == "1":
        break
    elif user_option == "2":
        print("Hola")
    elif user_option == "3":
        print("Hello")
    elif user_option == "4":
        print("Bonjour")
    else:
        print("Invalid option")