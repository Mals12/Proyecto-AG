import random as rm
from funcion_aptitud import apt_fit
def selec_padres(poblacion):
    pro_sel=[]
    pro_acu=[]
    pobla_padres=[]
    pobla_orden=sorted(poblacion,key=apt_fit)
    for i in range(1,len(poblacion)+1):
        prosel=(len(poblacion)-i+1)/((len(poblacion)*(len(poblacion)+1))/2)
        pro_sel.append(prosel)
        proacu=sum(pro_sel)
        pro_acu.append(proacu)
    while len(pobla_padres)<len(poblacion):
        r_1=rm.random()
        r_2=rm.random()
        c_1=0
        c_2=0
        while pro_acu[c_1]<r_1:
            c_1+=1
        while pro_acu[c_2]<r_2:
            c_2+=1
        papa_1=pobla_orden[c_1]
        papa_2=pobla_orden[c_2]
        pobla_padres.append(papa_1)
        pobla_padres.append(papa_2)
    return pobla_padres