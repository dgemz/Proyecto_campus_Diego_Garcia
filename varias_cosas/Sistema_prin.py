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
        'Nombres': nombres,
        'Apellidos': apellidos,
        'Direccion': direccion,
        'Acudiente': acudiente,
        'Telefono celular':telefonoc,
        'Telefono fijo':telefonof,
        'Ruta': 'No asignada',
        'Estado': 'Inscrito',
        'Riesgo': 'Nulo'
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

ruta['Java']={
    'Fecha de inicio': '9 de enero',
    'Fecha de finalización':'9 de agosto',
    'Horario': '6AM a 10AM',
    'Modulo 1': 'Introduccón a Java',
    'Modulo 2': 'Practica en Java',
    'Modulo 3': 'Especialización y uso real de Java'
}
salon['Java']= {'Trainer': {'No asignado'}}

ruta['NetCore']={
    'Fecha de inicio': '9 de febrero',
    'Fecha de finalización':'9 de septiembre',
    'Horario': '10AM a 2PM',
    'Modulo 1': 'Introduccón a NetCore',
    'Modulo 2': 'Practica en NetCore',
    'Modulo 3': 'Especialización y uso real de NetCore'
}
salon['NetCore']= {'Trainer': {'No asignado'}}

ruta['NodeJS']={
    'Fecha de inicio': '9 de enero',
    'Fecha de finalización':'9 de agosto',
    'Horario': '2AM a 6AM',
    'Modulo 1': 'Introduccón a NodeJS',
    'Modulo 2': 'Practica en NodeJS',
    'Modulo 3': 'Especialización y uso real de NodeJS'
    
}
salon['NodeJS']= {'Trainer': {'No asignado'}}

def crear_ruta(nombre_ruta, fecha_inicio, fecha_fin, horario):
    num_modulos = int(input("Cuantos modulos desea añadir  "))
    ruta[nombre_ruta] = {
        'Fecha de inicio': fecha_inicio,
        'Fecha de finalización': fecha_fin,
        'Horario': horario,
    }
    salon[nombre_ruta]= {'Trainer': 'No asignado'}
    for i in range(num_modulos):
        modulo = f"Modulo {i+1}"
        contenido = input(f"Ingrese el tema del {modulo}  ")
        ruta[nombre_ruta][modulo] = contenido

trainers={}

def ingresar_trainer(nombre_trainer, ruta_trainer):
    if not nombre_trainer in salon.keys():
        trainers[nombre_trainer] = ruta_trainer
        salon[ruta_trainer]['Trainer'] = {nombre_trainer}

def asignar_ruta(id_camper, ruta_asignada):
    print(ruta)
    if ruta_asignada in ruta.keys():
        if id_camper in camper.keys():
            if camper[id_camper]['Estado']=='Aprobado':
                num_est = len(salon[ruta_asignada])
                if num_est <= 34:
                    estudiante = f"Estudiante {num_est}"
                    salon[ruta_asignada][estudiante] = camper[id_camper]
                    camper[id_camper]['Ruta']=ruta_asignada
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
        ruta_camper=camper[id_camper]['Ruta']
        if modulo in ruta[ruta_camper].keys():
            nota=(nota_proyect*0.6)+(nota_quiz*0.3)+(nota_trainer*0.1)
            notas[id_camper]={modulo: nota}
            if nota<60:
                if not camper[id_camper]["Riesgo"]=="En riesgo":
                    camper[id_camper]["Riesgo"]="En riesgo"
                    print("El estudiante ahora se encuentra en riesgo por sacar menos de 60 en este modulo")
                else:
                    print("El estudiante ya se encontraba en riesgo, por tanto es expulsado por sacar dos modulos en menos de 60 :(")
        else:
            print("El modulo no existe")
    else:
        print("La identificación no está en el sistema.")

def mostrar_trainer():
    print("")








    



