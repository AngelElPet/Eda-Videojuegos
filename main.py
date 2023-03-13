import sqlite3


from function import*
from function2 import *
from function3 import *

import warnings
warnings.filterwarnings("ignore")

cnx = sqlite3.connect(':memory:')

def sql_query(query):
    
    return pd.read_sql(query,cnx)


# Creamos los tres DataFrames sacados de 3 json de internet

pd_xbox = crear_pd_xb()
pd_switch = crear_pd_sw()
pd_playstation = crear_pd_ps()



#hay videojuegos que no están catalogados en la categoría genero
#En el pd_xbox y pd_playstation vamos a cambiar aquellos que tengan una observacion de tipo lista '[]' por '['Sin genero']' 
#para después poder utilizarlas en las comparaciones

pd_xbox=arreglar_genre_xb(pd_xbox)
pd_playstation=arreglar_genre_ps(pd_playstation)
pd_switch = arreglar_genre_sw(pd_switch)



#Corregido ya el genero para que sea de tipo string vamos a solucionar el tema de las fechas
# Para ello vamos a generar una nueva columna que tendrá como valores 'NA' (Norte America), 'EU' (Europa), 'JP'(Japan)
# 'AU' (Australia) o una combinación según donde haya salido primero
# Con este fin, aprovecharemos las columnas rd para extraer información de las fechas para poder compararlas

#Hay datos en las columnas rd que tienen 'TBA' entre otras como dato o 'Unreleased', por lo que vamos a modificar dichos datos
#haciendo que donde ponga 'Unreleased' aparezca un '0' (puesto que unreleased= no ha salido en ingles)
# y sustituyendo el resto de los datos por np.NaN
#para despues hacer un dropna(inplace=True)

#Crearemos una lista nueva por cada columna donde almacenar los datos de la siguiente forma[año,mes,dia]
#Aquellos datos que vengan dados por un '0' lo introduciremos en la lista como [año=3000,mes = 0 , dia=0]
#Para poder compararlos con mayor facilidad

pd_playstation=arreglar_ps(pd_playstation)
lista_ps =lista_Comp_ps(pd_playstation)
pd_playstation['Comp']= lista_ps[0]

pd_xbox=arreglar_xbox(pd_xbox)
lista_xb = lista_Comp_xb(pd_xbox)
pd_xbox['Comp']= lista_xb[0]

pd_switch=arreglar_sw(pd_switch)
lista_sw=lista_Comp_sw(pd_switch)
pd_switch['Comp']= lista_sw[0]



#Borramos aquellas columnas que no nos sirven

pd_playstation =delete(pd_playstation)
pd_switch=delete(pd_switch)
pd_xbox=delete(pd_xbox)

#Terminamos de añadir datos sobre las fechas de lanzamiento de cada región a cada DataFrame

pd_playstation = pd_ps_final(pd_playstation,lista_ps)
pd_xbox= pd_xb_final(pd_xbox,lista_xb)
pd_switch =pd_sw_final (pd_switch,lista_sw)
pd_xbox['plataforma']='xbox'
pd_playstation['plataforma']='playstation'
pd_switch['plataforma']='switch'

# Juntamos todos los datos en un solo DATAFRAME final

df = pd.concat([pd_playstation,pd_switch,pd_xbox],ignore_index=True)
df['id']=1
df.info()
df.to_csv('src\data\Videojuegos.csv',sep = ';')

plataforma_year(df)

juegos_genero(df)

juegos_mes(df)

tarta_Comp(df)

x=pd.DataFrame(df.Comp.value_counts())
x['Regiones']=x.index
x.to_sql(name='x',con=cnx,if_exists='append', index=False)


query='''
SELECT*
FROM x
 '''
print(sql_query(query))

query='''
SELECT*
FROM x
WHERE NOT (Regiones LIKE '%EU%') AND Regiones LIKE '%NA%'
 '''
print(sql_query(query))
query='''
SELECT*
FROM x
WHERE NOT (Regiones LIKE '%NA%')  AND Regiones LIKE '%EU%' '''
print(sql_query(query))
query='''
SELECT*
FROM x
WHERE Regiones LIKE '%NA%' OR Regiones LIKE '%EU%' '''
print(sql_query(query))

plt.show()

