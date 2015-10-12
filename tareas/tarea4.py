minu_e = int(input('Introduzca los minutos: '))

tiem_hora = 0
tiem_dia = 0
minu_rest = 0
hora_rest = 0
if minu_e < 60:
	minutos = minu_e
	print('El resustado de los minutos introducidos equivale en dias a :'+ str(tiem_dia) + '\nen horas a :'+ str(tiem_hora) + '\ny en minutos a :'+ str(minutos))
else:
	if minu_e > 60:
		tiem_hora = minu_e//60
		if minu_e % 60 != 0:
			minu_rest = minu_e-(tiem_hora*60) #aqui estan los minutos restante del sobrante de la hora
		else:
			minu_rest = 0
		hora_rest = tiem_hora
	if tiem_hora > 24:
		tiem_dia = tiem_hora//24
		if tiem_hora % 24 != 0:
			hora_rest = tiem_hora-(tiem_dia*24)
		else:
			hora_rest = 0
	minutos = minu_rest
	horas = hora_rest
	print('El resustado de los minutos introducidos equivale en dias a :'+ str(tiem_dia) + '\nen horas a :'+ str(horas) + '\ny en minutos a :'+ str(minutos))
