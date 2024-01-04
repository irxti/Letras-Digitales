num = [0,1,1,1,3,4,3,2,1,3,21,1,1,1,1,23,4,4,6,7]

user_input = input()
user_number = int(user_input)

user_num_count = 0

for number in num:
    if number == user_number:
        user_num_count += 1

print(f"El número {user_number} se repite {user_num_count} veces")    