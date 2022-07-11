{
    "name":"book",
    "quantity": 3,
     "price" : 4.99
}

person = {
    "first_name":"ryan",
    "last_name" : "ray"
}

print(type(person)) # tipo diccionario
print(dir(person))

print(person.keys()) #muestra las claves
print(person.items()) # muestra los items

#del person #elimina person junto a sus items y claves 
print(person)

products = [
    {"name":"book","price":10.99}, #utilizar los diccionarios dentro de listas
    {"name" : "laptop","price":1000}
]
   
print(products)