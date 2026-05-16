#creando lista ( se puede modificar)
Lista = ['Misael Coronel', 'Idioma Guarani', False, 1.75]
#esto es valido
Lista [2] = True
print (Lista [2])

#creando una tupla (no se puede modificar)
tupla=('eduar correa','Mixal',True,3.16)
#esto no es valido
#tupla [1] = 'Miza'
print (tupla [1])

#creando conjunto (set) (no se accede a un elemento por indice, no almacena datos duplicados)
conjunto = {'hola','hola'}
#conjunto [0] = 'chao'
#print (conjunto [0]) -> no se puede acceder al elemento
print (conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
'nombre' : 'Misael Coronel',
'colegio' : 'Colegio Nacional Prof Encarnacion Alum de Vive',
'pais' : 'Paraguay',
'año' : 2026,
}
print (diccionario['pais'])
print (diccionario ['colegio'])
print (diccionario ['año'] + 2)

