seleccion=15
while seleccion!=0:
    print("Bienvenido a la base de datos de CAMPUSLANDS")
    print("""
        Por favor seleccione su perfil
        1-Camper
        2-Coordinador
        3-Trainer
        0-Salir
        """)
    seleccion=int(input("Ingrese el número del perfil al cual desea ingresar  "))
    if seleccion==1:
        from Camper import *
    elif seleccion==2:
        from Coordinador import *
    elif seleccion==3:
        from Trainer import *
    else:
        print("Opcaión no valida")

