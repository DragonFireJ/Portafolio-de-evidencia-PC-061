<#Script creado por: Jairo Santana García, Pablo de Jesus García Medina, Jose Pablo Perez Hernandez.
Objetivo del scritp: A traves de este script queremos que puedas gestionar tus archivos de una manera 
sencilla, con este vas a poder buscar archivos, directorios, ademas de esto vas a poder crearlos y eliminarlos#>

Import-Module -Name "C:\Program Files\WindowsPowerShell\Modules\PC061\Archivos.psm1" #Tener cuidado con el Path a la hora de instalar el modulo puede que la carpeta PC061 no este en su PC, favor de crearla o cambiarla en su defecto y poner ahi el modulo
$cont = $true

while($cont -eq $true){
$menu = Read-Host -Prompt "`n¿Qué desea realizar?
[1] Crear un nuevo directorio
[2] Crear un nuevo archivo
[3] Remover un directorio
[4] Remover un archivo
[5] Buscar archivos por extensión
[6] Salir
Opción: "

switch ($menu){
1{try{
Write-Host "`nSe le solicitaran los sig. datos: Nombre del archivo (Ej. Carpeta), Ruta donde se quiere guardar (Ej. C:\Users\Pedro)"
New-Directorio} catch{
Write-Host "Ocurrio un error lo sentimos mucho"
$_.Exception.Message #Encontramos un error a la hora de poner cadenas vacías
}
break}

2{try{
Write-Host "`nSe le solicitaran los sig. datos: Nombre del archivo (Ej. Archivo), Ruta donde se quiere guardar (Ej. C:\Users\Pedro), extensión del arcchivo (Ej. .txt)"
New-Archivo} catch{
Write-Host "Ocurrio un error lo sentimos mucho"
$_.Exception.Message #Encontramos un error a la hora de poner cadenas vacías
}
break}

3{try{
Write-Host "`nSe le solicitaran los sig. datos: Nombre del archivo (Ej. Carpeta), Ruta donde se quiere guardar (Ej. C:\Users\Pedro)"
Remove-Directorio} catch{
Write-Host "Ocurrio un error lo sentimos mucho"
$_.Exception.Message #Encontramos un error a la hora de poner cadenas vacías
}
break
}

4{try{
Write-Host "`nSe le solicitaran los sig. datos: Nombre del archivo que desea remover (Ej. Archivo), Ruta de donde sera eliminado el archivo  (Ej. C:\Users\Pedro), extensión del archivo (Ej. .txt)"
Remove-Archivo -ErrorAction Stop} catch{
Write-Host "Ocurrio un error lo sentimos mucho"
$_.Exception.Message #Encontramos un error a la hora de poner cadenas vacías
}
break}

5{try{
Write-Host "`nSe le solicitaran los sig. datos: Extencion de los archivos (Ej. txt), Ruta donde se quiere guardar (Ej. C:\Users\Pedro)"
Get-BuscaArchivos} catch{
Write-Host "Ocurrio un error lo sentimos mucho"
$_.Exception.Message #Encontramos un error a la hora de poner cadenas vacías
}
break}

6{Write-Host "`nGracias por usar el programa"
$cont = $false
break}
default{Write-Host  "`nIngrese una opción válida por favor"}
}
}