import pickle

def serializar(objeto, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(objeto, archivo)

def deserializar(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        objeto = pickle.load(archivo)
    return objeto
