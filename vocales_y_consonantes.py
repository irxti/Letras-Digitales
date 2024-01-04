# vocales = [a, e, i, o, u]
# consonantes = [b, c, d, f, g, h, j, k, l, m, n, ñ, p, q, r, s, t, v, w, x, y, z]

# user_input = input()
# user_input.lower

# user_word_vocales = 0

# for vocal in vocales:
#     if vocal == user_input:
#         user_word_vocales += 1

# user_word_consonantes = 0

# for consonante in consonantes:
#     if consonante == user_input
#         user_word_consonantes += 1

# print(f"La palabra tiene {user_word_vocales} vocales y {user_word_consonantes} consonantes.")    

numvoc = 0
numcon = 0 
palabra = str(input("Introduzca una palabra: "))

for i in range(0,len(palabra)): 
    if palabra[i] in ("a","e","i","o","u","A","E","I","O","U"):  
        numvoc = numvoc + 1;
    elif (palabra[i] in ("b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","x","z","w","y","B","C","D",
                         "F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","X","Z","W","Y")):
        numcon = numcon + 1;
    
print("El número de caracteres totales de esta palabra es: ",numvoc+numcon)  
print("El número de consontantes de esta palabra es: ",numcon)
print("El número de vocales de esta palabra es: ",numvoc)