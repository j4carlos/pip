import utilidades 
import read_csv
import charts
import pandas as pd

def run():
  '''
  #Para ver la poblacion mundial porcentual por pais, por continente
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  paises = list(map(lambda x: x['Country/Territory'],data))
  porcentaje = list(map(lambda x: x['World Population Percentage'],data))
  '''
  df = pd.read_csv('data.csv')
  
  df = df[df['Continent'] == 'Europe']
  paises = df['Country/Territory'].values
  porcentaje = df['World Population Percentage'].values
  charts.generate_pie_chart(paises,porcentaje)
  
  data = read_csv.read_csv('data.csv')
  country = input ('Type Country : ')
  resultado = utilidades.population_by_country(data,country)

  if len(resultado) > 0:
    country_bar = resultado[0]
    labels, values = utilidades.get_population(country_bar)
    charts.generate_bar_chart(labels,values,country)

if __name__ == '__main__':
  run()