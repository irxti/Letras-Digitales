from typing import Union


#reserved words: if, and, True, False, ennumerate...
#symbols: +, -, <, >, "", (); [], *, %
#Todo lo que no son reserved words o symbols son probablemente nombres de variables que estoy poniendo yo.

### Data types

#Numeric (int, float)

an_int:  int = 8
a_float: float = 9.1

#Estructura asignación (variable: type= value) una "declaración" es solo variable: type.

#Text (str)

a_string: str = "irati"

#Boolean (bool)

a_boolean: bool = False

#Data structure (list, dict, tuple)

a_list: list [int] = [1, 5, 7]
another_list: list[str] = ["Alberto", "Irati", "Aitana"]

a_dict: dict[str, Union[str, int]] = {
    "name": "age", 
    "age": 24
}

a_tuple: tuple [str]= ("Alberto", "Irati")

a_set: set [str] = {}


print("¿Cómo te llamas?")
name_answer: str = input() 
print("Hola, " + name_answer + ". ¿Cuántos años tienes?")
age_answer_introduced_by_user: str = input()
age_answer: int = int(age_answer_introduced_by_user)

if age_answer >= 18:
    print(name_answer + ", te recomiendo La bruja (2016)")
elif age_answer < 5:
    print(name_answer + ", te recomiendo dejar de usar el ordenador.")
elif age_answer == 5:
    print(name_answer + ", por el culo te la hinco.")
elif age_answer <= 12:
    print(name_answer + ", te recomiendo Torrente (2005)")
else:
    print(name_answer + ", no te recomiendo nada :(")

years_till_50: int= 50 - age_answer
if age_answer < 50:
    print("Te quedan " +  str(years_till_50) + " años para los 50.")