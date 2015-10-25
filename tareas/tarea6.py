#Tarea 6
#Autor: Noel Centeno
#Cedula: 8-840-2233

ajedrez = 0
atletismo = 0
baloncesto = 0
futbol = 0
karate = 0
natacion = 0
volleyball =0
flag = 0
pingp = 0
otros = 0
for x in range (10):
	nomb = input('Introduzca su nombre\n')
	print('\n\n\t\t!!!LISTA DE DEPORTES!!!')
	print("\n(1)Ajedrez","\t(2)Atletismo","\t(3)Baloncesto","\t(4)Futbol","\t(5)Karate","\n(6)Natacion","\t(7)Volleyball","\t(8)Flag","\t(9)Ping Pong","\t(10)Otros\n")
	op = int(input('Introduzca el numero de su deporte favorito '))
	if op == 1:
		print('El deporte favorito de ' +nomb+' es Ajedrez')
		ajedrez = ajedrez+1
	elif op == 2:
		print('El deporte favorito de ' +nomb+' es Atletismo')
		atletismo = atletismo+1
	elif op == 3:
		print('El deporte favorito de ' +nomb+' es Baloncesto')
		baloncesto = baloncesto+1
	elif op == 4:
		print('El deporte favorito de ' +nomb+' es Futbol')
		futbol = futbol+1
	elif op == 5:
		print('El deporte favorito de ' +nomb+' es Karate')
		karate = karate+1
	elif op == 6:
		print('El deporte favorito de ' +nomb+' es Natacion')
		natacion = natacion+1
	elif op == 7:
		print('El deporte favorito de ' +nomb+' es Volleyball')
		volleyball = volleyball+1
	elif op == 8:
		print('El deporte favorito de ' +nomb+' es Flag')
		flag = flag+1
	elif op == 9:
		print('El deporte favorito de ' +nomb+' es Ping Pong')
		pingp = pingp+1
	elif op == 10:
		print('El deporte favorito de ' +nomb+' no es ninguno de los anteriores')
		otros = otros+1
	else:
		print('el dato introducido no es valio')

print('\n\n\t\t!!!Resultado de la encuesta!!!')
print('-Ajedrez\t\t' +str(ajedrez)+ '\n-Atletismo\t\t' +str(atletismo)+ '\n-Baloncesto\t\t' +str(baloncesto)+ 
	'\n-Futbol\t\t\t' +str(futbol)+ '\n-Karate\t\t\t' +str(karate)+ '\n-Natacion\t\t' +str(natacion)+ '\n-Volleyball\t\t' +str(volleyball)+ 
	'\n-Flag\t\t\t' +str(flag)+ '\n-Ping Pong\t\t' +str(pingp)+ '\n-Otros\t\t\t' +str(otros)+ '\n\n')