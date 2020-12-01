
#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import smtplib

import json

import sys

#Envimax es un documento para el envio de correos multiples 

m=[]
data = {}
with open('data.json') as f:
        data = json.load(f)
# Se crea una instancia del objeto mensaje 
# Se le agregan argumentos al msg
msg = MIMEMultipart()

msg['From']= data['user']
msg['Subject']= str(sys.argv[1])
message= str(sys.argv[2])

# Se le agrega el cuerpo del mensaje 
msg.attach(MIMEText(message, 'plain'))

#Creacion del servidor  no modificar puedes dejarlo asi 
server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

# Se crean las credenciales del inicio de sesion aqui se crean los datos para que inicies sesion de manera manual 

server.login(data['user'], data['pass'])

g= open('Mails.txt','r')
for line in g:
    to=line
    m.append(to)
g.close

for element in m:
    print(element)
    msg['To']= element
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("successfully sent email to %s:" % (msg['To']))
server.quit()
#Se imprimen  todos los elementos y se envian imprimiendo si el mensaje fue enviado 