# Script elaborado por Jairo Santana García
# Pablo de Jesus Garcia Medina
# Nota, el script revisara del puerto 0 al 100, en caso de querer otros cambiar en el script Nmap.py
$Python = "python.exe"
$Script = "C:\Users\jairo\Documents\JAIRO\UANL\3er semestre\PC\Powershell\Nmap.py" #Cambiar ruta
$cont = $true

while($cont -eq $true){
$menu = Read-Host -Prompt "`n¿Qué desea realizar?
[1] Agregar una dirección IP
[2] Agregar un archivo txt con links
[3] Salir
Opción: "

switch($menu){
1{$ip = Read-Host "¿Que direccion IP se va a analizar?"
$ip | & $Python $Script
break}
2{$filePath = Read-Host "Ingrese la ruta con el nombre del txt"
$text = Get-Content $filePath
$text | & $Python $Script
break}
3{Write-Host "`nGracias por usar el programa"
$cont = $false
break}
default{Write-Host  "`nIngrese una opción válida por favor"}}}
