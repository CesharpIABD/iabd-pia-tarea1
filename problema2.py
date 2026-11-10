def contar_frecuencias(palabras, ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        contenido = file.read().lower()
    for char in '.,;:!?¿¡()[]{}"\'«»“”\n':
        contenido = contenido.replace(char, " ")
    palabras_contenido = contenido.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra.lower()] = palabras_contenido.count(palabra.lower())
    return frecuencia

if __name__ == "__main__":
    lista_palabras = ["python", "programación", "diccionario", "función", "archivo", "java" ,"java"]
    ruta = "texto.txt"
    print("Lista de palabras y sus frecuencias de forma ordenada por la palabra:")
    for palabra, veces in sorted(contar_frecuencias(lista_palabras, ruta).items()):
        print(" - " + palabra + ": " + str(veces))
