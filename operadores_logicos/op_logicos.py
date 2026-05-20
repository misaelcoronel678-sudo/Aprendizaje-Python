#AND (Se tienen que cumplir las dos condiciones si no se cumplen las dos es False)

Resultado = True & True #Devolver True
Resultado2 = True & False #Devolver False
Resultado3 = True & False #Devolver False 
Resultado4 = False & False #Devolver False

#OR (Con tal de que se cumpla una condicion es True)

Resultado5 = True | True #Devolver True
Resultado6 = True | False #Devolver True
Resultado7 = False | True #Devolver True
Resultado8 = False | False #Devolver False

#NOT (Invierte el Valor)

Resultado9 = not 2 > 1000 #Devolver True
Resultado10 = not 1000 > 2 #Devolver False

print (Resultado10)
