camper={}
def ingreso_campers(id, nombres, apellidos, direccion, acudiente, telefonoc, telefonof):
    camper[id]={
        'Nombres': nombres,
        'Apellidos': apellidos,
        'Dirección': direccion,
        'Acudiente': acudiente,
        'Telefono celular':telefonoc,
        'Telefono fijo':telefonof,
        'Estado': 'Inscrito',
        'Riesgo': 'Nulo'
    }

def aprobar_camper(id, nota_teorica, nota_practica):

    if id in camper:
        nota_prueba=(nota_practica+nota_teorica)/2
        if nota_prueba>=60:
            camper[id]['Estado'] = 'Aprobado'
        return camper
    else:
        return "No se encontró el camper con el id: " + str(id)
    
ruta={}
salon={}

ruta['Java']={
    'Modulo 1': 'Introduccón a Java',
    'Modulo 2': 'Practica en Java',
    'Modulo 3': 'Especialización y uso real de Java'
}
salon['Java']= {'Trainer': {'No asignado'}}


ruta['NetCore']={
    'Modulo 1': 'Introduccón a NetCore',
    'Modulo 2': 'Practica en NetCore',
    'Modulo 3': 'Especialización y uso real de NetCore'
}
salon['NetCore']= {'Trainer': {'No asignado'}}

ruta['NodeJS']={
    'Modulo 1': 'Introduccón a NodeJS',
    'Modulo 2': 'Practica en NodeJS',
    'Modulo 3': 'Especialización y uso real de NodeJS'
    
}
salon['NodeJS']= {'Trainer': {'No asignado'}}

def crear_ruta(nombre_ruta):
    num_modulos = int(input("Cuantos modulos desea añadir  "))
    ruta[nombre_ruta] = {}
    salon[nombre_ruta]= {'Trainer': {}}
    for i in range(num_modulos):
        modulo = f"Modulo {i+1}"
        contenido = input(f"Ingrese el tema del {modulo}  ")
        ruta[nombre_ruta][modulo] = contenido

trainers={}

def ingresar_trainer(nombre_trainer, ruta_trainer):
    if not nombre_trainer in salon:
        trainers[nombre_trainer] = ruta_trainer
        salon[ruta_trainer]['Trainer'] = {nombre_trainer}

def asignar_ruta(id_camper, ruta_asignada):
    if ruta_asignada in ruta:
        if id_camper in camper:
            if camper[id_camper]['Estado']=='Aprobado':
                num_est = len(salon[ruta_asignada])
                if num_est < 33:
                    estudiante = f"Estudiante {num_est}"
                    salon[ruta_asignada][estudiante] = camper[id_camper]
                else:
                    print("La ruta está llena.")
            else:
                print("El alumno no esta aprobado. ")
        else:
            print("La identificación no está en el sistema.")
    else:
        print("La ruta no existe. ")

