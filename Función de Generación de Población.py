def crea_poblacion(num_individuos):
    poblacion=[]
    for i in range(0,num_individuos):
        individuo=[]
        vec=[0,1,2,3,4,5,6,7]
        while len(individuo)<8:
            n=rm.choice(vec)
            vec.remove(n)
            individuo.append(n)
        poblacion.append(individuo)
    return poblacion