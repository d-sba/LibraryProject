import sqlite3

# 1. Define las rutas
DB_FILE = 'LibraryDB.db' # Asegúrate de que este sea el nombre de tu archivo .db
OUTPUT_FILE = 'dump.sql' # Nombre del archivo SQL que se generará

# 2. Conectarse a la base de datos SQLite
try:
    conn = sqlite3.connect(DB_FILE)
    print(f"Conectado a la base de datos: {DB_FILE}")

    # 3. Abrir el archivo de salida para escribir el script SQL
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # Generar el script SQL (incluye CREATE TABLE e INSERT)
        for line in conn.iterdump():
            f.write(f'{line}\n')

    print(f"\n¡Éxito! El script SQL ha sido generado en: {OUTPUT_FILE}")

except sqlite3.Error as e:
    print(f"Error de SQLite: {e}")
finally:
    if conn:
        conn.close()