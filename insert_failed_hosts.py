import pyodbc
import sys

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql.server.com;DATABASE=ASM_MONITOR;UID=sqluser;PWD=sqlpass'
)
cursor = conn.cursor()

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print("No data found in log.")
        sys.exit(1)
    columns = [col for col in lines[0].split('|') if col]
    for line in lines[1:]:
        values = [val for val in line.split('|') if val]
        if len(values) != len(columns):
            print(f"Skipping line due to column mismatch: {line}")
            continue
        placeholders = ','.join(['?'] * len(columns))
        sql = f"INSERT INTO YOUR_TABLE ({','.join(columns)}) VALUES ({placeholders})"
        cursor.execute(sql, *values)
conn.commit()
conn.close() 