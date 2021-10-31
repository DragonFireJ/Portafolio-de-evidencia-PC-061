# Script elaborado por: Jairo Santana García
# Pablo de Jesus García Medina
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


def enviar_img(subject, body, sender, receiver, password, img, nombre):
    if password is None:
        password = getpass.getpass()
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = f"{nombre} <{sender}>"
    message["To"] = receiver
    message["Subject"] = subject
    message["Bcc"] = receiver

    message.attach(MIMEText(body, "plain"))
    filename = img  # In same directory as script

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)
    print("Mensaje enviado")


def enviar_correo(user, pwd, to, subject, text, nombre):
    if pwd is None:
        pwd = getpass.getpass()
    msg = MIMEText(text)
    msg['From'] = f"{nombre} <{user}>"
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")


subject = input("Ingresa el asunto del mensaje: ")
body = input("Ingresa el cuerpo del mensaje: ")
sender = input("Ingresa el correo del remitente: ")
receiver = input("Ingresa el correo del destinatario: ")
password = getpass.getpass()
nombre = input("Ingresa tu nombre completo: ")
print("¿Quiere enviar una imagen?")
x = int(input("""[1]Yes
[2]No
Opcion: """))
while x < 1 or x > 2:
    print("¿Quiere enviar una imagen?")
    x = int(input("""[1]Yes
[2]No
Opcion: """))
if x == 1:
    img = input("Ingresa el nombre o ruta de la imagen: ")
    enviar_img(subject, body, sender, receiver, password, img, nombre)
elif x == 2:
    enviar_correo(sender, password, receiver, subject, body, nombre)
