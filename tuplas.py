#estructura de una tupla

# x = (1,2,3)
# print(type(x))
# months = ("Enero","Febrero", "Marzo")

# y = tuple((1,2,3))  #variacion
# print(dir(x)) # info de tuplas

# x = (1,) # no puedo hacer una tupla de un solo elemento, si quiero hacerlo se coloca una coma
x = (1,2,3,4,5,6)
print(type(x))
print(x[3]) # ver el valor en el indice colocado
#no se pueden modificar los elementos de la tupla

# del x #borra toda la tupla

locations = {
    (35.12312, 39.000):"Tokyo", #uso de tupla en una biblioteca por ejemplo coordenadas
    (35.12312,39000): "Berlin"
}
