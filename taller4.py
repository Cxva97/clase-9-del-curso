"""
crear un sistema de contactos
menu agregar contactos
eliminar contactos
editar contactos
mostrar todos los contactos


inicio en menu
   Bienvenida
   opciones ( 1 mostrar , 2 agregar, 3 editar, 4 eliminar, 5 salir)
        1 muestro nomrbres y numeros
            opcion nombre y le pido que me de el nombre para darle el numero / escriba un nombre y yo le doy la respuesta  
        2 Agregar contacto (* ingreso con id 1,2,3)
            solicito nombre, el numero 
            ? numero debe tener 10 digitos
            ? deben ser exclusivamente numeros
        3. Editar contacto
            en base a un id 
            nuevo nombre o nuevo numero
        4 Eliminar contacto
            en base a un id
        5. salir
            mensaje y salir

Se usara funciones, bucles, datos estructurados, try except
"""
def agregarContacto():
    nombre = input("ingrese el nombre y apellido del contacto: ")
    numero = int(input("ingrese el numero de telefono del contacto: "))
    contacto = {
        'id': len(lista_contactos) + 1,
        'nombre': nombre,
        'numero': numero
    }

    lista_contactos.append(contacto)
    print(f"Contacto {contacto} agregado exitosamente.")
def mostrarContactos():
    print("lista de contactos")
    print("N nombre   telefono")
    for contacto in lista_contactos:
        print(f"{contacto['id']}. {contacto['nombre']} {contacto['numero']}")

def editarContacto():
    mostrarContactos()
    id = input("ingrese el id del contacto a editar: ")
    nombre = input("ingrese el nuevo nombre y apellido del contacto: ")
    numero = int(input("ingrese el nuevo numero de telefono del contacto: "))
    for contacto in lista_contactos:
        if contacto['id'] == int(id):
            contacto['nombre'] = nombre
            contacto['numero'] = numero
            print(f"Contacto con id {id} editado exitosamente.")
        else:
            print("No se encontro el contacto con el id proporcionado.")
            return
    

def eliminarContacto():
    mostrarContactos()
    id = input("ingrese el id del contacto a eliminar: ")
    for contacto in lista_contactos: #trabaja con cada contacto en la lista
        if contacto['id'] == int(id): # si el id del contacto es igual al id ingresado
            lista_contactos.remove(contacto) # elimina el contacto de la lista
            print(f"Contacto con id {id} eliminado exitosamente.") 
            return
    print("No se encontro el contacto con el id proporcionado.")

opcion = ""
lista_contactos = [{
    'id': 1,
    'nombre': 'Cesar',
    'numero': '1234567890'
}]
#{
#    'id': 1,
#    'nombre': 'Cesar',
#    'numero': '1234567890'
#}


while opcion != "5" and opcion.lower() != "salir":
    print("Bienvenidos")
    print("1. Mostrar contactos")
    print("2. Agregar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1": # mostrar
        mostrarContactos()
        print(lista_contactos)
    if opcion == "2": # agregar
        agregarContacto()
    if opcion == "3": # editar
        editarContacto()
    if opcion == "4": # eliminar
        eliminarContacto()
    else: # salir
        print("Gracias por usar el sistema de contactos.")
