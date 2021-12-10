import os
from Movimientos import Menu 
from Movimientos import Operaciones
from Movimientos import Validacion

Validacion.validarUsuario()
os.system("cls")
Menu.ImprimirMenu()
Operaciones.operaciones()




