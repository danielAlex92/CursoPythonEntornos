# Forma de convertir un CSV en una lista de diccionarios para mas facil manejo
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:  #Sentencia para usar archivo y que se cierre automaticamente
    reader = csv.reader(csvfile, delimiter=',')  #Se obtiene objeto tipo reader proveniente del CSV
    print(reader)
    #header almacena la primera iteracion de reader, es decir,
    #el primer elemento que sería la primera fila
    header = next(reader)
    print(header)
    
    data = []    #Creo vector vacío para empezar a almacenar mi lista
    for row in reader:
      iterable = zip(header, row) #Guardo tuplas con la pareja header,elemento
      #uso Dict comprehension para convertirlo a diccionario
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict) #Voy anexando cada pareja key-value al dict
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0]) #Devuelve el primer diccionario el cual contiene los datos de un país