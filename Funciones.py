## Funciones ##

def hello(name="Person" ): #el ="person " es un parametro por defecto si el usuario no agrega valores
    print("hello" + name)


hello("carlos") #invocar la funcion para que se ejecute la funcion (en este caso hello) y sus instrucciones
# dentro de los () puedo ingresar un dato el cual la funcion lo recibe y lo utiliza
hello("anibal")
hello("federico") # se ejecuta todo el codigo de la funcion con los valores que le damos
hello("arturo")  # sin necesidad de ejecutar todo el codigo

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10,30))
print(add(600,10))
len("hello")


add1 = lambda numberOne, numberTwo: numberOne+numberTwo

add1(10,30)

print(add1(10,30))

