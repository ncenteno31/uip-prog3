#Quiz 2
#Nombre: NOEL CENTENO
#Cedula: 8-840-2233



for i in range(4):


	print("monto de la compra: ")
	monto = int(input())
	
	if monto >= 500:
		descuento = monto * 0.30 
		total = monto - descuento
		print ("el total es " + str(total))

	if monto <500 and monto >=200:
		descuento = monto * 0.20 
		total = monto - descuento
		print ("el total es " + str(total))
	if monto <200 and monto >=100:
		descuento = monto * 0.10 
		total = monto - descuento
		print ("el total es " + str(total))
	else: 
		print ("el total es " + str(monto))





