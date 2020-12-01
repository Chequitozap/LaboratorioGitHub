
#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

data = {}
with open('data.json') as f:
        data = json.load(f)
# crea una instancia de un objeto 

msg = MIMEMultipart()

# Se le agrega los parametros del usuario

msg['From'] = data['user']
msg['To'] = str(sys.argv[1])
msg['Subject'] = str(sys.argv[2])
message= str(sys.argv[3])

#Se le agrega el cuerpo del mensaje  
msg.attach(MIMEText(message, 'plain'))

#Se define el cuerpo tambien puede ser utilizado para gmail.com
server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

# Se crean los datos a agregar por el usuario 
server.login(data['user'], data['pass'])


# Se conecta el servidor con el envio de correo 
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))

#Sale del servidor para despues imprimir el mensaje si se envio con exito 