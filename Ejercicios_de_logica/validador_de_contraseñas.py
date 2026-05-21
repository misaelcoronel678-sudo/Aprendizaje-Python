'''​El problema: Los profesores necesitan registrarse en tu sistema,
 pero no pueden usar cualquier contraseña. Tenés que crear un script
 que evalúe si una contraseña es segura.

​Lo que tenés que hacer: * Pedirle al usuario mediante un input() que 
ingrese una contraseña.

​Comprobar las siguientes reglas usando condicionales:
​Debe tener como mínimo 8 caracteres (Podés usar len(password) para saber 
el largo).

​No puede contener la palabra "123" ni "abc" adentro.

​Debe terminar con un signo de exclamación ! o un punto ..

​Si cumple todo, imprimí "Contraseña válida". Si falla en algo, 
decile exactamente en qué falló.'''

contraseña = input("Ingrese la contraseña: ")
minusc = contraseña.lower()
contraseña_caracteres = len(contraseña)
palabras_no_admitidas = minusc.count ("abc")
palabras_no_admitidas2 = minusc.count ("123")
lista_caracteres = list(contraseña)
final_contraseña = lista_caracteres[-1]
caracter_1 = "!"
caracter_2 = "."


if contraseña_caracteres < 8:
    print ("la contraseña es demaciado corta Ingrese una con almenos 8 caraceres")
elif palabras_no_admitidas > 0 or palabras_no_admitidas2 > 0:
    print ("No se permiten tener abc ni 123 en la contraseña")
elif final_contraseña != caracter_1 and final_contraseña != caracter_2:
    print("La contraseña debe de terminar en ! o en .")
else:
    print("contraseña valida")
