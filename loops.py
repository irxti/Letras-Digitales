# i: int = 1
# while i <= 100:
#     print(i)
#     i += 1

# i: int = 2
# while i <= 100:
#     print(i)
#     i += 2


# i: int = 2
# while i <= 100:
    
#     if i % 5 == 0:
#         print("Adiós")
#     elif i % 2 == 0:
#         print (i)
#     else:
#         print("hola")
#     i += 1


print("indícame un número")
number: int = int(input())
i: int = 2

is_prime: bool = True

while i < number:
    if number % i == 0:
        is_prime = False
    i += 1

if is_prime is True:
    print ("es primo")
else:
    print ("no es primo")