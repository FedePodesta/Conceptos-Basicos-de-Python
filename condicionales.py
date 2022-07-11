#condicionales
#<mayor | > menor | and | or | == (igual) | != distinto | <= (mayorigual) >= (menorigual)

x = 20


if x < 30:                          # si esta condicion es True
    print("x es menor a 30")        # ejecuta esta instruccion
elif x == 25:                       #si la primer condicion es false, verifica la segunda       
#                                    #condicion(se pueden poner multiples condiciones)
    print("x es igual a 25")
else:                               # si es False
    print("x es mayor a 30")        # ejecuta esto


name ="john"
lastname= "carter"

if name == "John":                       
    if lastname =="carter":#if anidado, se tienen que cumplir las dos , si no va al segundo else
        print("you are john Carter")
    else: ("you are not jhon")
else:
    print("error")

y=4

if x>2 and x< 10:#En AND se tienen que cumplir ambas condiciones si no será FALSE
    print("x es mayor a 2 y menor a 10")

if x > 2 or x <= 20:#En OR mientras se cumpla 1 condicion el resultado será true
    print("x es mayor a 2 o es menor a 20")

if (not (x == y)):
    print("x no es igual a y")
