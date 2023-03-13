def comparador_fechas(Eu,Na): #devolverá una lista de strings donde pondrá NA,EU o NA EU
    fechas_comparadas=[]
    for x in range(len(Eu)):
        
        if Eu[x][0]>Na[x][0]:
            fechas_comparadas.append('NA')
        elif  Eu[x][0]<Na[x][0]:
            fechas_comparadas.append('EU')
        elif (Eu[x][0]==Na[x][0]) & (Eu[x][1]>Na[x][1]):
            fechas_comparadas.append('NA')
        elif (Eu[x][0]==Na[x][0])& (Eu[x][1]<Na[x][1]):
            fechas_comparadas.append('EU')
        elif (Eu[x][0]==Na[x][0]) & (Eu[x][1]==Na[x][1])&(Eu[x][2]>Na[x][2]):
            fechas_comparadas.append('NA')
        elif (Eu[x][0]==Na[x][0])& (Eu[x][1]==Na[x][1])&(Eu[x][2]<Na[x][2]):
            fechas_comparadas.append('EU')
        elif (Eu[x][0]==Na[x][0] )& (Eu[x][1]==Na[x][1]) & (Eu[x][2]==Na[x][2]) :
            fechas_comparadas.append('NA EU')
    return fechas_comparadas

def comparador_fechas_str(a1,a2,lista): #devolverá una lista de strings donde pondrá NA,EU o NA EU
    fecha=''    
    if a1[0]>a2[0]:
        fecha=lista[1]
    elif a1[0]<a2[0]:
            fecha=lista[0]
    elif (a1[0]==a2[0]) & (a1[1]>a2[1]):
        fecha= lista[1]
    elif (a1[0]==a2[0])& (a1[1]<a2[1]):
        fecha = lista[0]
    elif (a1[0]==a2[0]) & (a1[1]==a2[1])&(a1[2]>a2[2]):
        fecha=lista[1]
    elif (a1[0]==a2[0]) & (a1[1]==a2[1])&(a1[2]<a2[2]):
        fecha=lista[0]
    else:
        fecha=lista[0]+' '+lista[1]
        
    return fecha

def comparador_fechas_4(Eu,Na,Jp,Au):
    a= comparador_fechas(Eu,Na)
    for x in range(len(Eu)):
        lista = []
        lista.append(a[x])
        lista.append('JP')
        
        if 'EU' in a[x]:
            a[x] = comparador_fechas_str(Eu[x],Jp[x],lista)
        elif 'NA' in a[x]:
            a[x] = comparador_fechas_str(Na[x],Jp[x],lista)
    
    for x in range(len(Eu)):
        lista = []
        lista.append(a[x])
        lista.append('AU')
        if 'EU' in a[x]:
            a[x] = comparador_fechas_str(Eu[x],Au[x],lista)
        elif 'NA' in a[x]:
            a[x] = comparador_fechas_str(Na[x],Au[x],lista)
        elif 'JP' in a[x]:
            a[x] = comparador_fechas_str(Na[x],Au[x],lista)
    
    return a
        
def lista_Comp_ps (pd_playstation):
    meses = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fecha_Na_ps =[]
    for x in pd_playstation.iloc[:,3]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                        fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)
        fecha_Na_ps.append(fecha)

    fecha_Eu_ps =[]
    for x in pd_playstation.iloc[:,4]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)
        fecha_Eu_ps.append(fecha) 

    fecha_Jp_ps =[]
    for x in pd_playstation.iloc[:,2]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)
        fecha_Jp_ps.append(fecha)

    fecha_Au_ps =[]
    for x in pd_playstation.iloc[:,5]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)
        fecha_Au_ps.append(fecha)
    lista = comparador_fechas_4(fecha_Eu_ps,fecha_Na_ps,fecha_Jp_ps,fecha_Au_ps)
    a= [lista,fecha_Eu_ps,fecha_Na_ps,fecha_Jp_ps,fecha_Au_ps]
    return a


def lista_Comp_xb (pd_xbox):
    fecha_Na_xbox =[]
    meses = ['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for x in pd_xbox.iloc[:,3]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)
        fecha_Na_xbox.append(fecha)

    fecha_Eu_xbox =[]
    for x in pd_xbox.iloc[:,4]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)

        fecha_Eu_xbox.append(fecha)     

    fecha_Jp_xbox =[]
    for x in pd_xbox.iloc[:,2]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)

        fecha_Jp_xbox.append(fecha) 

    fecha_Au_xbox =[]
    for x in pd_xbox.iloc[:,5]:
        fecha=[]
        if x =='0':
            fecha.append(3000)
            fecha.append(0)
            fecha.append(0)
        elif len(x)>8:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(int(x[4:-6]))
        elif len(x)>4 &len(x)<9:
            fecha.append(int(x[-4:]))
            for y in range(1,13):
                if meses[y-1]==x[0:3]:
                    fecha.append(y)
            fecha.append(0)
        else:
        
            fecha.append(int(x))
            fecha.append(0)
            fecha.append(0)

        fecha_Au_xbox.append(fecha) 
    lista = comparador_fechas_4(fecha_Eu_xbox,fecha_Na_xbox,fecha_Jp_xbox,fecha_Au_xbox)
    a =[lista,fecha_Eu_xbox,fecha_Na_xbox,fecha_Jp_xbox,fecha_Au_xbox]
    return a

def lista_Comp_sw (pd_switch):
    fecha_Na_sw =[]
    meses = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    for x in pd_switch.iloc[:,3]:
    
        fecha1=[]
        if x == '0':
            fecha1.append(3000)
            fecha1.append(0)
            fecha1.append(0)
        elif len(x)==4:
            fecha1.append(int(x))
            fecha1.append(0)
            fecha1.append(0)
        elif not(','in x):
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[1]))
            fecha1.append(fecha[0])
            fecha1.append(0)
        else:
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[2]))
            fecha1.append(fecha[0])
            fecha1.append(int(fecha[1].replace(',','')))
        fecha_Na_sw.append(fecha1)

    fecha_Eu_sw =[]
    for x in pd_switch.iloc[:,4]:
        fecha1=[]
        if x == '0':
            fecha1.append(3000)
            fecha1.append(0)
            fecha1.append(0)
        elif len(x)==4:
            fecha1.append(int(x))
            fecha1.append(0)
            fecha1.append(0)
        elif not(','in x):
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[1]))
            fecha1.append(fecha[0])
            fecha1.append(0)
        else:   
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[2]))
            fecha1.append(fecha[0])
            fecha1.append(int(fecha[1].replace(',','')))
        fecha_Eu_sw.append(fecha1)  

    fecha_Jp_sw=[]
    for x in pd_switch.iloc[:,2]:
        fecha1=[]
        if x == '0':
            fecha1.append(3000)
            fecha1.append(0)
            fecha1.append(0)
        elif len(x)==4:
            fecha1.append(int(x))
            fecha1.append(0)
            fecha1.append(0)
        elif not(','in x):
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[1]))
            fecha1.append(fecha[0])
            fecha1.append(0)
        else:
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[2]))
            fecha1.append(fecha[0])
            fecha1.append(int(fecha[1].replace(',','')))
        fecha_Jp_sw.append(fecha1)  

    fecha_Au_sw =[]
    for x in pd_switch.iloc[:,5]:
        fecha1=[]
        if x  == '0':
            fecha1.append(3000)
            fecha1.append(0)
            fecha1.append(0)
        elif len(x)==4:
            fecha1.append(int(x))
            fecha1.append(0)
            fecha1.append(0)
        elif not(','in x):
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[1]))
            fecha1.append(fecha[0])
            fecha1.append(0)
        else:
            fecha=x.split()
            for y in range(1,13):
                if meses[y-1]==fecha[0]:
                    fecha[0]=y
            fecha1.append(int(fecha[2]))
            fecha1.append(fecha[0])
            fecha1.append(int(fecha[1].replace(',','')))
        fecha_Au_sw.append(fecha1)  
    lista = comparador_fechas_4(fecha_Eu_sw,fecha_Na_sw,fecha_Jp_sw,fecha_Au_sw)
    a= [lista,fecha_Eu_sw,fecha_Na_sw,fecha_Jp_sw,fecha_Au_sw]
    return a