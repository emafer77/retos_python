usuarios = []

def new_user():
    while True:
        nuevo_usuario = {}
        firt_name = input('Escribe tu nombre: ')
        total_de_caracteres_nombre = len(firt_name)

        if 5 <= total_de_caracteres_nombre <= 50:
            nuevo_usuario['Nombre'] = firt_name
        else:
            print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
            continue

        last_name = input('Escribe tu apellido: ')
        total_de_caracteres_apellido = len(last_name)

        if 5 <= total_de_caracteres_apellido <= 50:
            nuevo_usuario['Apellido'] = last_name
        else:
            print("Apellido inválido. Debe tener entre 5 y 50 caracteres.")
            continue

        phone_number = input('Escribe tu número de teléfono: ')

        if len(phone_number) == 10:
            nuevo_usuario['Teléfono'] = phone_number
        else:
            print("Número de teléfono inválido. Debe tener 10 dígitos.")
            continue

        email = input('Escribe tu correo electrónico: ')
        total_de_caracteres_correo = len(email)

        if ('@' in email and '.' in email) and 5 <= total_de_caracteres_correo <= 50:
            nuevo_usuario['Correo electrónico'] = email
        else:
            print("Correo electrónico inválido.")
            continue

        print("Registro exitoso")
        usuarios.append(nuevo_usuario)
        break

def show_user(user_id):
    print("Información del usuario:")
    for key, value in usuarios[user_id - 1].items():
        print(f"{key}: {value}")

def edit_user(user_id):
    usuario_actualizado = usuarios[user_id - 1].copy()
    while True:
        firt_name = input('Escribe tu nombre: ')
        total_de_caracteres_nombre = len(firt_name)

        if 5 <= total_de_caracteres_nombre <= 50:
            usuario_actualizado['Nombre'] = firt_name
        else:
            print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
            continue

        last_name = input('Escribe tu apellido: ')
        total_de_caracteres_apellido = len(last_name)

        if 5 <= total_de_caracteres_apellido <= 50:
            usuario_actualizado['Apellido'] = last_name
        else:
            print("Apellido inválido. Debe tener entre 5 y 50 caracteres.")
            continue

        phone_number = input('Escribe tu número de teléfono: ')

        if len(phone_number) == 10:
            usuario_actualizado['Teléfono'] = phone_number
        else:
            print("Número de teléfono inválido. Debe tener 10 dígitos.")
            continue

        email = input('Escribe tu correo electrónico: ')
        total_de_caracteres_correo = len(email)

        if ('@' in email and '.' in email) and 5 <= total_de_caracteres_correo <= 50:
            usuario_actualizado['Correo electrónico'] = email
        else:
            print("Correo electrónico inválido.")
            continue

        print("Registro exitoso")
        usuarios[user_id - 1] = usuario_actualizado
        break
    print("Usuario actualizado exitosamente.")

def delete_user(user_id):
    del usuarios[user_id - 1]
    print("Usuario eliminado exitosamente.")

def list_users():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("ID de usuarios registrados:")
        for i, _ in enumerate(usuarios):
            print(f"ID: {i + 1}")

# Mapeo de opciones a funciones
opciones = {
    'A': new_user,
    'B': list_users,
    'C': show_user,
    'D': edit_user,
    'E': delete_user
}

while True:
    print("\nMenú:")
    print("A.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Consultar usuario por ID")
    print("D.- Editar usuario por ID")
    print("E.- Eliminar usuario por ID")
    print("F.- Finalizar programa")

    opcion = input("Seleccione una opción (A/B/C/D/E/F): ").upper()

    if opcion == 'F':
        print("Programa finalizado.")
        break
    elif opcion in opciones:
        if opcion == 'B':
            opciones[opcion]()
        else:
            try:
                id_usuario = int(input("Ingrese el ID del usuario: "))
                opciones[opcion](id_usuario)
            except ValueError:
                print("Ingrese un valor numérico válido.")
    else:
        print("Opción no válida. Intente de nuevo.")
