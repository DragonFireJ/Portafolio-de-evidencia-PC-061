# Script Modificado por: Jairo Santana García
# Pablo de Jesus García Medina
# Nota cambiar los puertos en caso de querer hacer una busqueda mas extensa
import argparse
import nmap
import sys

ip = []

for i in sys.stdin:
    entry = i.strip()
    if entry:
        print(entry)
        ip.append(entry)

for i in ip:
    nm = nmap.PortScanner()         
    nm.scan(i,'0-100') # Se pueden cambiar los puertos siguiendo #N-#N
    for host in nm.all_hosts():
        print('---------------------------------------------------------')
        print('Host : %s (%s)' % (host,nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('-----------------------------------------------------')
            print('protocol : %s' % proto )
            lport = nm[host][proto].keys()
            for port in lport:                 
                print('port : %s\tstate : %s' % (port,nm[host][proto][port]['state']))





