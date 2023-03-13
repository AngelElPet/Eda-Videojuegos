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
elif menu == 'Regiones por Meses':
    img1 = Image.open('src\data\mes_Eu.jpg')
    st.image(img1,use_column_width='auto') 
    img2 = Image.open('src\data\mes_Au.jpg')
    st.image(img2,use_column_width='auto') 
    img3 = Image.open('src\data\mes_Jp.jpg')
    st.image(img3,use_column_width='auto')
    img4 = Image.open('src\data\mes_Na.jpg')
    st.image(img4,use_column_width='auto')
elif menu == 'Generos principales':
    
    generos()

elif menu== 'Regiones por Dias':
    st.subheader('Clasificación por días de estreno')
    st.markdown('''
    En esta pestaña podremos comprobar cuales son los días en los que se han salido a mercado más videojuegos en cada región
    ''')  
    if st.checkbox("Europa",value=True):
        st.markdown('El día más popular en Europa para que salga un juego es el 29s')
        fig1 = dias_Eu()
        st.plotly_chart(fig1, use_container_width=True)

    if st.checkbox("Norte América",value=True):
        st.markdown('El día más popular en Europa para que salga un juego es el 29s')    
        fig2 = dias_Na()
        st.plotly_chart(fig2, use_container_width=True)

    if st.checkbox("Japón",value=True):
        st.markdown('El día más popular en Europa para que salga un juego es el 29s')    
        fig3 = dias_Jp()
        st.plotly_chart(fig3, use_container_width=True)

    if st.checkbox("Australia",value=True):
        st.markdown('El día más popular en Europa para que salga un juego es el 29s')
        fig4 = dias_Au()
        st.plotly_chart(fig4, use_container_width=True)

    

