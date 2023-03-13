import streamlit as st
import json
import pandas as pd
#from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import plotly.express as px
import pydeck as pdk
import seaborn as sb

from function3 import*

def config_pagina():
    st.set_page_config(page_title='VIDEOJUEGOS',page_icon=':chart:',layout='centered')


def pagina_principal ():
    st.title('Bienvenido')

    st.subheader('Introducción')

    img = Image.open('.\src\data\plataforma1.jpg')
    st.image(img,use_column_width='auto')
    st.markdown('''Aquí irá una pequeña introducción de lo que se verá en la página ''')

    with st.expander('Dirección de los datos'):
        st.markdown('En los siguientes enlaces están los datos originales de donde se ha extraido el trabajo')
        if st.checkbox("Playstation",value=True):
            i1= Image.open('.\src\data\playstation.jpg')
            st.image(i1,use_column_width='Auto')
            st.markdown('''

                \t*Esta es la url de PlayStation 'https://api.sampleapis.com/playstation/games'\n

        ''')
        if st.checkbox("Xbox",value=True):
            i2 = Image.open(".\src\data\\xbox.jpg")
            st.image(i2,use_column_width='Auto')
            st.markdown('''
                \t*Esta es la url de Xbox'https://api.sampleapis.com/xbox/games'\n

        ''')
        if st.checkbox("Switch",value=True):
            i3= Image.open('.\src\data\switch.jpg')
            st.image(i3,use_column_width='Auto')
            st.markdown('''
                \t*Esta es la url de Swithc 'https://api.sampleapis.com/switch/games'\n
        ''')




def cargar_datos():
    st.markdown('hola1')
    archivo=st.file_uploader('Arrastra aquí el archivo CSV Videojuegos de la carpeta data',type = ['csv'])

    if archivo is not None:

        global df
        df=pd.read_csv(archivo,sep=';')
        st.markdown('holdsga')
        if st.button('Ver tabla de Videojuegos'):
            st.markdown("<h3 style='text-align: center; color: skyblue;'> DataFrame Videojuegos </h3>", unsafe_allow_html=True)
            st.dataframe(df)
            df_pibote=pd.DataFrame(df.plataforma.value_counts())
            df_pibote['plat']=df_pibote.index
            f = sb.countplot(x=df.plataforma)
            fig = f.figure
            st.markdown("<h3 style='text-align: center; color: skyblue;'> Gráfica de Barras de Videojuegos </h3>", unsafe_allow_html=True)
            st.pyplot(fig)

def tarta():
    x=pd.DataFrame(df.Comp.value_counts())

    fig={'data':[{'values':x.Comp,'labels':x.index,'domain':{'x':[0,0.7]},'name':'','hoverinfo':'label+value','hole':0.5,'type':'pie'},],
         'layout':{'title':'Región de Lanzamiento de juegos'}}
    
    st.plotly_chart(fig,use_container_width=True)

    
def generos(): 
    df1 = df.copy()
    df1[df1.genre=='Sin genero']=np.NaN
    df1.dropna(inplace=True)
    u=pd.DataFrame(df1.genre.value_counts())
    u[u.genre<30]=np.NaN
    u.dropna(inplace=True)
    lista=[]
    for x in df1.genre.unique():
        if not (x in u.index):
            lista.append(x)
    df1[df1.genre.isin(lista)]=np.NaN
    df1.dropna(inplace=True)
    plt.figure(figsize=(15,10))
    fig2 = sb.countplot(x=df1.genre)
    plt.xticks(rotation=-45);
    plt.title('Cantidad de juegos de los principales generos')
    f2= fig2.figure
    st.pyplot(f2)

def plataforma_year():
    
    df_pd = df[df['plataforma']=='playstation']
    df_xb = df[df['plataforma']=='xbox']
    df_sw = df[df['plataforma']=='switch']
    s2 = pd.DataFrame(df_xb.groupby('Year Eu').sum('id'))
    s3 = pd.DataFrame(df_sw.groupby('Year Eu').sum('id'))
    s1 = pd.DataFrame(df_pd.groupby('Year Eu').sum('id'))
    
    s1 ['Year'] = s1.index
    s2 ['Year'] = s2.index
    s3 ['Year']= s3.index
    s1[s1.Year==3000] = np.NaN
    s2[s2.Year==3000] = np.NaN
    s3[s3.Year==3000] = np.NaN
    s2[s2.Year==2010] = np.NaN
    s1.dropna(inplace=True)
    s2.dropna(inplace=True)
    s3.dropna(inplace=True)
    
    trace1 = go.Bar(x=s1.Year,y=s1.id,name='playstation', marker= dict(color='rgba(255,174,255,0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace2 = go.Bar(x=s2.Year,y=s2.id,name='xbox', marker= dict(color='rgba(255, 255, 128, 0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace3 = go.Bar(x=s3.Year,y=s3.id,name='switch', marker= dict(color='skyblue',line = dict(color='rgb(0,0,0)', width = 1.5)))
    data = [trace1,trace2,trace3]
    layout = go.Layout(title ='Cantidad de juegos que han salido en Europa, filtrado por plataformas',barmode='group')
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig,use_container_width=True)

    
    s2 = pd.DataFrame(df_xb.groupby('Year Jp').sum('id'))
    s3 = pd.DataFrame(df_sw.groupby('Year Jp').sum('id'))
    s1 = pd.DataFrame(df_pd.groupby('Year Jp').sum('id'))
    s1 ['Year'] = s1.index
    s2 ['Year'] = s2.index
    s3 ['Year']= s3.index
    s1[s1.Year==3000] = np.NaN
    s2[s2.Year==3000] = np.NaN
    s3[s3.Year==3000] = np.NaN
    s2[s2.Year==2010] = np.NaN
    s1.dropna(inplace=True)
    s2.dropna(inplace=True)
    s3.dropna(inplace=True)
    trace1 = go.Bar(x=s1.Year,y=s1.id,name='playstation', marker= dict(color='rgba(255,174,255,0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace2 = go.Bar(x=s2.Year,y=s2.id,name='xbox', marker= dict(color='rgba(255, 255, 128, 0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace3 = go.Bar(x=s3.Year,y=s3.id,name='switch', marker= dict(color='skyblue',line = dict(color='rgb(0,0,0)', width = 1.5)))
    data = [trace1,trace2,trace3]
    layout = go.Layout(title ='Cantidad de juegos que han salido en Japón, filtrado por plataformas',barmode='group')
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig,use_container_width=True)

    s2 = pd.DataFrame(df_xb.groupby('Year Au').sum('id'))
    s3 = pd.DataFrame(df_sw.groupby('Year Au').sum('id'))
    s1 = pd.DataFrame(df_pd.groupby('Year Au').sum('id'))
    
    s1 ['Year'] = s1.index
    s2 ['Year'] = s2.index
    s3 ['Year']= s3.index
    s1[s1.Year==3000] = np.NaN
    s2[s2.Year==3000] = np.NaN
    s3[s3.Year==3000] = np.NaN
    s2[s2.Year==2010] = np.NaN
    s1.dropna(inplace=True)
    s2.dropna(inplace=True)
    s3.dropna(inplace=True)
    trace1 = go.Bar(x=s1.Year,y=s1.id,name='playstation', marker= dict(color='rgba(255,174,255,0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace2 = go.Bar(x=s2.Year,y=s2.id,name='xbox', marker= dict(color='rgba(255, 255, 128, 0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace3 = go.Bar(x=s3.Year,y=s3.id,name='switch', marker= dict(color='skyblue',line = dict(color='rgb(0,0,0)', width = 1.5)))
    data = [trace1,trace2,trace3]
    layout = go.Layout(title ='Cantidad de juegos que han salido en Australia, filtrado por plataformas',barmode='group')
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig,use_container_width=True)
    
    s2 = pd.DataFrame(df_xb.groupby('Year Na').sum('id'))
    s3 = pd.DataFrame(df_sw.groupby('Year Na').sum('id'))
    s1 = pd.DataFrame(df_pd.groupby('Year Na').sum('id'))
    s1 ['Year'] = s1.index
    s2 ['Year'] = s2.index
    s3 ['Year']= s3.index
    s1[s1.Year==3000] = np.NaN
    s2[s2.Year==3000] = np.NaN
    s3[s3.Year==3000] = np.NaN
    s2[s2.Year==2010] = np.NaN
    s1.dropna(inplace=True)
    s2.dropna(inplace=True)
    s3.dropna(inplace=True)
    trace1 = go.Bar(x=s1.Year,y=s1.id,name='playstation', marker= dict(color='rgba(255,174,255,0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace2 = go.Bar(x=s2.Year,y=s2.id,name='xbox', marker= dict(color='rgba(255, 255, 128, 0.5)',line = dict(color='rgb(0,0,0)', width = 1.5)))
    trace3 = go.Bar(x=s3.Year,y=s3.id,name='switch', marker= dict(color='skyblue',line = dict(color='rgb(0,0,0)', width = 1.5)))
    data = [trace1,trace2,trace3]
    layout = go.Layout(title ='Cantidad de juegos que han salido en Norte América, filtrado por plataformas',barmode='group')
    fig = go.Figure(data=data,layout=layout)
    st.plotly_chart(fig,use_container_width=True)
    
  






















