"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra.


  """
  # Abrimos el archivo y leemos todas las lineas
  with open('files/input/clusters_report.txt', "r", encoding="utf-8") as f:
      lines = f.readlines()
  
  # Datos del dataframe
  data = []
  # Cluster
  cluster = 0
  # Cantidad palabras clave
  cantPalabras = 0
  # Porcentaje palabras clave
  porcenPalabras = 0
  # Palabras clave
  palabrasClave = ' '
  # Procesamos desde la linea 5
  for line in lines[4:]:
      # Quitamos los espacios en blanco del inicio y final de la linea
      cleanLine = line.strip().split()

      if len(cleanLine) > 0:
        # Si el primer elemento de la linea es un numero, quiere decir que estamos en la primera linea de una fila
        if cleanLine[0].isdigit():
          # Asignamos el cluster
          cluster = int(cleanLine[0])
          # Asignamos la cantidad de palabras claves
          cantPalabras = int(cleanLine[1])
          # Asignamos el porcentaje
          porcenPalabras = float(cleanLine[2].replace(',', '.'))
          # Creamos la cadena de palabras clave
          palabrasClave = palabrasClave.join(cleanLine[4:])
        else:
          # Debemos concatenar el siguiente renglon de palabras clave
          palabrasClave += ' ' + ' '.join(cleanLine).strip('.')
      else:
        # Es un renglon vacio, es decir, continua la siguiente fila
        data.append({'cluster': cluster, 'cantidad_de_palabras_clave': cantPalabras, 
                     'porcentaje_de_palabras_clave': porcenPalabras, 'principales_palabras_clave': palabrasClave})
        # Reiniciamos la variable de las palabras clave
        palabrasClave = ' '

  # Dataframe resultante
  df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
         
  return df