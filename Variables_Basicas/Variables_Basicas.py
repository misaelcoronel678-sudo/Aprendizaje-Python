#Definiendo Variables
a=6
b=7
#Concatenar 
c= a+b
print (c)

#Definiendo Variables con CameCase
NombreDelUsuario= "Misael"
 #Definiendo Variables con Snake_Case
Apellido_Del_Usuario= "Coronel"
#Concatenando con +
bienvenida="Hola " + NombreDelUsuario+ " "  + Apellido_del_usuario + " ¿Como estas?"
print (bienvenida)

#Definiendo Variables
Eres= "Hombre"
Edad= "15"
#Concatenar con f-String
Saludo = f"Ahh entonces eres {Eres} y tienes {Edad} Años de edad"
print (Saludo)

#Operadores de Pertenencia ( in / not in )
print ('dad' in Saludo) #Verdadero
print ('fulano' in Saludo) #Falso

print ('algo' not in bienvenida)#Verdadero
print ('Hola' not in bienvenida) #Falso
