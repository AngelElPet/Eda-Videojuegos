import streamlit as st
from functionst import*
import sqlite3
import warnings
warnings.filterwarnings("ignore")
def sql_query(query):
    
    return pd.read_sql(query,cnx)

config_pagina()

menu = st.sidebar.selectbox('Menu',('Página principal','Cargar_datos','Meses','Generos principales','Conclusión'))

if menu=='Página principal':
    pagina_principal()
elif menu =='Cargar_datos':
    cargar_datos()
elif menu =='Conclusión':
    st.header('Videojuegos')
    plataforma_year()
    tarta()
    
    cnx = sqlite3.connect(':memory:')
    x=pd.DataFrame(df.Comp.value_counts())
    x['Regiones']=x.index
    x.to_sql(name='x',con=cnx,if_exists='append', index=False)

    query='''
    SELECT*
    FROM x
    '''
    st.dataframe(sql_query(query))

    query='''
    SELECT*
    FROM x
    WHERE NOT (Regiones LIKE '%EU%') AND Regiones LIKE '%NA%'
     '''
    st.dataframe(sql_query(query))
    query='''
    SELECT*
    FROM x
    WHERE NOT (Regiones LIKE '%NA%')  AND Regiones LIKE '%EU%' '''
    st.dataframe(sql_query(query))
    query='''
    SELECT*
    FROM x
    WHERE Regiones LIKE '%NA%' OR Regiones LIKE '%EU%' '''
    st.dataframe(sql_query(query))
elif menu == 'Meses':
    img1 = Image.open('.\src\data\mes_Eu.jpg')
    st.image(img1,use_column_width='auto') 
    img2 = Image.open('.\src\data\mes_Au.jpg')
    st.image(img2,use_column_width='auto') 
    img3 = Image.open('.\src\data\mes_Jp.jpg')
    st.image(img3,use_column_width='auto')
    img4 = Image.open('.\src\data\mes_Na.jpg')
    st.image(img4,use_column_width='auto')
elif menu == 'Generos principales':
    
    generos()
    

