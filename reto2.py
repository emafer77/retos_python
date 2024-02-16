num_de_usuarios = int(input('¿Cuántos nuevos usuarios desea ingresar?: '))

for i in range(num_de_usuarios):
   
    while True:
        firt_name = input('Escribe tu nombre: ')
        total_de_caracteres_nombre = 0
        for caracter in firt_name:
            total_de_caracteres_nombre += 1

        if 5 <= total_de_caracteres_nombre <= 50:
            break
        else:
            print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")

    while True:
        last_name = input('Escribe tu apellido: ')
        total_de_caracteres_apellido = 0
        for caracter in last_name:
            total_de_caracteres_apellido += 1

        if 5 <= total_de_caracteres_apellido <= 50:
            break
        else:
            print("Apellido inválido. Debe tener entre 5 y 50 caracteres.")

    while True:
        phone_number = input('Escribe tu número de teléfono: ')
        total_de_digitos = 0
        for caracter in phone_number:
            total_de_digitos += 1

        if total_de_digitos == 10:
            break
        else:
            print("Número de teléfono inválido. Debe tener 10 dígitos.")

    while True:
        email = input('Escribe tu correo electrónico: ')
        total_de_caracteres_correo=0
        if ('@' in email and '.' in email)and 5 <= total_de_caracteres_correo <= 50:
            break
        else:
            print("Correo electrónico inválido.")

    print("Registro exitoso")

