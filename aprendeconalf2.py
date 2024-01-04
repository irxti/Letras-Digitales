
print("Pizzería Bella Napoli, ¿deseas una pizza vegetariana? (Y/N)")
useroption_vegetarian = input()
if useroption_vegetarian.upper() not in ["Y", "N"]:
    print("Invalid option")
else:
    if useroption_vegetarian == "Y":
        print("Puedes elegir los siguientes ingredientes: pimiento y tofu.")
    else:
        print("Puedes elegir los siguientes ingredientes: pimiento, tofu, peperoni, jamón y salmón.")

    vegetarian_ingredients: list = ["pimiento", "tofu"]
    karnaka_ingredients: list = ["peperoni", "jamón", "salmón"]
    selectable_ingredients: list = karnaka_ingredients + vegetarian_ingredients

    print("Además de tomate y mozzarella, ¿qué primer ingrediente quieres?")
    customer_ingredients = []
    while True:
        customer_ingredient = input()
        customer_ingredients.append(customer_ingredient)
        print ("¿Quieres añadir algo más? Y/N")
        anotherone = input()
        if anotherone.upper() == "Y":
            print ("¿Qué más quieres?")
        else:
            break
    
    # if () not in selectable_ingredients:
    #     print(f"{first_ingredient} es una opción inválida")
    # elif second_ingredient.lower() not in selectable_ingredients:
    #     print(f"{second_ingredient} es una opción inválida")
    # elif first_ingredient.lower() in vegetarian_ingredients and second_ingredient.lower() in vegetarian_ingredients:
    #     print(f"tu pizza es una vegetariana de {first_ingredient} y {second_ingredient}.")
    # else:
    #     print(f"tu pizza es de {first_ingredient} y {second_ingredient}.")

    # first_ingredient = input()
    # print("¿Y un segundo ingrediente?")
    # second_ingredient = input()

    


