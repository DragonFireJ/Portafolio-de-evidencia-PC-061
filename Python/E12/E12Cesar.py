# Scripts brindados por la maestra Perla Marlene Viera Gonzalez
# Modificado por: Jairo Santana García
# Pablo de Jesus García Medina
import argparse
import os
import detectSpanish

def descifrado_cesar(message, clave):
    key = clave

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print(f"El mensaje desencriptado es: \n{translated}")


def crackeo_cesar(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    Llaves = {}
    
    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''
        # The rest of the program is almost the same as the original program:

        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        # Display every possible decryption:
        if detectSpanish.isEspaniol(translated):
            Llaves[key] = translated
    if Llaves:
        for i in Llaves:
            print(f"Llave #{i}:", Llaves[i])
    else:
        print("No se encontro ningun mensaje")
        

def cifrado_cesar(message, clave):
    key = clave

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print(f"El mensaje encriptado es: \n{translated}")

ayuda=r"""Modo de uso:
Modo encriptar
E12Cesar.py -mo e -me 'Mensaje a encriptar' -k 3
Modo desencriptar
E12Cesar.py -mo d -me 'Mensaje a desencriptar' -k 7
Modo crackear
E12Cesar.py -mo c -me 'Mensaje a crackear'"""
parser = argparse.ArgumentParser(description='Cripto Cesar',
                                 epilog=ayuda,
                                 formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument("-mo", "--mode", dest="mode", required=True,
                    help="Pon uno de los modos: e, d, c")
parser.add_argument("-me", "--message", dest="message", required=True,
                    help="Agrega un mensaje")
parser.add_argument("-k", "--key", dest="clave", type=int, default=1,
                    help="Agrega el numero para la clave")
params = parser.parse_args()
if params.mode == "e":
    cifrado_cesar(params.message, params.clave)
elif params.mode == "d":
    descifrado_cesar(params.message, params.clave)
elif params.mode == "c":
    crackeo_cesar(params.message)
else:
    print("""Por favor seleccione un modo valido:
-mo e (Modo encriptar)
-mo d (Modo desencriptar)
-mo c (Modo crackeo) """)
    
