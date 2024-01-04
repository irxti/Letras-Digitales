#Ejercicio 1 (listas)
animales01: list[str] = ["perro", "gato", "tortuga"] 
animales02: list[str] = ["pez"] 
print(animales01 [1 : 3])
print("gato" in animales01)
print("gato" in animales02)
print(len(animales01))
print(len(animales02))
print(max(animales01))
print(min(animales02))
animales02.append("lagarto")
print(animales02)
print(animales01.count("perro"))
print(animales01 + animales02)
print(animales01.index("tortuga"))
animales01.insert(1, "mono")
print(animales01)
animales01.pop(3)
print(animales01)
animales01.remove("perro")
print(animales01)


#Ejercicio 2
teléfonos : dict[str, int] = 
{'Daniel' : 2345, 'Pepe' : 2233, 'Juan' : 5665,}
pedrosinfo: dict[str, int] = {'Pedro' : 2534}
print(teléfonos.update(pedrosinfo))
teléfonos.update({'Daniel' : 1111})
print(teléfonos)
print('Pepe' in teléfonos)
print(len(teléfonos))
print(teléfonos.keys())
print(teléfonos.values())
teléfonos.pop('Daniel')
print (teléfonos)
teléfonos2 = {'Pepe' : 2222, 'Carlos' : 2173}
teléfonos.update(teléfonos2)
print(teléfonos)
teléfonos.clear()
print(teléfonos)

