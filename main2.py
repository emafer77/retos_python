
    
age = int (input('ingresa tu edad: '))

if age >= 0 and age < 110:
    if age >= 18:
        print('tienes la edad para votar')
    else:
        print('no tienes la edad para votar')
else:
    print('la edad no es valida intenta de nuevo')
    
color ="gray"

if color =="green":
    print('puede continuar')
elif color == "yellow":
    print("alto parcial")
elif color =="red":
    print("alto")
else:
    print("el color no es valido ")



match color:
    case 'green':
        print("puede continuar")
    case 'yellow':
        print("Alto parcial")
    case 'red':
        print("detengase")
    case _:
        print("el color no es valido")
    
title ="estructuras de contrl"
for caracter in title:
    print(caracter)

for number in range(1,101):
   if number % 2 == 0:
       print(number)

number =0
while number < 10:
    number += 1
else:
    print("la condicion no se cumple")


random =5
number=10

while number != random:
    number = int(input("ingresa un numero:"))
else:
    print("felicidades")
    
      