from funciones import *
from verificaciones import *

depositos=["Rosario", "Cordoba", "Salta", "Bahia blanca"]
tipos_insumos=["Arduino UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]

ventas=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

stock_insumos = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

menu()
opcion=consultar_opcion()
while opcion != 0:
    match opcion:
        case 1:
            cargar_stock(stock_insumos, depositos, tipos_insumos)
        case 2: 
            mayor_stock_total_depositos(stock_insumos, depositos)
        case 3:
            mayor_stock_total_insumos(stock_insumos, tipos_insumos)
        case 4:
            mayor_unidad_insumo(stock_insumos, depositos, tipos_insumos)
        case 5: 
            registrar_ventas(ventas, depositos, tipos_insumos)
        case 6:
            print("")
        case 7:
            print("")
        case 8:
            mostrar_unidades_faltantes(stock_insumos, depositos, tipos_insumos)
    input("ENTER para continuar")
    menu()
    opcion=consultar_opcion()