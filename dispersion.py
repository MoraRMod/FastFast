from collections.abc import Iterable


def dispersar(gerente):
    dispersado = [[] for _ in range(len(gerente.getIndex(0)))]

    for i in range(len(gerente)):
        for obj in gerente.getIndex(i):
            indice = hash(obj) % len(gerente)
            dispersado[indice].append(obj)

    gerente._Manager__gerente = dispersado

def mostrarDispersado(gerente):
    for i, sublist in enumerate(gerente.getIndex(0)):
        print(f'Índice {i}')
        if isinstance(sublist, Iterable):
            for obj in sublist:
                print(obj)
        else:
            print(sublist)
        print("\n")