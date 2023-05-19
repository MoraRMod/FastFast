import zipfile
import pickle
import os

def comprimir(gerente):
    gerenteSerializado = pickle.dumps(gerente)

    with zipfile.ZipFile("gerente.zip", "w") as archivo:
    	archivo.writestr("gerente.pickle", gerenteSerializado)

def descomprimir(archivo, directorioDestino = None):
	if directorioDestino is None:
		directorioDestino = os.getcwd()
    
	with zipfile.ZipFile(archivo, "r") as archivo:
		archivo.extractall(directorioDestino)
