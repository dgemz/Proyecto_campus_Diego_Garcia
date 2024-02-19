import json
camper={}



def guardar_camper(camper):

    try:
        with open ("campers.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(camper)

    with open ("campers.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Camper registrado exitosamente")

def ingreso_campers(id, nombres, apellidos, direccion, acudiente, telefonoc, telefonof):
    camper[id]={
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Direccion": direccion,
        "Acudiente": acudiente,
        "Telefono celular":telefonoc,
        "Telefono fijo":telefonof,
        "Ruta": "No asignada",
        "Estado": "Inscrito",
        "Riesgo": "Nulo"
    }

    guardar_camper(camper)

def aprobar_camper(id, nota_teorica, nota_practica):
    if id in camper.keys():
        nota_prueba=(nota_practica+nota_teorica)/2
        if nota_prueba>=60:
            camper[id]['Estado'] = 'Aprobado'
        return camper
    else:
        return "No se encontró el camper con el id: " + str(id)

ruta={}
salon={}
notas={}

def guardar_rutas(ruta):

    try:
        with open ("rutas.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(ruta)

    with open ("rutas.json", "w") as file:
        json.dump(data, file, indent=4)

def guardar_salon(salon):

    try:
        with open ("salon.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(salon)

    with open ("salon.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Trainer registrado exitosamente")

def crear_ruta(nombre_ruta, fecha_inicio, fecha_fin, horario, salon_clas):
    num_modulos = int(input("Cuantos modulos desea añadir  "))
    ruta[nombre_ruta] = {
        "Fecha de inicio": fecha_inicio,
        "Fecha de finalización": fecha_fin,
        "Horario": horario,
        "Salón de clase": salon_clas
    }
    for i in range(num_modulos):
        modulo = f"Modulo {i+1}"
        contenido = input(f"Ingrese el tema del {modulo}  ")
        ruta[nombre_ruta][modulo] = contenido
    salon[nombre_ruta]= {'Trainer': 'No asignado'}
    guardar_rutas(ruta[nombre_ruta])
    guardar_salon(salon[nombre_ruta])

trainers={}

def guardar_trainers(trainers):

    try:
        with open ("trainers.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(trainers)

    with open ("trainers.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Trainer registrado exitosamente")

def ingresar_trainer(nombre_trainer, ruta_trainer):
    if not nombre_trainer in salon.keys():
        trainers[nombre_trainer] = ruta_trainer
        salon[ruta_trainer]["Trainer"] = {nombre_trainer}
        guardar_trainers(trainers)
        guardar_salon(salon)

def asignar_ruta(id_camper, ruta_asignada):
    print(ruta)
    if ruta_asignada in ruta.keys():
        if id_camper in camper.keys():
            if camper[id_camper]["Estado"]=="Aprobado":
                num_est = len(salon[ruta_asignada])
                if num_est <= 34:
                    estudiante = f"Estudiante {num_est}"
                    salon[ruta_asignada][estudiante] = camper[id_camper]
                    camper[id_camper]["Ruta"]=ruta_asignada
                    guardar_salon(salon)
                else:
                    print("La ruta está llena.")
            else:
                print("El alumno no esta aprobado. ")
        else:
            print("La identificación no está en el sistema.")
    else:
        print("La ruta no existe o aun no tiene un TRAINER designado. ")

def calc_notas(id_camper, modulo, nota_proyect, nota_quiz, nota_trainer):

    if id_camper in camper.keys():
        ruta_camper=camper[id_camper]["Ruta"]
        if modulo in ruta[ruta_camper].keys():
            nota=(nota_proyect*0.6)+(nota_quiz*0.3)+(nota_trainer*0.1)
            notas[id_camper]={modulo: nota}
            if nota<60:
                if not camper[id_camper]["Riesgo"]=="En riesgo":
                    camper[id_camper]["Riesgo"]="En riesgo"
                    print("El estudiante ahora se encuentra en riesgo por sacar menos de 60 en este modulo")
                else:
                    camper[id_camper]["Estado"]="Expulsado"
                    print("El estudiante ya se encontraba en riesgo, por tanto es expulsado por sacar dos modulos en menos de 60 :(")
        else:
            print("El modulo no existe")
    else:
        print("La identificación no está en el sistema.")

seleccion2=54
while seleccion2!=0:
      print("Bienvenido al menú de coordinadores")
      print("""Funcionalidades
      1- Para ingresar nuevo camper.
      2- Prueba de admición de un nuevo camper.
      3- Asignar una ruta a un trainer.
      4- Asignar ruta a los campers.
      5- Crear una nueva ruta.
      6- Imprimir rutas.
      7- Imprimir Trainers.
      8- Imprimir campers
      0- Salir
      
      """)
      seleccion2=int(input("Ingrese la función que desea realizar  "))
      if seleccion2==1:
            id=input("Ingrese el número de identificación del camper  ")
            nombres=input("Ingrese los nombres del camper  ")
            apellidos=input("Ingrese los apellidos del camper  ")
            direccion=input("Ingrese la direccion del camper  ")
            acudiente=input("Ingrese el nombre del acudiente  ")
            telefonoc=input("Ingrese el telefono celular del camper  ")
            telefonof=input("Ingrese el numero fijo del camper  ")
            ingreso_campers(id, nombres, apellidos, direccion, acudiente, telefonoc, telefonof)

      elif seleccion2==2:
            id=input("Ingrese la identificación del camper  ")
            nota_teorica=input("Ingrese la nota teoria del camper  ")
            nota_practica=input("Ingrese la nota practica del camper  ")
            aprobar_camper(id, nota_teorica, nota_practica)
          
      elif seleccion2==3:
          nombre_trainer=input("Ingrese el nombre completo del trainer  ")
          print(ruta)
          ruta_trainer=input("Ingrese la ruta asignada al trainer  ")
          ingresar_trainer(nombre_trainer, ruta_trainer)
      
      elif seleccion2==4:
          id=input("Ingrese el id del camper  ")
          ruta=input("Ingrese la ruta a la cual sera ingresado ese camper  ")
          asignar_ruta(id, ruta)

      elif seleccion2==5:
          nombre_ruta=input("Ingrese el nombre de la ruta  ")
          fecha_inicio=input("Ingrese la fecha de inicio  ")
          fecha_fin=input("Ingrese la fecha de finalización de la ruta  ")
          horario=input("Ingrese el horario en el cual se dictara esa ruta  ")
          salon_clas=input("Ingrese el salón en el cual se dictara la clase  ")
          crear_ruta(nombre_ruta, fecha_inicio, fecha_fin, horario, salon_clas)

      elif seleccion2==6:
        try:
            with open ("rutas.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = []
        print(data)

      elif seleccion2==7:
        try:
            with open ("trainers.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = []
        print(data)
        
      elif seleccion2==8:
        try:
            with open ("campers.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = []
        print(data)

print("Saliendo del menú de coordinadores...")
      