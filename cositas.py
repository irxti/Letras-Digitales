#~el usuario introduce una velocidad en km/h y un tiempo en el que va a estar conduciendo.
#preguntar ambas cosas y decir cuántos km va a recorrer en ese tiempo

import math


print("¿Cuántas horas conduces?")
timeanswer: str = input()
time: float = float(timeanswer)

print("¿A qué velocidad vas a conducir?")
speedanswer: str = input()
speed: float = float(speedanswer)

km: float = time*speed

print("Vas a recorrer " + str(km) +" km.")

if speed >=180:
    print("Vas como una moto racineta")

elif speed >=120:
    print("muere joven")

elif speed <50:
    print("mete el turbo, turboguarra")

else:
    print("vas a " + str(speed) + " km por hora") 


#Cada 50km recorridos 1 punto. Bonus. si tiene un número que termine en 0 toca punto extra.

puntos: int = math.floor(km / 50)

deserves_extra_point: bool = km % 10 == 0
if deserves_extra_point:
    puntos = puntos + 1

print ("Tienes " + str(puntos) + " puntos.")
if deserves_extra_point:
    print("Además has ganado el punto extra (ya incluido)")