foods = ["apples","bread","cheese", "milk"]

for food in foods:      #en la lista de alimentos quiero ver todos los elementos
    if food =="cheese":  #si comida es igual a queso 
        break              # se termina el for
        #continue  cuando llega a queso, lo "saltea" y sigue con la lista
    print(food)



for number in range (1,8): #para cada numero en el rango de 1 a 8
    print(number)  # imprimelo

for letter in "hello": # para letras en hello
    print (letter)  # imprimir letter ( imprime cada letra en su linea )

    count = 4

while count <= 10: # mientras el contador sea igual menor a 10 , realiza la accion (y se repite)
    print(count)   
    count+= 1  # sumo 1  para incrementar el contador y asi hacer que el ciclo while termine  

    