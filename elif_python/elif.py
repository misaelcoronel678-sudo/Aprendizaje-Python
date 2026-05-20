ingreso_mensual = 85000
gasto_mensual = 90000
if ingreso_mensual >= 10000:
	if ingreso_mensual - gasto_mensual < 0:
		print ('amigo estas en deficit')
	elif ingreso_mensual - gasto_mensual > 3000:
		print ('Estas bien Economicamente')
	else:
		print ('y la verdad que estas gastando una banda')
elif ingreso_mensual >= 1000:
	print ('estas bien en latinoamerica')
elif ingreso_mensual >= 650:
	print ('estas bien en Paraguay')
elif ingreso_mensual >= 500:
	print ('estas bien en Argentina')
elif ingreso_mensual >= 200:
	print ('estas bien en Venezuela')
else:
	print ('sos pobre my brother')