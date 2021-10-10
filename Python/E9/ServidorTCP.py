# Script elaborado por la Maestra Perla Marlene Viera Gonzalez
# Modificado por: Jairo Santana García
# Keila Sofia Caballero Ramos
# Marco Arturo Cantu Vivanco
# Ernesto Jesus Cano Arenas
# Primero importamos los modulos necesarios
import socket
from cryptography.fernet import Fernet

# Establecemos los datods de conexion
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# Creamos un objeto socket para abrir una conexion a traves de IPv4 y TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Usamos bind para enviar la IP y el puerto como argumentos
sock.bind((TCP_IP, TCP_PORT))
# Escuchamos conexiones entrantes
sock.listen(1)
# Creamos una tupla para guardar la respuesta del intento de conexion
(conection, addres) = sock.accept()
print('Direccion de conexion:', addres)
while True:
   # Recibimos el mesnsaje que envio el cliente
   mensajecif = conection.recv(BUFFER_SIZE)
   # Le respondemos al cliente que se resivio el mensaje
   conection.send(b"Enterado. Bye!")
   break
# Cerramos la conexion
conection.close()

# Aquí se crea el objeto con cifrado Fernet
# Abrimos el archivo clave.key (Que se creo en el script clienteTCP.py)
file = open('clave.key', 'rb')
# Asignamos el contendio del archivo a la variable clave
clave = file.read()
# Cerramos el objeto
file.close()
# Creamos la clave de cifrado
cifrado = Fernet(clave)

# Desencriptamos el mensaje en bytes
mensajeBytes = cifrado.decrypt(mensajecif,None)
# Decodificamos el mensaje en bytes a un lenguaje sin caracteres extraños
mensaje = mensajeBytes.decode()
print("Mensaje recibido:\n",mensaje)
