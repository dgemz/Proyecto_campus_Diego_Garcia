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

def modificar_camper(id, nota_teorica, nota_practica):

    if id in camper:
        nota_prueba=(nota_practica+nota_teorica)/2
        if nota_prueba>=60:
            camper[id]['Estado'] = 'Aprobado'
        return camper
    else:
        return "No se encontró el camper con el id: " + str(id)
    
id=123456789
nombres= 'Diego'
apellidos= 'Garcia'
direccion= '123nort'
acudiente= 'Petronila Sinforosa'
telefonoc= '123456'
telefonof= '654321'

ingreso_campers(id, nombres, apellidos, direccion, acudiente, telefonoc, telefonof)

nota_teorica= 60
nota_practica= 70

modificar_camper(id, nota_teorica, nota_practica)
print(camper)

