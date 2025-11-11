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
    pass

def mostrarContactos():
    pass

def editarContacto():
    pass

def eliminarContacto():
    pass

opcion = ""
lista_contactos = []
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
    if opcion == "2": # agregar
        agregarContacto()
    if opcion == "3": # editar
        editarContacto()
    if opcion == "4": # eliminar
        eliminarContacto()
    else: # salir
        print("Gracias por usar el sistema de contactos.")


