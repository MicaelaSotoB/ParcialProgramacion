from verificaciones import *

def menu():
    print("0. Salir")
    print("1. Cargar stock de insumos")
    print("2. Ver depositos con stock mayores a 5000")
    print("3. Ver insumos con stock mayor a 3000")
    print("4. Ver insumo con mayor cantidad de stock")
    print("5. Registrar ventas ")
    print("6. Ver informe de ventas por deposito")
    print("7. Ver informe por insumo de cada deposito")
    print("8. Informe de reposicion de stock")
    print("9. Porcentaje de stock de cada insumo respecto al total general")

def cargar_stock(matriz, depositos, tipos_insumos):
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            stock=int(input(f"Ingrese el stock de insumo {tipos_insumos[j]} en el {depositos[i]}: "))
            matriz[i][j]=stock

def mayor_stock_total_depositos(matriz, depositos):

    for i in range(len(matriz)):
        total_depositos=0
        for j in range(len(matriz[i])):
            total_depositos += matriz[i][j]
        if total_depositos > 5000:
            print(f"Total depósito {depositos[i]}: {total_depositos}")

def mayor_stock_total_insumos(matriz, tipos_insumos):
    
    for i in range(len(matriz[0])):
        total_insumos = 0
        for j in range(len(matriz)):
            total_insumos += matriz[j][i] 
        if total_insumos > 3000:
            print(f"Insumo {tipos_insumos[j]} con mayor cantidad de unidades en depósitos : {total_insumos}")


def mayor_unidad_insumo(matriz, depositos, tipos_insumos):
    mayor_unidad = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mayor_unidad:
                mayor_unidad = matriz[i][j]
                mayor_unidad_deposito = i
                mayor_unidad_insumo = j
    print(f"Depósito con mayor unidad: {depositos[mayor_unidad_deposito]}")
    print(f"Insumo de mayor unidad en el depósito: {tipos_insumos[mayor_unidad_insumo]}")
    print(f"Stock del insumo: {mayor_unidad}")



def cargar_ventas(ventas, deposito, insumo, precio=100):
    ventas[deposito][insumo] = precio


def registrar_ventas(ventas, depositos, insumos):
    deposito = consultar_deposito(depositos)
    insumo = consultar_insumo(insumos)
    
    eleccion=int(input("1. Ingresar precio- 2.Dejar precio Predeterminado: "))
    if eleccion==1:
        precio = int(input("Ingrese precio del insumo seleccionado: "))
        cargar_ventas(ventas, deposito, insumo, precio)
    else:
        cargar_ventas(ventas, deposito, insumo)


def consultar_deposito(depositos):
    for i in range(len(depositos)):
        print(f"{i+1}. {depositos[i]}")
    deposito = int(input("Ingrese depósito: "))
    
    es_valido = validar_existencia(deposito, depositos)
    while not es_valido:
        print("Ingrese depósito válido")
        deposito = int(input("Ingrese depósito: "))
        es_valido = validar_existencia(opcion, lista)

    return deposito-1

def consultar_insumo(insumos):
    for i in range(len(insumos)):
        print(f"{i+1}. {insumos[i]}")
    insumo = int(input("Ingrese insumo: "))
    
    es_valido = validar_existencia(insumo, insumos)
    while not es_valido:
        print("Ingrese insumo válido")
        insumo = int(input("Ingres insumo: "))
        es_valido = validar_existencia(opcion, lista)
    
    return insumo-1


def calcular_stock_total_depositos(stock_insumos):
    stocks_totales = [0]*len(stock_insumos)

    for i in range(len(stock_insumos)):
        total_depositos=0
        for j in range(len(stock_insumos[i])):
            total_depositos += stock_insumos[i][j]
        stocks_totales[i] = total_depositos
    return stocks_totales

def mostrar_unidades_faltantes(stock_insumos, depositos, tipos_insumos, minimo = 500):
    stock_totales = calcular_stock_total_depositos(stock_insumos)
    for i in range(len(stock_totales)):
        print(f"Depósito {depositos[i]} - Total: {stock_totales[i]}")
        for j in range(len(stock_insumos[i])):
            if stock_insumos[i][j] <= minimo:
                unidades_faltantes = (stock_insumos[i][j] - minimo) * -1
                print(f"Producto {tipos_insumos[j]} - Unidades faltantes para llegar al mínimo: {unidades_faltantes}")
        print("--------------------")

