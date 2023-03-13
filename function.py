import numpy as np
import pandas as pd
import requests as rq
import json

def crear_pd_xb():
    #Creamos el DataFrame de Xbox

    url = 'https://api.sampleapis.com/xbox/games'
    response = rq.get(url)
    a = response.json()

    id = []
    name = []
    genre= []
    developers =[]
    rdJapan=[]
    rdNorthAmerica=[]
    rdEurope=[]
    rdAustralia=[]

    for x in a:
        id.append(x['id'])
        name.append(x['name'])
        genre.append(x['genre'])
        developers.append(x['developers'])
        y= x['releaseDates']
        rdJapan.append(y['Japan'])
        rdNorthAmerica.append(y['NorthAmerica'])
        rdEurope.append(y['Europe'])
        rdAustralia.append(y['Australia'])

    dict_xbox={'id':id,'name':name,'genre':genre,'rdJapan':rdJapan,'rdNorthAmerica':rdNorthAmerica,'rdEurope':rdEurope,'rdAustralia':rdAustralia}
    pd_xbox = pd.DataFrame(dict_xbox)
    return pd_xbox

def crear_pd_sw():
    #Creamos el DataFrame de Switch

    url1 = 'https://api.sampleapis.com/switch/games'
    response = rq.get(url1)
    a1 = response.json()

    id = []
    name = []
    genre= []
    developers =[]
    rdJapan=[]
    rdNorthAmerica=[]
    rdEurope=[]
    rdAustralia=[]

    for x in a1:
        id.append(x['id'])
        name.append(x['name'])
        genre.append(x['genre'])
        developers.append(x['developers'])
        y= x['releaseDates']
        rdJapan.append(y['Japan'])
        rdNorthAmerica.append(y['NorthAmerica'])
        rdEurope.append(y['Europe'])
        rdAustralia.append(y['Australia'])

    dict={'id':id,'name':name,'genre':genre,'rdJapan':rdJapan,'rdNorthAmerica':rdNorthAmerica,'rdEurope':rdEurope,'rdAustralia':rdAustralia}
    pd_switch = pd.DataFrame(dict)
    return pd_switch

def crear_pd_ps():
    url2 = 'https://api.sampleapis.com/playstation/games'
    response = rq.get(url2)
    a2 = response.json()

    id = []
    name = []
    genre= []
    developers =[]
    rdJapan=[]
    rdNorthAmerica=[]
    rdEurope=[]
    rdAustralia=[]

    for x in a2:
        id.append(x['id'])
        name.append(x['name'])
        genre.append(x['genre'])
        developers.append(x['developers'])
        y= x['releaseDates']
        rdJapan.append(y['Japan'])
        rdNorthAmerica.append(y['NorthAmerica'])
        rdEurope.append(y['Europe'])
        rdAustralia.append(y['Australia'])

    dict={'id':id,'name':name,'genre':genre,'rdJapan':rdJapan,'rdNorthAmerica':rdNorthAmerica,'rdEurope':rdEurope,'rdAustralia':rdAustralia}
    pd_playstation = pd.DataFrame(dict)
    return pd_playstation


def lista_fechas(lista):
    fecha=[[],[],[]]
    for x in lista:
        fecha[0].append(x[0])
        fecha[1].append(x[1])
        fecha[2].append(x[2])
    return fecha

def delete(pd_playstation):
    del(pd_playstation['rdAustralia'])
    del(pd_playstation['rdEurope']) 
    del(pd_playstation['rdJapan'])
    del(pd_playstation['rdNorthAmerica'])

    return pd_playstation

def arreglar_ps (pd_playstation):
    pd_playstation.rdEurope[pd_playstation['rdEurope'].isin(['TBA','Assorted','Q3 2020'])]=np.NAN
    pd_playstation.rdNorthAmerica[pd_playstation['rdNorthAmerica'].isin(['TBA','Assorted','Q3 2020'])]=np.NAN
    pd_playstation.rdJapan[pd_playstation['rdJapan'].isin(['TBA','Assorted','Q3 2020'])]=np.NAN
    pd_playstation.rdAustralia[pd_playstation['rdAustralia'].isin(['TBA','Assorted','Q3 2020'])]=np.NAN
    pd_playstation.rdEurope[pd_playstation['rdEurope'].isin(['Unreleased'])]='0'
    pd_playstation.rdJapan[pd_playstation['rdJapan'].isin(['Unreleased'])]='0'
    pd_playstation.rdAustralia[pd_playstation['rdAustralia'].isin(['Unreleased'])]='0'
    pd_playstation.rdNorthAmerica[pd_playstation['rdNorthAmerica'].isin(['Unreleased'])]='0'
    pd_playstation.dropna(inplace=True)
    return pd_playstation

def arreglar_sw(pd_switch):
    pd_switch.rdEurope[pd_switch['rdEurope'].isin(['TBA','Assorted','Q3 2020','Early Access',"Error in Template:Date table sorting: 'Dex' is not a valid month"])]=np.NAN
    pd_switch.rdNorthAmerica[pd_switch['rdNorthAmerica'].isin(['TBA','Assorted','Early Access0','Q3 2020'])]=np.NAN
    pd_switch.rdJapan[pd_switch['rdJapan'].isin(['TBA','Assorted','Early Access','Q3 2020'])]=np.NAN
    pd_switch.rdAustralia[pd_switch['rdAustralia'].isin(['TBA','Assorted','Early Access','Q3 2020'])]=np.NAN
    pd_switch.rdEurope[pd_switch['rdEurope'].isin(['Unreleased'])]='0'
    pd_switch.rdJapan[pd_switch['rdJapan'].isin(['Unreleased'])]='0'
    pd_switch.rdAustralia[pd_switch['rdAustralia'].isin(['Unreleased'])]='0'
    pd_switch.rdNorthAmerica[pd_switch['rdNorthAmerica'].isin(['Unreleased'])]='0'
    pd_switch.dropna(inplace=True)
    return pd_switch

def arreglar_xbox(pd_xbox):
    pd_xbox.rdEurope[pd_xbox['rdEurope'].isin(['TBA','Assorted','Q3 2020','Early Access',"Error in Template:Date table sorting: 'Dex' is not a valid month"])]=np.NAN
    pd_xbox.rdNorthAmerica[pd_xbox['rdNorthAmerica'].isin(['TBA','Assorted','Early Access','Q3 2020'])]=np.NAN
    pd_xbox.rdJapan[pd_xbox['rdJapan'].isin(['TBA','Assorted','Early Access','Q3 2020'])]=np.NAN
    pd_xbox.rdAustralia[pd_xbox['rdAustralia'].isin(['TBA','Assorted','Early Access','Q3 2020'])]=np.NAN
    pd_xbox.rdEurope[pd_xbox['rdEurope'].isin(['Unreleased'])]='0'
    pd_xbox.rdNorthAmerica[pd_xbox['rdNorthAmerica'].isin(['Unreleased'])]='0'
    pd_xbox.rdJapan[pd_xbox['rdJapan'].isin(['Unreleased'])]='0'
    pd_xbox.rdAustralia[pd_xbox['rdAustralia'].isin(['Unreleased'])]='0'
    pd_xbox.dropna(inplace=True)
    return pd_xbox


def arreglar_genre_sw(pd_switch):
    pd_switch.genre[pd_switch.genre.isin([[]])]= [['Sin genero']]
    genre = []
    for x in pd_switch.iloc[:,2]:
        if x =='Sin genero':
            genre.append('Sin genero')
        else:
            genre.append(x[0])
    del(pd_switch['genre'])
    pd_switch['genre']=genre
    return pd_switch

def arreglar_genre_ps(pd_playstation):
    pd_playstation.genre[pd_playstation.genre.isin([[]])]= [['Sin genero']]
    genre=[]
    for x in pd_playstation.iloc[:,2]:
        if x =='Sin genero':
            genre.append('Sin genero')
        else:
            genre.append(x[0])
    del(pd_playstation['genre'])
    pd_playstation['genre']=genre
    return pd_playstation

def arreglar_genre_xb(pd_xbox):
    pd_xbox.genre[pd_xbox.genre.isin([[]])]= [['Sin genero']]
    genre=[]
    for x in pd_xbox.iloc[:,2]:
        if x =='Sin genero':
            genre.append('Sin genero')
        else:
            genre.append(x[0])
    del(pd_xbox['genre'])
    pd_xbox['genre']=genre
    return pd_xbox

def pd_sw_final (pd_switch,lista_sw):
    afecha_sw_Eu = lista_fechas(lista_sw[1])
    afecha_sw_Na = lista_fechas(lista_sw[2])
    afecha_sw_Jp = lista_fechas(lista_sw[3])
    afecha_sw_Au = lista_fechas(lista_sw[4])

    pd_switch['Year Eu'] = afecha_sw_Eu[0]
    pd_switch['Mes Eu'] = afecha_sw_Eu[1]
    pd_switch['Dia Eu'] = afecha_sw_Eu[2]
    pd_switch['Year Na'] = afecha_sw_Na[0]
    pd_switch['Mes Na'] = afecha_sw_Na[1]
    pd_switch['Dia Na'] = afecha_sw_Na[2]
    pd_switch['Year Jp'] = afecha_sw_Jp[0]
    pd_switch['Mes Jp'] = afecha_sw_Jp[1]
    pd_switch['Dia Jp'] = afecha_sw_Jp[2]
    pd_switch['Year Au'] = afecha_sw_Au[0]
    pd_switch['Mes Au'] = afecha_sw_Au[1]
    pd_switch['Dia Au'] = afecha_sw_Au[2]
    return pd_switch

def pd_xb_final(pd_xbox,lista_xb):
    afecha_xb_Eu = lista_fechas(lista_xb[1])
    afecha_xb_Na = lista_fechas(lista_xb[2])
    afecha_xb_Jp = lista_fechas(lista_xb[3])
    afecha_xb_Au = lista_fechas(lista_xb[4])

    pd_xbox['Year Eu'] = afecha_xb_Eu[0]
    pd_xbox['Mes Eu'] = afecha_xb_Eu[1]
    pd_xbox['Dia Eu'] = afecha_xb_Eu[2]
    pd_xbox['Year Na'] = afecha_xb_Na[0]
    pd_xbox['Mes Na'] = afecha_xb_Na[1]
    pd_xbox['Dia Na'] = afecha_xb_Na[2]
    pd_xbox['Year Jp'] = afecha_xb_Jp[0]
    pd_xbox['Mes Jp'] = afecha_xb_Jp[1]
    pd_xbox['Dia Jp'] = afecha_xb_Jp[2]
    pd_xbox['Year Au'] = afecha_xb_Au[0]
    pd_xbox['Mes Au'] = afecha_xb_Au[1]
    pd_xbox['Dia Au'] = afecha_xb_Au[2]
    return pd_xbox

def pd_ps_final(pd_playstation,lista_ps):
    afecha_ps_Eu = lista_fechas(lista_ps[1])
    afecha_ps_Na = lista_fechas(lista_ps[2])
    afecha_ps_Jp = lista_fechas(lista_ps[3])
    afecha_ps_Au = lista_fechas(lista_ps[4])

    pd_playstation['Year Eu'] = afecha_ps_Eu[0]
    pd_playstation['Mes Eu'] = afecha_ps_Eu[1]
    pd_playstation['Dia Eu'] = afecha_ps_Eu[2]
    pd_playstation['Year Na'] = afecha_ps_Na[0]
    pd_playstation['Mes Na'] = afecha_ps_Na[1]
    pd_playstation['Dia Na'] = afecha_ps_Na[2]
    pd_playstation['Year Jp'] = afecha_ps_Jp[0]
    pd_playstation['Mes Jp'] = afecha_ps_Jp[1]
    pd_playstation['Dia Jp'] = afecha_ps_Jp[2]
    pd_playstation['Year Au'] = afecha_ps_Au[0]
    pd_playstation['Mes Au'] = afecha_ps_Au[1]
    pd_playstation['Dia Au'] = afecha_ps_Au[2]
    return pd_playstation
