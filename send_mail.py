import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'sender@abc.com'
msg['To'] = 'abc@abc.com'
msg['Subject'] = '[ASM Monitor] Report'

with open('/tmp/asm_details/asm_details.html') as f:
    html = f.read()
msg.attach(MIMEText(html, 'html'))

server = smtplib.SMTP('smtp.abc.com', 25)
server.sendmail(msg['From'], [msg['To']], msg.as_string())
server.quit() 