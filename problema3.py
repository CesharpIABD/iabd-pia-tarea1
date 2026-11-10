def procesar_conjuntos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    return {
        "interseccion": conjunto1.intersection(conjunto2),
        "union": conjunto1.union(conjunto2),
        "diferencia_simetrica": conjunto1.symmetric_difference(conjunto2)
    }

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    print(procesar_conjuntos(lista1, lista2))
