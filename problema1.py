def procesar_lista(enteros):
    return sorted(list(set([x for x in enteros if x >= 0])))


if __name__ == "__main__":
    print(procesar_lista([1, 3, -4, 12, 6, -15, 6]))
