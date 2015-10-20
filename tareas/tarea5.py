#TAREA: 5
#AUTOR: NOEL CENTENO
#CEDULA: 8-840-2233


lis_super = []
op = 0
num = 0
while op < 4:
	print("""""""""""""""""""""""""""""""""""""""""""")
	print("         1.Agregar productos a lista	     ")
	print("         2.Eliminar Productos de la lista ")
	print("         3.Ver la lista                   ")
	print("         4.Salir                          ")
	print("""""""""""""""""""""""""""""""""""""""""""")
	op = int(input("Introduzca la opcion a realizar: "))
	if op == 1:
			print("Lista de productos de super mercado")
			print("\n(1)Carne","\t(2)Arroz","\t(3)Porotos","\t(4)Lentejas","\t(5)Leche","\n(6)Pan","\t\t(7)Vegetales","\t(8)Embutidos","\t(9)Dulces","\t(10)Sopas\n")
			num == int(input("seleccione el numero del producto a comprar:\n"))
			if num == 1:
				lis_super.append("Carne")
			elif num == 2:
				lis_super.append("Arroz")
			elif num == 3:
				lis_super.append("Porotos")
			elif num == 4:
				lis_super.append("Lentejas")
			elif num == 5:
				lis_super.append("Leche")
			elif num == 6:
				lis_super.append("Pan")
			elif num == 7:
				lis_super.append("Vegetales")
			elif num == 8:
				lis_super.append("Embutidos")
			elif num == 9:
				lis_super.append("Dulces")
			else:
				lis_super.append("Sopas")
	elif op == 2:
			borr == int(input("introduza la posicion que desea eliminar"))
			del lis_super[borr-1]
	elif op == 3:
			print("\n\n\tSU LISTA DE PRODUCTOS A COMPRAR ES:\n")
			print(lis_super)
			