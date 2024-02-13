
import sqlite3

# Conectar a la base de datos SQLite (esto la creará si no existe)
conn = sqlite3.connect('main.db')
c = conn.cursor()

# Crear una tabla
c.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_disc TEXT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    puntos INTEGER DEFAULT 0,
    saldo REAL DEFAULT 0.0
);
''')

# Guardar (confirmar) los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()