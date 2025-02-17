import sqlite3
import os
import csv

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, 'BasesDeDatos', 'sales')
    conexion = sqlite3.connect(path)
    cursor = conexion.cursor()
    consulta1='''
        SELECT s.id_sucursal, s.nombre_sucursal, SUM(v.precio_total) AS TotalVentas
        FROM ventas v
        INNER JOIN sucursales s ON v.id_sucursal = s.id_sucursal
        GROUP BY s.id_sucursal, s.nombre_sucursal
        HAVING SUM(v.precio_total) = (
            SELECT MAX(TotalVentas)
            FROM (
                SELECT v.id_sucursal, SUM(v.precio_total) AS TotalVentas
                FROM ventas v
                GROUP BY v.id_sucursal
            ) AS Subconsulta
        );
            '''  
    ask1=["¿Cuál fue la sucursal con más ventas totales (suma del precio total) durante el último mes?",consulta1]  
    answer1=ask(cursor,ask1)
    print(ask1[0])
    print(f"la sucursal {answer1[0][1]} con unas ventas {answer1[0][2]} es la de mayor ventas del último mes")    
    answer1.insert(0,["id_sucursal","nombre_sucursal","ventas totales"])
    create("SucursalMasVentas.csv",answer1)
    consulta2='''
        SELECT p.id_producto,p.nombre_producto, COUNT(*) AS veces
        FROM ventas v
        JOIN productos p ON v.id_producto = p.id_producto
        GROUP BY p.nombre_producto
        ORDER BY veces DESC
        LIMIT 5;
            '''  
    ask2=["¿Cuáles fueron los 5 productos más vendidos por categoría?",consulta2]  
    answer2=ask(cursor,ask2)    
    print(ask2[0])    
    print(f"Los 5 productos mas vendidos son:")
    for values in answer2:
        unidad_plural = "unidad" if values[1] == 1 else "unidades"
        print(f"producto {values[0]} {unidad_plural} {values[1]}")
    answer2.insert(0,["id_producto","nombre_producto","cantidad"])
    create("ProductoMasVendidosPorCategoria.csv",answer2) 
    consulta3='''
        SELECT s.id_sucursal,s.nombre_sucursal,v.fecha,v.precio_total
        FROM ventas v
        JOIN sucursales s ON v.id_sucursal = s.id_sucursal
        GROUP BY v.fecha,v.id_sucursal
        ORDER BY v.fecha,v.precio_total DESC
            '''  
    ask3=["Calcula las ventas totales por día, agrupadas por sucursal.",consulta3]  
    print(ask3[0])
    answer3=ask(cursor,ask3)
    print("Las ventas totales por día son:")
    for value in answer3:
        print(f"{value[1]} {value[0]} total: {value[2]}")
    answer3.insert(0,["id_sucursal","nombre_sucursal","fecha","ventas totales"])
    create("VentasPorSucursales.csv",answer3) 
    conexion.close()
 
def ask(cursor, ask):
    cursor.execute(ask[1])
    filas = cursor.fetchall()
    filas_array = [list(fila) for fila in filas]
    return filas_array

def create(filename,data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)        
        writer.writerows(data)
    print(f"Archivo '{filename}' creado con éxito.")

if __name__ == "__main__":
    main()