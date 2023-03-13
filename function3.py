from plotly.offline import  iplot
from plotly.io import write_image
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np


#plotly

def tarta_Comp(df):
    
    x=pd.DataFrame(df.Comp.value_counts())

    fig={'data':[{'values':x.Comp,'labels':x.index,'domain':{'x':[0,0.7]},'name':'','hoverinfo':'label+value','hole':0.5,'type':'pie'},],
         'layout':{'title':'Región de Lanzamiento de juegos'}}
    iplot(fig)

def plataforma_year(df):
    
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
    iplot(fig)

    
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
    iplot(fig)

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
    iplot(fig)
    
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
    iplot(fig)

#seaborn

def juegos_genero(df): 
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
    sb.countplot(x=df1.genre)
    plt.xticks(rotation=-45);
    plt.title('Cantidad de juegos de los principales generos')


#matplotlib.pyplot

def juegos_mes(df):
    
    conteo = df['Mes Eu'].value_counts(ascending=True)
    plt.figure(figsize=(10,5))
    plt.hlines(y=conteo.index,xmin=0,xmax=conteo,color ='skyblue')
    plt.plot(conteo,conteo.index,'o')
    plt.title('Cantidad de juegos que han salido cada mes en Europa')
    
    

    conteo = df['Mes Na'].value_counts(ascending=True)
    plt.figure(figsize=(10,5))
    plt.hlines(y=conteo.index,xmin=0,xmax=conteo,color ='skyblue')
    plt.plot(conteo,conteo.index,'o')
    plt.title('Cantidad de juegos que han salido cada mes en Norte América')
    
    
    conteo = df['Mes Jp'].value_counts(ascending=True)
    plt.figure(figsize=(10,5))
    plt.hlines(y=conteo.index,xmin=0,xmax=conteo,color ='skyblue')
    plt.plot(conteo,conteo.index,'o')
    plt.title('Cantidad de juegos que han salido cada mes en Japón')

    conteo = df['Mes Au'].value_counts(ascending=True)
    plt.figure(figsize=(10,5))
    plt.hlines(y=conteo.index,xmin=0,xmax=conteo,color ='skyblue')
    plt.plot(conteo,conteo.index,'o')
    plt.title('Cantidad de juegos que han salido cada mes en Australia')

    
    
