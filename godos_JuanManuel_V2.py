#Juan Manuel Benítez Campmany

def nombreBebe(listaReyes, letraInicial):
	nombres = []
	for rey in listaReyes:
		if letraInicial.lower() == rey.lower()[0]:
			nombres.append(rey)
	if len(nombres) == 0:
		return "No existe ningun rey godo con la inicial " + letraInicial.upper()
	else:
		return nombres