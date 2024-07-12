import csv
import os
import random

nombres =["Juan Pérez2","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 
sueldo_de_trabajadores = []

with open("sueldos_examen.csv", "w", newline="", encoding="utf-8") as archivo:
    archivo.write("nombre,sueldo,desc,afp,sueldo_liquido")

def sueldos_aleatorios():
    global sueldo_de_trabajadores
    for a in sueldo_de_trabajadores:
        sueldo_de_trabajadores = [{"nombre": a, "sueldo": random.randint(300000 , 2500000)}]

def sueldos_aleatorios():
    global sueldo_de_trabajadores
    sueldo_de_trabajadores = [{"nombre": nombre, "sueldo": random.randint(300000, 2500000)} for nombre in nombres]
    print("sueldos asignados aleatoriamente.")

def clasificarSueldos():
    global sueldo_de_trabajadores
    b = []
    c = []
    d = []
    
    for a in sueldo_de_trabajadores:
        if a["sueldo"] < 800000:
            b.append({a["nombre"]:a["sueldo"]})
        elif a["sueldo"] <= 2000000:
            c.append({a["nombre"]:a["sueldo"]})
        else:
            d.append({a["nombre"]:a["sueldo"]})
    print("Sueldos menores a 800000")
    print(b)
    print("Sueldos entre 800000 y 2000000")
    print(c)
    print("Sueldos mayores a 2000000")
    print(d)
    
    
def estadisticas():
    if not sueldo_de_trabajadores:
        print("primero debes generar sueldos aleatorios.")
        return

    while True:
        
        print("1.- mostrar el sueldo mayor")
        print("2.- Sueldo más bajo" )
        print("3.- promedio de sueldos")
        print("4.- media geométrica")
        

        try:
            opcion = int(input("Seleccione una opcion "))
        except ValueError:
            print("error: Ingresa un numero válido")
            continue

        if opcion == 1:
            sueldo_mayor = max(sueldo_de_trabajadores, key=lambda x:x["sueldo"])
            print(f'Sueldo mayor: {sueldo_mayor["nombre"]}: {sueldo_mayor["sueldo"]}')
        elif opcion == 2:
            sueldo_menor = min(sueldo_de_trabajadores, key=lambda x:x["sueldo"])
            print(f'Sueldo menor: {sueldo_menor["nombre"]}: {sueldo_menor["sueldo"]}')
        elif opcion == 3:
            total_sueldos = sum(persona["sueldo"] for persona in sueldo_de_trabajadores)
            promedio_sueldos = total_sueldos / len(sueldo_de_trabajadores)
            print(f"Promedio de sueldos: {promedio_sueldos}")
        elif opcion == 4:
            
            
            break
        else:
            print("Opción inválida Por favor selecciona una opción del 1 al 4")

def reporte_de_sueldos():
    if not sueldo_de_trabajadores:
        print("primero debes generar sueldos aleatorios.")
        return

    with open("sueldos_examen.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        for persona in sueldo_de_trabajadores:
            descuento = 0.07 * persona["sueldo"]
            afp = 0.12 * persona["sueldo"]
            sueldo_liquido = persona["sueldo"] - descuento 
            writer.writerow([persona["nombre"], persona["sueldo"], descuento,  sueldo_liquido])
while True:
    print("1 .-asignar sueldos aleatorios ")
    print("2.- clasificar sueldos ")
    print("3.-ver estadísticas ")
    print("4.-reporte de sueldos ")
    print("5 .-Salir")

    try:
        opcion = int(input("Seleccione una opcion "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

    if opcion == 1:
        sueldos_aleatorios()
    elif opcion == 2:
        clasificarSueldos()
    elif opcion == 3:
        estadisticas()
    elif opcion == 4:
        reporte_de_sueldos()
    elif opcion == 5:
        print("Saliendo del programa")
        break
    else:
        print("")
