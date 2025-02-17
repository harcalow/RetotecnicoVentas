#!/bin/bash
file_path="BasesDeDatos/sales"
if [ -f "$file_path" ]; then
    echo "El archivo $file_path existe."
 else
    python main.py
fi


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    python3 queriesSql.py
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    python queriesSql.py
else
    echo "Sistema operativo no soportado"
    exit 1
fi



