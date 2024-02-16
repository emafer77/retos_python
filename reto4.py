usuarios = []

while True:
    print("\nMenú:")
    print("A.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Consultar usuario por ID")
    print("D.- Editar usuario por ID")
    print("E.- Finalizar programa")

    opcion = input("Seleccione una opción (A/B/C/D/E): ").upper()

    if opcion == 'A':
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

    elif opcion == 'B':
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("ID de usuarios registrados:")
            for i,value in enumerate(usuarios):
                print(f"ID: {i + 1} {value}")

    elif opcion == 'C':
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            while True:
                try:
                    id_usuario = int(input("Ingrese el ID del usuario para consultar: "))
                    if 1 <= id_usuario <= len(usuarios):
                        print("Información del usuario:")
                        for key, value in usuarios[id_usuario - 1].items():
                            print(f"{key}: {value}")
                        break
                    else:
                        print("ID de usuario inválido. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un valor numérico válido.")

    elif opcion == 'D':
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            while True:
                try:
                    id_usuario = int(input("Ingrese el ID del usuario para editar: "))
                    if 1 <= id_usuario <= len(usuarios):
                        usuario_actualizado = usuarios[id_usuario - 1].copy()
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
                            usuarios[id_usuario - 1] = usuario_actualizado
                            break
                        print("Usuario actualizado exitosamente.")
                        break
                    else:
                        print("ID de usuario inválido. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un valor numérico válido.")

    elif opcion == 'E':
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
