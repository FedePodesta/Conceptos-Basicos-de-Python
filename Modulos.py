# own modules (propios modulos)
# thirdy party modules ( internet bibliotecas)
# python modules (modulos que nos da python)

#index de los modulos de python https://docs.python.org/3/py-modindex.html
# modulos de la comunidad listados https://pypi.org/
#si googleo el modulo nos da una extensa explicacion de la misma y su documentación

import datetime
from lib2to3.pytree import convert
from mimetypes import init 

print(datetime.date.today())
print(datetime.timedelta(minutes=70))

#tambien puedo traerlo directamente

from datetime import timedelta , date
print(datetime.timedelta(minutes=100))
print(date.today())


#importamos nuestro propio modulo desde esta carpeta llamado Fmath 
import Fmath

Fmath.add(1,2)
Fmath.substract(1,2)

# from colorama import Fore,Style, init #desde el cmd junto con la pagina pypi se instala la libreria
# init(convert=True)
# print(Fore.RED + "Hello World")
