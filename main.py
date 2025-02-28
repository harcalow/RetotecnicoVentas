import csv
import os
import sqlite3

def main():
    database('create')
    read_csv('ventas.csv')
    read_csv('sucursales.csv')
    read_csv('productos.csv')
    
def database(function,data=[]):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, 'BasesDeDatos', 'sales')
    conn = sqlite3.connect(path) 
    if (function=='create'):
        create_table(conn.cursor())
    elif(function=='save_ventas.csv'):
        save_table_sales(conn.cursor(),data)
    elif(function=='save_sucursales.csv'):
        save_table_branches(conn.cursor(),data)
    elif(function=='save_productos.csv'):
        save_table_products(conn.cursor(),data)
    conn.commit()
    conn.close()

def create_table(cursor):
    cursor.execute('PRAGMA foreign_keys = ON;')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY,
            nombre_producto VARCHAR(255) NOT NULL,
            categoria VARCHAR(255) NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sucursales (
            id_sucursal INTEGER PRIMARY KEY,
            nombre_sucursal VARCHAR(255) NOT NULL,
            ubicacion VARCHAR(255) NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id_venta INTEGER PRIMARY KEY,
            id_producto INTEGER NOT NULL,
            id_sucursal INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            precio_total REAL NOT NULL,
            fecha DATE NOT NULL,
            FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE RESTRICT,
            FOREIGN KEY (id_sucursal) REFERENCES sucursales(id_sucursal) ON DELETE RESTRICT
        )
    ''')
def save_table_sales(cursor,data):
    cursor.execute('''
    INSERT INTO ventas (id_venta, id_producto, id_sucursal, cantidad, precio_unitario, fecha, precio_total)
    VALUES (?, ?, ?, ?, ?, ?,?)
    ''', data)
def save_table_products(cursor,data):
    cursor.execute('''
    INSERT INTO productos (id_producto, nombre_producto, categoria)
    VALUES (?, ?, ?)
    ''', data)
def save_table_branches(cursor,data):
    cursor.execute('''
    INSERT INTO sucursales (id_sucursal, nombre_sucursal, ubicacion)
    VALUES (?, ?, ?)
    ''', data)

def read_csv(name_document):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, 'Archivos', name_document)
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)     
        if name_document=='ventas.csv':
            for row in reader:  
                if validate_null_values(row) and validate_inconsistent_values(row[0], row[4]):
                    calculated_value = str(float(row[3]) * float(row[4]))
                    row.append(calculated_value)
                    database("save_"+name_document,normalize_data(row))
        else:     
            for row in reader:  
                if validate_null_values(row):
                    database("save_"+name_document,normalize_data(row))

def validate_null_values(row):
    for item in row:
        if item == '' or item is None:
            print("Hay un campo vacío o nulo "+"id = "+row[0])
            return False
    return True    
def validate_inconsistent_values(id,price):
        try:
            if float(price) < 0:
                print("Precio no validado "+"id = "+id)
                return False
            return True
        except ValueError:
            print(f"Error: El precio '{price}' no es un valor numérico. id = {id}")
            return False
        
def normalize_data(row):
    for index in range (len(row)):
        if row[index].isdigit():  
            row[index]=row[index]
        else:
            row[index]=row[index].capitalize()
    return row
        
if __name__ == "__main__":
    main()