import sqlite3
import os

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
    consulta2='''
        SELECT p.nombre_producto, COUNT(*) AS veces
        FROM ventas v
        JOIN productos p ON v.id_producto = p.id_producto
        GROUP BY p.nombre_producto
        ORDER BY veces DESC
        LIMIT 5;
            '''  
    ask2=["¿Cuáles fueron los 5 productos más vendidos por categoría?",consulta2]  
    answer2=ask(cursor,ask2)
    print(answer2)
    #print(f"La sucursal con mas vetas totales fue {answer1[0][1]} con un total de ventas de {answer1[0][2]}")
    print(f"Los 5 productos mas vendidos son {answer2}")
    
    conexion.close()
 
def ask(cursor, ask1):
    cursor.execute(ask1[1])
    filas = cursor.fetchall()
    filas_array = [list(fila) for fila in filas]
    return filas_array


if __name__ == "__main__":
    main()