def get_population(country_dict):
  population_dict = {  #Creo un diccionario nuevo donde capturo el valor de dichos keys
    '2022': int(country_dict['2022 Population']), #Si no le colocamos el int, lo toma como String y no grafica correctamente
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  print(labels)
  print(values)
  return labels, values

# Comparo si el parametro country ingresado por el usuario es igual al
#  nombre de un pais ubicado en cada diccionario de la lista
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  print(result)
  return result