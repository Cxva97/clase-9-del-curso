#feedback
# try except
# es el manejo de errores

"""
NameError = Variable no declarada 
TypeError = Operacion no posibles 
FileNotFound = Archivono encontrado
SyntaxErro = codigo mal escrito
ValueError = Conversiones ej text a int 
IndexError =  si trabajamos con listas o tuplas no hay la posicion
KeyError = Si trabajamos con dict no hay key llave
ZeroDivisionError = No se puede dividir para cero
Exception
"""


try : 
    print("hola")
except  Exception as e:
    print("Ha ocurrido un error: ", e) 
finally:
    print("ejecuta siempre")


lista= [1,2]
print(lista[3])

diccionario={
    'nombre' : "cesar"
}

print(diccionario['edad'])