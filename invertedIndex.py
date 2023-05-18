from client import Client

def actualizarIndiceInvertido(manager):
	indice_invertido = {}
	for i, registro in enumerate(manager):
		for obj in registro:
			if isinstance(obj, Client):
				nombre = obj.getName()
				if nombre not in indice_invertido:
					indice_invertido[nombre] = []
				indice_invertido[nombre].append(i)
	return indice_invertido

def mostrarIndiceInvertido(manager, indice_invertido):
    print("Índice invertido:")
    for nombre, indices in indice_invertido.items():
        print(f"Registros para el cliente '{nombre}':")
        for indice in indices:
            registro = manager.getIndex(indice)
            print(f"Índice asociado: {indice}")
            for obj in registro:
                print(obj)
            print()

