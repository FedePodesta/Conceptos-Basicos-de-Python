#VARIABLE UASADA EN LOS SIGUIENTES  EJEMPLOS
myString = "Hello World"

# print (dir(myString)) #la consola muestra todo lo que se puede realizar con un dato de tipo "String"

print(myString.upper()) # convierte todos los string en Mayuscula,
print(myString.lower()) # """""""""""""""""""""""""""" Minuscula,
print(myString.swapcase())# """"""""""  UnAmAyUsCuLaYuNaMiN
print(myString.capitalize())# Convierte la 1er letra de cada palabra en Mayuscula(de la primera palabra)

print (myString.replace("hello","Bye"))
 # reemplaza la primera palabra del parentesis luego de .replace y la reemplaza por la segunda 

print (myString.count("o")) 
# cuenta los caracteres que se le indiquen en el parentesis

print (myString.startswith("hola")) 
# si el texto empieza con la palabra indicada en el parentesis devuelve un True, si no False(funciona tambien ingresando una letra o el inicio de una palabra)

print (myString.endswith("world")) 
#lo contrario a lo anterior, me indica si mi texto termina con los datos ingresados en el parentesis

myString (myString.split()) #Separa los valores por el valor que se ingrese dentro del () (reemplaza la letra por un espacio EN UNA LISTA)

print(myString.find("o"))# busca cuantos valores [ingresados dentro del ()] hay y devuelve por consola dicho numero

print (len(myString)) # imprime el numero total de caracteres que tenga mi variable

print (myString.index("e")) # indica en que posicion se encuentra el valor ingresado en el ()


print(myString.isnumeric()) # saber si la variable es numerica
print(myString.isalpha())  # saber si la variable es alpha numerico

print(myString[4]) # imprime la posicion declarada en el [corchete]
print(myString[-2])
print(myString[2])

#CONCATENACIÓN
name="Federico"


print ("My name is" + name) 
print(f"My name is{name}") #variación para concatenar
print ("My Name is {0}".format(name)) # Variación