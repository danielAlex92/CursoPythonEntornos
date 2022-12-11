#Proyecto para graficar la poblacion de un pais con base en un archivo CSV

import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  
  data = list(filter(lambda item : item['Continent'] == 'South America',data))#Filtro los paises de Suramerica
  print(data)
  countries = list(map(lambda x: x['Country'], data)) #Hago una lista con los nombres de los paises
  percentages = list(map(lambda x: x['World Population Percentage'], data)) #Hago una lista con los porcentajes de estos paises de Suramerica
  charts.generate_pie_chart(countries, percentages)
  
  #Con este segmento grafico la poblacion de un pais que digite por teclado

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'],labels, values)
  

if __name__ == '__main__':
  run()