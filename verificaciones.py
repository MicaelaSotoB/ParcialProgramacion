def validar_existencia(opcion, lista):
    es_valido = True
    if opcion < 0 or opcion >= (len(lista)):
        es_valido = False
    return es_valido

def consultar_opcion():
    opcion = int(input("Ingrese opción correspondiente: "))
    while opcion < 0 or opcion > 9:
        print("Opción no válida")
        opcion = int(input("Ingrese opción correspondiente: "))
    return opcion