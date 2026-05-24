cadena1 = 'hola Soy Misa'
cadena2 = '123456'
cadena3 = 'Misael'

#La formula para los metodos es DATO.METODO ( )

#dir es una funcion que nos dice que podemos hacer con ese elemento que le mandamos
resultado = dir (cadena1) 


#upper convierte a mayusculas
mayus = cadena1.upper () 
mayus2 = 'hola cracks mi nombre es donatho'.upper ()

#Lower convierte a Minusculas
minusc = 'HOLA SOY MISAEL CORONEL'.lower ()

#capitalize convierte la prinera letra en Mayuscula
primera_letra_mayusc = 'hola como estan'.capitalize ()

#find busca una cadena en otra cadena si no hay coincidencias devuelve -1
busqueda_find = cadena1.find ('M')

#index busca una cadena en otra cadena, si no hay coincidencias nos devuelve una excepcion
busqueda_index = cadena1.index ('S')

#isnumeric ve si es numerico entonces devuelve True si no lo es devuelve False
es_numerico = cadena2.isnumeric ()

#si es alfanumerico, devolvemos True si no devolvemos False
es_alfanumerico = cadena3.isalpha ()

#buscamos una cadena en otra cadena devuelve la cantidad de veces que coincide un caracter
contar_coincidencias = cadena1.count ("hola")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len (cadena1)

#verifica si la cadena empieza con la letra que le decimos si empieza con esa letra muestra True si no muestra False
empiesa_con = cadena1.startswith ('h')

#verifica si la cadena empieza con la letra que le decimos si empieza con esa letra muestra True si no muestra False 
termina_con = cadena1.endswith ('sa')

#reemplaza un pedazo de la cadena dada por otra cadena dada
cadena_nueva = cadena1.replace ("sa","so")

#separa cadenas con las cadenas que le pasamos y lo convierte en listas
cadena_separada = cadena1.split (' ')

print (cadena_separada)