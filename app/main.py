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
  choice = input('Type option: \n\t1 - Continent population \n\t2 - Country population\n==> ')
  if choice == '1':
    continent = input('Type continent (Asia,Africa,Europe,North America,South America,Oceania): ')
    df = df[df['Continent'] == continent.title()]
    paises = df['Country/Territory'].values
    porcentaje = df['World Population Percentage'].values
    charts.generate_pie_chart(paises,porcentaje)
    charts.generate_bubble(continent,paises,porcentaje)
    print('Archivos generados en bubble.png y pie.png con exito')
  else:
    data = read_csv.read_csv('data.csv')
    country = input ('Type Country : ')
    resultado = utilidades.population_by_country(data,country)

    if len(resultado) > 0:
      country_bar = resultado[0]
      labels, values = utilidades.get_population(country_bar)
      charts.generate_bar_chart(labels,values,country)

if __name__ == '__main__':
  run()