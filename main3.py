my_list=[1,3.14,"string",True,[2,3.111,"example",False]]
print(my_list)
print(type(my_list))

numbers=[1,2,3,4,5,6,7,8,9]
curses =['python','Django','Flask','Ruby','Ruby on Rails']


print(len(curses))

last_index=len(curses)-1

index = int(input("ingresa el indice del cual quieras conocer su valor:"))

print(curses[index-1])

if index <= last_index :
    print(curses[index])
else:
    print("el indice no es valido")
    
    
    
new_list = curses[0:3]#crear una nueva lista ,el valor 1 siempre es la posicion en la que nos encontramos
print(new_list)
new_curses=['java','c#']



curses.append('c++')#agrega al final
curses.insert(1,"javascript")#inserta en valor en dicha posicion
curses.extend(new_curses)#extiende la lista con otra lista

print(curses)

curses.remove("python")#remueve el valor
print(curses)
print(curses.count("python"))#cuenta cuantas veces esta el mismo valor

print('ruby'in curses)#busca si la palabra ruby esta  en la lista

print(curses.index("c++"))#indica el indice  en el que se encuentra la palabra





    