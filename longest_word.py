user_words: list[str] = []

print("Introduzca la primera palabra")
while True:
    user_word: str = input()
    if user_word == "fin":
        break
    user_words.append(user_word)
    print("Introduzca la siguiente palabra o 'fin' para finalizar")

if len(user_words) > 0:
    longest_words: list[str] = []
    for word in user_words:
        if len(longest_words) == 0:
            longest_words.append(word)
            continue
        if len(longest_words[0]) > len(word):
            continue
        if len(longest_words[0]) < len(word):
            longest_words = [word]
        else:
            longest_words.append(word) 
        
    if len(longest_words) > 1:
        print(
            "Hay varias palabras igual de largas, que son las más "
            f"largas introducidas por el usuario, son: {', '.join(longest_words)}"
        )
    else:
        print(f"La palabra más larga introducida es: {longest_words[0]}")
else:
    print("No ha introducido ninguna palabra")

# or (less SOLID compliant but more efficient)

longest_word: str = ""
print("Introduzca la primera palabra")
while True:
    user_word: str = input()
    if user_word == "fin":
        break
    
    if len(longest_word) < len(user_word):
        longest_word = user_word
    
    print("Introduzca la siguiente palabra o 'fin' para finalizar")

if len(longest_word) > 0:
    print(f"La palabra más larga introducida es: {longest_word}")
else:
    print("No ha introducido ninguna palabra")