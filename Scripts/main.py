from database import crear_tabla, agregar_contacto, obtener_contactos, eliminar_contacto

def main():
    crear_tabla()
    
    while True:
        print("\n--- Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Eliminar contacto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
            print("Contacto agregado.")
        
        elif opcion == '2':
            contactos = obtener_contactos()
            print("\nLista de contactos:")
            for contacto in contactos:
                print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}")
        
        elif opcion == '3':
            contacto_id = int(input("ID del contacto a eliminar: "))
            eliminar_contacto(contacto_id)
            print("Contacto eliminado.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
