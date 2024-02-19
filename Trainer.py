import json
def buscar_info(num_unico):
      try:
            with open ("rutas.json", "r") as file:
                  data = json.load(file)
      except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
            print(data)

seleccion=15
while seleccion!=0:
      print("Bienvenido a la base de datos de los campers")
      print("""Seleccione una de las opciones.
            1- Para ver sus estudiantes.
            2- Para ver sus clases y horarios.
            0- Salir
            
            """)
      seleccion=int(input("Ingrese el número de la opción  "))
      if seleccion==1:
            try:
                  with open ("rutas.json", "r") as file:
                        data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                  data = []
                  print(data)
      elif seleccion==2:
            try:
                  with open ("salon.json", "r") as file:
                        data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                  data = []
                  print(data)

      else:
            print("Opcaión no valida")
print("Saliendo del menú de campers")