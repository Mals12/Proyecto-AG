def selec_padres(poblacion):
    padres=[]
    lisvacia=poblacion.copy()
    while len(lisvacia)>0:
        papa1=rm.choice(lisvacia)
        lisvacia.remove(papa1)
        papa2=rm.choice(lisvacia)
        lisvacia.remove(papa2)
        padres.append(papa1)
        padres.append(papa2)
    return padres