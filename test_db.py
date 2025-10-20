import pyodbc

server = 'localhost'
database = 'Proyecto_web'
driver = 'ODBC Driver 17 for SQL Server'

try:
    conn = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
    print("✅ Conexión exitosa a SQL Server.")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.databases;")
    for row in cursor.fetchall():
        print("-", row.name)
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
