import pyodbc
import sys

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql.server.com;DATABASE=ASM_MONITOR;UID=sqluser;PWD=sqlpass'
)
cursor = conn.cursor()

with open(sys.argv[1]) as f:
    for line in f:
        if not line.strip():
            continue
        parts = line.strip().split(',')
        if len(parts) < 7:
            continue
        hostname, dg, typ, size, free, pct, rec = parts
        cursor.execute(
            "INSERT INTO ASM_DISKGROUP_USAGE (hostname, diskgroup, type, total_mb, free_mb, usage_pct, recommendation) VALUES (?, ?, ?, ?, ?, ?, ?)",
            hostname, dg, typ, size, free, pct, rec
        )
conn.commit()
conn.close() 