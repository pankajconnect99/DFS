import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql.server.com;DATABASE=ASM_MONITOR;UID=sqluser;PWD=sqlpass'
)
cursor = conn.cursor()
cursor.execute("SELECT hostname, diskgroup, type, total_mb, free_mb, usage_pct, recommendation FROM ASM_DISKGROUP_USAGE")
rows = cursor.fetchall()

with open('/tmp/asm_details/asm_details.html', 'w') as f:
    f.write('<html><body><h2>ASM Diskgroup Usage Report</h2>')
    f.write('<table border="1"><tr><th>Hostname</th><th>Diskgroup</th><th>Type</th><th>Total MB</th><th>Free MB</th><th>Usage %</th><th>Recommendation</th></tr>')
    for row in rows:
        f.write('<tr>' + ''.join(f'<td>{col}</td>' for col in row) + '</tr>')
    f.write('</table></body></html>')

conn.close() 