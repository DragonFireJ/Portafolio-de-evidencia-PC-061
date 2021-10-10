# -*- encoding: utf-8 -*-
# Fragmentos de codigo tomados de lo brindado por:
# La maestra Perla Marlene Viera Gonzalez 
# Profesor Osvaldo Habib Gonzalez Gonzalez
# Modificado por Jairo Santana García
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import argparse


def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret

    
def printMeta(ruta):
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            try:
                cont = 0
                exifData = {}
                exif = get_exif_metadata(name)
                if exif == {}:
                        print("No se hayaron metadatos de %s " % (name))
                        with open(f"{name}.txt", "w") as f:
                            f.write(f"No hay metadatos")
                            f.close()
                            print ("\n")
                else:
                    for metadata in exif:
                        x = r"Metadata: %s - Value: %s " %(metadata,
                                                           exif[metadata])
                        print(x)
                        if cont == 0:
                            f = open(f"{name}.txt", "w")
                            f.write(f"{x}\n")
                            f.close()
                        else:
                            f = open(f"{name}.txt", "a")
                            f.write(f"{x}\n")
                            f.close()
                        cont += 1
                    print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)


def scrapingImages(url):
        print("\nObteniendo imagenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src') #find_all

            print ('Imagenes %s encontradas' % len(images))
    
            #create directory for save images
            os.makedirs('Imagenes', exist_ok=True)
    
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                print(download.split('/')[-1])
                # download images in images directory
                r = requests.get(download)
                f = open('Imagenes/%s' % download.split('/')[-1], 'wb') # C
                f.write(r.content)
                print('\n')
                f.close()
                
        except Exception as e:
                print(e)
                print ("Error conexion con " + url)
                pass

ayuda=r"""Modo de uso:
python E11meta.py -link 'ruta'
python E11meta.py -path 'https://google.com/'
"""
parser = argparse.ArgumentParser(description='Bajar Imagenes y obtener Metadata',
                                 epilog=ayuda,
                                 formatter_class = argparse.RawDescriptionHelpFormatter)
parser.add_argument('-link', type=str,
                    help='Ruta de la imagen')
args = parser.parse_args()

scrapingImages(args.link)

url = f"{os.getcwd()}/Imagenes"
printMeta(url)
