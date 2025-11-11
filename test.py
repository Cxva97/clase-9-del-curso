# POO programacion orientada a objetos
# es paradigma de programacion que busca oritentar el codigo a aplicativos reales u objetos

"""
Clases => son plantillas 
    atributos => propiedades
    estaticos => por defecto tiene todos los objetos
    dinamicos => se crean en base a los objetos
    metodos => funciones dentro de las clases
objetos => son instancias de las clases. Creacion en base a las clases"""

class auto():
    def __init__(self, color): # metodo constructor
        self.color = color # atributo dinamico 
    llantas = 4 # atributo estatico

    def encender(self):
        print("el auto se ha encendido")


    def __str__(self): # metodo especial para representar el objeto como cadena
        return self.color 

auto1= auto("rojo") # creacion del objeto auto1
auto2= auto("blanco") # creacion del objeto auto2

print(auto1.color)
print(auto1.llantas)

print(auto2.color)
print(auto2.llantas)
auto1.encender()
auto2.encender()

"""PILARES
1. herencia
2. abstraccion
3. polimorfismo
4. encapsulamiento


"""

