#Ejercicio 1 (tipos de datos numéricos)


entero: int = 4
decimal: float = 3.5

print(entero + decimal)
print(entero - decimal)
print(- entero)
print(entero * decimal)
print(entero ** 2)
print(entero / decimal)
print(entero // decimal)
print(entero % decimal)

#Ejercicio 2 (tipos de datos booleanos) Cree una variable de tipo booleana al que le asigne un valor True y otra varible de tipo booleana con valor False y 
# realice las siguientes operaciones mostrando el resultado por pantalla (función print):

false: bool = False
true: bool = True

print(false and true)
print(false or true)
print(not true)

#Ejercicio 3 (tipo de datos cadenas - operadores y funciones)

shortstring: str = "soy una cadena corta"
longstring: str = "pues soy una cadena más larga porque tengo más caracteres"

print(shortstring + longstring)
print(shortstring * 3)
print(shortstring == longstring)
print(shortstring < longstring)
print(len(shortstring))
print(shortstring [8 : 14])
print(longstring [13 : 19])
print("larga" in longstring)
print("larga" in shortstring)
print("Lista de la compra \"Cumpleaños Borja\":\n\tChorizo.\n\tPanceta.\n\tChuletas de cordero.")

#Ejercicio 4 (tipo de datos cadenas - métodos)


learning_py: str = "Estoy aprendiendo el lenguaje de programación Python"

print(learning_py.find("Python"))
print(learning_py.split(" "))
print(learning_py.replace("Python", "Python3"))
print(learning_py.upper())
print(learning_py.lower())
print(learning_py.startswith("Estoy"))
