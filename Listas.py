#Estructura [1,"hola",False]
# Sobre listas 
# **** La forma de contar dentro de una lista es la siguiente:
#  0  1   2   3     4   
#["h",23,51,False,True]
#siempre comienza desde el numero 0


colors = ["rojo","verde","naranja" ["gris","dorado"]] #puede haber una lista dentro de otra

number_list = list(1,2,3,4)
#print (numbers_list)

# r=list(range(1,10))#range = de que valor a que valor quiero crear la lista ,esta se guarda en la variable r
# print(r)

print(dir(colors)) 
# info de todo lo que se puede hacer con una lista

print(len(colors)) 
# cuenta los elementos de la lista

print(colors[2]) 
#obtener la segunda posicion de una lista

print("green" in colors) 
#devuelve T o F si el valor ingresado (en este caso green) esta en la lista

colors[1] = "yellow" #cambiar el valor elegido = el valor nuevo

colors.append ("violet")
 #se agrega a la ultima posicion de la lista , lo ingresado en el ()
print(colors)

colors.extend(["blue","gold"]) 
 # agrega multiples elementos ,pero se guardan como elementos y no como tuplas ni listas

colors.insert(-1,"silver") # inserta  en el (indice de la lista, el valor ) (-1 indica el final de la lista)

colors.insert(len(colors),"brown") #agrega el valor a lo ultimo de la lista
print(colors)


colors.pop() #se elimina el ultimo elemento de la lista
print(colors)

colors.remove("green")#borra el unicamente el valor ingresado
print()

colors.pop(1) # borra el indice indicado

colors.clear() #Limpia toda la lista


colors.sort(reverse=True) #ordena los numeros en este caso albafeticamente a la inversa
print(colors)

colors.index("red") # muestra la posicion del valor ingresado en la lista
colors.count("red)") # cuenta las veces que el valor ingresado esta en la lista
