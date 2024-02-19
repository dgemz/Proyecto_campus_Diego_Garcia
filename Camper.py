import json
try:
      with open ("campers.json", "r") as file:
            data = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
      data = []

def buscar_info(num_unico):
      print(data[num_unico])

seleccion=15
while seleccion!=0:
      print("Bienvenido a la base de datos de los campers")
      print("""Seleccione una de las opciones
            1- Para ver sus datos y estado
            2- Para ver su estado
            0- Salir
            
            """)
      seleccion=int(input("Ingrese el número de la opción deseada  "))
      if seleccion==1:
            ide_unico=int(input("Ingrese el número dado por campus para ver su información  "))
            buscar_info(ide_unico)

      else:
            print("Opcaión no valida")
print("Saliendo del menú de campers...")