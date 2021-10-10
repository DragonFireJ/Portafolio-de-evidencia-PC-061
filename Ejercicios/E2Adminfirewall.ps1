<#Jairo Santana García, Jose Pablo Perez Hernandez, Pablo de Jesús García Medina#>

Import-Module -Name "C:\Program Files\WindowsPowerShell\Modules\PC061\Modulo061.psm1" #Tener cuidado con el Path a la hora de instalar el modulo puede que la carpeta PC061 no este en su PC, favor de crearla o cambiarla en su defecto y poner ahi el modulo
$cont = $true

while($cont -eq $true){
$menu = Read-Host -Prompt '¿Qué desea realizar?
[1] Ver el estatus del perfil
[2] Cambiar el estatus del perfil
[3] Ver Perfil red acutal
[4] Cambiar perfil red actual
[5] Reglas de bloqueo
[6] Agregar reglas de bloqueo
[7] Eliminar reglas de bloqueo
[8] Salir
NOTA: PARA USAR LAS FUNCIONES 2, 4, 6 Y 7 DEBERAS TENER PERMISOS DE ADMINISTRADOR
Opción: '

switch ($menu){
1{try{
Write-Host "`n---Accediendo a Ver Status del perfil---`n"
Ver-StatusPerfil -ErrorAction "Stop"
Write-Host "`n---Impresion de datos realizada exitosamente---`n"} catch{
Write-Host "`n---------------------------------------------------------------------
Ocurrió un error, favor de poner un valor válido 'Public' o 'Private'
---------------------------------------------------------------------`n "}
break
}
2{try{
Write-Host "`n---Accediendo a cambiar el status del perfil---`n"
Cambiar-StatusPerfil -ErrorAction "Stop"
Write-Host "`n---Operacion finalizada gracias por confiar en nosotros---`n"} catch{
Write-Host "`n------------------------------------------------------------------------------------
Ocurrió un error, existen 2 posibles casos;
[1] Ingreso un valor inválido en el perfil, debe poner 'Public' o 'Private'
[2] O bien no se pudo hacer el cambio
------------------------------------------------------------------------------------`n "}
break
}
3{
Write-Host "`n---Accediendo a cambiar el status del perfil---`n"
Ver-PerfilRedActual -ErrorAction "Stop"
Write-Host "`n-----------------------------------------------`n"
break
}
4{try{
Write-Host "`n---Accediendo el perfil de red actual---`n"
Cambiar-PerfilRedActual -ErrorAction "Stop"
Write-Host "`n---Operacion finalizada gracias por confiar en nosotros---`n"}
catch{
Write-Host "
`n--------------------------------------------------------------------------------------
Ocurrio un error, lo sentimos, puede ser por los permisos que tiene no sean suficientes
--------------------------------------------------------------------------------------`n"}
break
}
5{try{
Write-Host "`n---Accediendo a ver las reglas de bloqueo---`n"
Ver-ReglasBloqueo -ErrorAction "Stop"
Write-Host "`n---Operacion finalizada gracias por confiar en nosotros---`n"}
catch{
Write-Host "`n-------------------------------------
Ocurrio un error, lo sentimos
-------------------------------------`n"}
break
}
6{try{
Write-Host "`n---Accediendo a agregar reglas de bloqueo---`n"
Agregar-ReglasBloqueo -ErrorAction "Stop"
Write-Host "`n---Operacion finalizada gracias por confiar en nosotros---`n"}
catch{
Write-Host "`n---------------------------------------------------------------------
Ocurrió un error:
[1] No se pudo crear la regla por los permisos
[2] El puerto es inválido
---------------------------------------------------------------------`n "}
break
}
7{try{
Write-Host "`n---Eliminando regla de bloqueo----`n"
Eliminar-ReglasBloqueo -ErrorAction "Stop"
Write-Host "`n---Operacion finalizada gracias por confiar en nosotros---`n"
}
catch{
Write-Host "`n-------------------------------------------------------
Ocurrió un error, existen 3 posibles casos;
[1] Ingreso un valor inválido en la regla, debe ser una existente
[2] Ingreso un valor inválido en el perfil, debe poner 'Public' o 'Private'
[3] Ingreso un valor inválido en el ID de la regla'N'
-------------------------------------------------`n"}
}
8{Write-Host "Gracias por usar el programa"
$cont = $false
break}
default{Write-Host  "Ingrese una opción válida por favor"}
}
}
