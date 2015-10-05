num = int(input('Introduzca la cantidad de numeros de la piramide que desea ver: '))
for x in range(num):
	piramide = (x*(x+1))/2
	print ('Los nuemeros de la piramide  '+ str(piramide))
	x+1