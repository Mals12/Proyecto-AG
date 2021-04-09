from funcion_aptitud import apt_fit
from funcion_poblacion import crea_poblacion
from funcion_seleccion_padres import selec_padres
from funcion_cruza import cruza_extre
from funcion_mutación import mut_inser
from funcion_reemplazo import reem_generacional
import numpy as np
import random as rm
import collections
import pandas as pd
import matplotlib.pyplot as plt

pobla_inicial=crea_poblacion(50)
generaciones=[]
mejor_fitness=[]
mejor_individuo=[]
peor_fitness=[]
peor_individuo=[]
individuo_promedio=[]
des_estandar=[]

for i in range(0,50):
    pobla_padres=selec_padres(pobla_inicial)
    pobla_hijos=cruza_extre(pobla_padres)
    pobla_mutada=mut_inser(pobla_hijos)
    pobla_inicial=reem_generacional(pobla_mutada)
    generaciones.append(pobla_inicial)

    ''' Mejor fitness por generacion '''
    fit_pobla=[]
    for i in range(len(pobla_inicial)):
        fit_individuo=apt_fit(pobla_inicial[i])
        fit_pobla.append(fit_individuo)
    men_fit=min(fit_pobla)
    mejor_fitness.append(men_fit)
    indiv_con_men_fit=0
    for i in range(len(pobla_inicial)):
        if men_fit==fit_pobla[i]:
            indiv_con_men_fit +=1
    mejor_individuo.append(indiv_con_men_fit)

    ''' Peor fitness por generacion '''
    may_fit = max(fit_pobla)
    peor_fitness.append(may_fit)
    indiv_con_may_fit = 0
    for i in range(len(pobla_inicial)):
        if may_fit ==fit_pobla[i]:
            indiv_con_may_fit += 1
    peor_individuo.append(indiv_con_may_fit)

    ''' Fitness promedio por generaion'''
    prom = sum(fit_pobla)/len(fit_pobla)
    individuo_promedio.append(prom)

    ''' Desviación estandar'''
    de_es=0
    for i in range(len(fit_pobla)):
        des=(fit_pobla[i]-prom)**2
        de_es +=des
    var=de_es/(len(fit_pobla))
    des_est=np.sqrt(var)
    des_estandar.append(des_est)

''' Cracion de tabla '''
num_generacion=range(50)
lis_num_generacion=list(num_generacion)
dict={'M. Fit': mejor_fitness,
      'C.I.M Fit': mejor_individuo,
       'P. Fit)':peor_fitness,
       'C.I.P Fit':peor_individuo,
        'Fit Prom':individuo_promedio,
       'Des. Est':des_estandar}
tabla=pd.DataFrame(dict)
tabla.index=lis_num_generacion
print(tabla)
''' Grafica del mejor individuo '''
plt.style.use('ggplot')
fig,ax=plt.subplots(figsize=(15,10))
x=np.linspace(0,49,50)
y=mejor_fitness
plt.plot(x,y,'b')
plt.title('$Grafica\ de\ Convergencia$', loc="center", fontdict={'fontsize':16, 'fontweight':'bold','color':'tab:green'})
plt.grid()
