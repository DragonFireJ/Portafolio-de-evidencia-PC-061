# Script elaborado por la Maestra Perla Marlene Viera Gonzalez
# Modificado por: Jairo Santana García
# Keila Sofia Caballero Ramos
# Marco Arturo Cantu Vivanco
# Ernesto Jesus Cano Arenas
# Importamos los modulos necesarios
import argparse
import socket
from cryptography.fernet import Fernet

# Asignamos una variable con una descripcion de como usar el script
epilogo="""Modo de uso:
    clienteTCP.py -msj 'Mensaje a enviar'"""
# Creamos el objeto ArgumentParser y le agregamos la variabla de apoyo anterior
parser = argparse.ArgumentParser(description='Cliente TCP',
                               epilog=epilogo,
                            formatter_class=argparse.RawDescriptionHelpFormatter)
# Añadimos argumentos al bojeto
parser.add_argument("-msj", metavar="MSJ", dest="msj",
                    help="mensaje a enviar", required=True)
# Creamos la variable params para tomar el valor de los args. de manera sencilla
params = parser.parse_args()
# Creamos una llave de encriptacion
clave = Fernet.generate_key()
# Iniciamos el objeto de encriptacion
cifrado = Fernet(clave)

# Creamos un archivo .key donde guardaremos la llave de encriptacion
# La inicializamos en escritura de bytes
file = open('clave.key', 'wb')
# Escribimos la llave de encriptacion
file.write(clave)
# Cerramos el archivo
file.close()

# Guardamos el mensaje que se nos dio como argumento en una variable
mensj = params.msj
# Convertimos el mensaje en un dato de tipo bytes
menbytes = mensj.encode()

# Encriptamos el mensaje
msjcif = cifrado.encrypt(menbytes)
print("Mensaje enviado:\n", mensj)

# Establecemos los datos de conexion para el servidor TCP
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# Creamos un objeto socket para abrir establecer conexion a traves de IPv4 y TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Realizamos la conexion hacia el IP y el puerto seleccionado
sock.connect((TCP_IP, TCP_PORT))
# Enviamos el mensaje cifrado
sock.send(msjcif)
# Almacenamos el mensaje que nos envia el servidor (Despues de conectarnos)
# Y lo decodificamos
respuesta = sock.recv(BUFFER_SIZE).decode()
# Cerramos la conexion
sock.close

print("Respuesta recibida:", respuesta)

