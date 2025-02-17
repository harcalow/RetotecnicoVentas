# RetotecnicoVentas
Imagina que trabajas como ingeniero de datos para una empresa que quiere analizar las ventas de sus productos en diferentes sucursales. Los datos están almacenados en varios archivos CSV que debes procesar, limpiar, y luego cargar en una base de datos relacional para hacer consultas y generar un informe final.

Reto:
Obtención de datos:

Descarga tres archivos CSV que representan ventas, productos y sucursales.
ventas.csv: Contiene las columnas id_venta, id_producto, id_sucursal, cantidad, precio_unitario, fecha.
productos.csv: Contiene las columnas id_producto, nombre_producto, categoria.
sucursales.csv: Contiene las columnas id_sucursal, nombre_sucursal, ubicacion.
Limpieza de datos:

Usa Python para cargar los archivos CSV, verifica si hay valores nulos o inconsistentes (como precios negativos o ventas sin fecha).
Normaliza los nombres de productos y sucursales para que no haya diferencias de mayúsculas/minúsculas o espacios adicionales.
Agrega una nueva columna en el archivo de ventas que calcule el precio total de la venta (cantidad * precio_unitario).
Carga a base de datos:

Crea una base de datos en SQLite.
Carga los datos de los CSV en tablas de SQLite llamadas ventas, productos, y sucursales.
Consultas SQL:

Genera las siguientes consultas en SQL:
¿Cuál fue la sucursal con más ventas totales (suma del precio total) durante el último mes?
¿Cuáles fueron los 5 productos más vendidos por categoría?
Calcula las ventas totales por día, agrupadas por sucursal.
Automatización en Shell:

Escribe un script en Shell que automatice la ejecución del flujo completo:

Ejecutar Shell.sh

Para linux dar permisos chmod +x Shell.sh
Ejecutar el script ./Shell.sh

Para windows 
Ejecutar el script ./Shell.sh