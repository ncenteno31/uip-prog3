# quiz 3
# Nombre: Noel Centeno
#
# Dado un intervalo de tiempo en segundos, calcular los segundos restantes
# que corresponden para convertirse exactamente en minutos.
# Este programa debe funcionar para 5 oportunidades

for i in range(5):
	seg= int(input(" Introduzca un Numero para Calcular "))

	cont= 60
	while seg > cont:
		cont=cont+60


	min= cont-seg

	print(" Faltan " + str(min) + " segundos ")
