import streamlit as st
from functionst import*
import sqlite3
import warnings
warnings.filterwarnings("ignore")
def sql_query(query):
    
    return pd.read_sql(query,cnx)

config_pagina()

menu = st.sidebar.selectbox('Menu',('Página principal','Cargar_datos','Regiones por Meses','Regiones por Dias','Generos principales','Conclusión'))

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
    st.markdown(''' 
    Mostramos aquí una tabla donde aparecen todos los datos de la gráfica anterior. Vamos a filtrarlos para poder responder a la pregunta inicial
    de si se estrenan antes más videojuegos en Norte América que en Europa.
    ''')
    query='''
    SELECT*
    FROM x
    '''
    st.dataframe(sql_query(query))
    st.markdown(''' 
    Veamos cuantos han salido antes en Norte América en la siguiente tabla. Si os dais cuenta, son las mismas observaciones que en la tabla
    anterior, solo que filtrado para que escoger aquellas observaciones en las que no salga Eu en la columna Regiones, pero si aparezca NA.
    ''')
    query='''
    SELECT*
    FROM x
    WHERE NOT (Regiones LIKE '%EU%') AND Regiones LIKE '%NA%'
     '''
    st.dataframe(sql_query(query))
    st.markdown('''
    Aquí podremos apreciar los que se pudieron jugar antes en Europa que en Norte América.
    ''')
    query='''
    SELECT*
    FROM x
    WHERE NOT (Regiones LIKE '%NA%')  AND Regiones LIKE '%EU%' '''
    st.dataframe(sql_query(query))
    st.markdown('''Y en esta tabla, podemos apreciar como realmente hay una aplia mayoria de juegos que han salido a la vez en ambas regiones.''')
    query='''
    SELECT*
    FROM x
    WHERE Regiones LIKE '%NA%' AND Regiones LIKE '%EU%' '''
    st.dataframe(sql_query(query))
    st.markdown('''CONCLUSIÓN: \n
                Finalmente podemos apreciar que se han estrenado antes más juegos en Euro que en Norte América. Sin embargo, cabe destacar
                que la gran mayoría de los juegos se han estrenado a la vez en ambas regiones.''')
elif menu == 'Regiones por Meses':
    st.subheader('Clasificación de estreno por meses')

    st.markdown('''En este apartado podremos apreciar cuantos juegos han salido en cada mes y en cada región, pudiendo sacar
    conclusiones como cuál es el mes más popular para estrenar un viedojuego y cual es el menos popular.''')

    if st.checkbox("Europa",value=False):
        img1 = Image.open('src/data/Mes Eu.jpg')
        st.image(img1,use_column_width='auto') 
    
    if st.checkbox("Australia",value=False):
        img2 = Image.open('src/data/Mes Au.jpg')
        st.image(img2,use_column_width='auto') 

    if st.checkbox("Japón",value=False):
        img3 = Image.open('src/data/Mes Jp.jpg')
        st.image(img3,use_column_width='auto')

    if st.checkbox("Norte América",value=False):
        img4 = Image.open('src/data/Mes Na.jpg')
        st.image(img4,use_column_width='auto')

elif menu == 'Generos principales':
    st.subheader('Clasificación de videojuegos por los géneros principales')
    st.markdown('''En este apartado podemos ver cuales han sido los generos más populares durante los últimos años. Esta información
    puede inspirar a un empresa a tomar una decisión sobre que tipo de juegos desarrollar en un futuro.''')
    generos()

elif menu== 'Regiones por Dias':
    st.subheader('Clasificación de estreno por días')
    st.markdown('''
    En esta pestaña podremos comprobar cuales son los días en los que se han salido a mercado más videojuegos en cada región.
    ''')  
    if st.checkbox("Europa",value=False):
        st.markdown('El día más popular en Europa para que salga un juego es el 29.')
        fig1 = dias_Eu()
        st.plotly_chart(fig1, use_container_width=True)

    if st.checkbox("Norte América",value=False):
        st.markdown('El día más popular en Norte America para que salga un juego es el 29.')    
        fig2 = dias_Na()
        st.plotly_chart(fig2, use_container_width=True)

    if st.checkbox("Japón",value=False):
        st.markdown('El día más popular en Japon para que salga un juego es el 20.')    
        fig3 = dias_Jp()
        st.plotly_chart(fig3, use_container_width=True)

    if st.checkbox("Australia",value=False):
        st.markdown('El día más popular en Australia para que salga un juego es el 29.')
        fig4 = dias_Au()
        st.plotly_chart(fig4, use_container_width=True)

    

