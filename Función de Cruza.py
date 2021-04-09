def cruza_extre(pobla_padres):
    pobla_hijos=[]
    for i in range(0,25):
        papa1=pobla_padres[2*i]
        papa2=pobla_padres[2*i+1]
        khijo=[]
        khijo2=[]
        e=[]
        for i in range(0,8):
            pos_en_papa2 = papa2.index(papa1[i])
            if i <= 6:
                if pos_en_papa2 != 7:
                    ex = [papa1[i - 1], papa1[i + 1], papa2[pos_en_papa2 - 1], papa2[pos_en_papa2 + 1]]
                    e.append(ex)
                else:
                    ex = [papa1[i - 1], papa1[i + 1], papa2[pos_en_papa2 - 1], papa2[i - i]]
                    e.append(ex)
            else:
                if pos_en_papa2 != 7:
                    ex = [papa1[i - 1], papa1[i - i], papa2[pos_en_papa2 - 1], papa2[pos_en_papa2 + 1]]
                    e.append(ex)
                else:
                    ex = [papa1[i - 1], papa1[i - i], papa2[pos_en_papa2 - 1], papa2[i - i]]
                    e.append(ex)
        #print(e)
        N=rm.randrange(0,8)
        while len(khijo)<len(papa1):
            khijo.append(N)
            cokhijo=khijo.copy()
            #print(khijo)
            for m in range(0,2):
                for i in range(len(e)):
                    if N in e[i]:
                        posN=e[i].index(N)
                        e[i].pop(posN)
            inde=papa1.index(N)
            lista_ext_N=e[inde]
            if len(lista_ext_N)!=0:
                ele_leN = lista_ext_N
                elem_rep=[x for x,y in collections.Counter(ele_leN).items() if y>1]
                if len(elem_rep)== 1 or len(elem_rep)==2:
                    N=elem_rep[0]
                else:
                    jlon=[]
                    jpos=[]
                    for i in range(len(lista_ext_N)):
                        pos_leN=papa1.index(lista_ext_N[i])
                        jpos.append(pos_leN)
                        lisext_pos_leN=e[pos_leN]
                        jlon.append(len(lisext_pos_leN))
                    elerep_jlon=[x for x,y in collections.Counter(jlon).items() if y>1]
                    x=min(jlon)
                    if x in elerep_jlon:
                        g=[]
                        for i in range(0,8):
                            if i not in cokhijo:
                                g.append(i)
                        while len(cokhijo)<8:
                            Nn=rm.choice(g)
                            g.remove(Nn)
                            cokhijo.append(Nn)
                        N=Nn
                    else:
                        x_jlon=jlon.index(x)
                        x_jpos=jpos[x_jlon]
                        N=papa1[x_jpos]
            else:
                g=[]
                for i in range(0,8):
                    if i not in cokhijo:
                        g.append(i)
                while len(cokhijo)<8:
                    Nn=rm.choice(g)
                    g.remove(Nn)
                    cokhijo.append(Nn)
                N=Nn
        N=rm.randrange(0,8)
        while len(khijo2)<len(papa1):
            khijo2.append(N)
            cokhijo2=khijo2.copy()
            #print(khijo2)
            for m in range(0,2):
                for i in range(len(e)):
                    if N in e[i]:
                        posN=e[i].index(N)
                        e[i].pop(posN)
            inde=papa1.index(N)
            lista_ext_N=e[inde]
            if len(lista_ext_N)!=0:
                ele_leN = lista_ext_N
                elem_rep=[x for x,y in collections.Counter(ele_leN).items() if y>1]
                if len(elem_rep)== 1 or len(elem_rep)==2:
                    N=elem_rep[0]
                else:
                    jlon=[]
                    jpos=[]
                    for i in range(len(lista_ext_N)):
                        pos_leN=papa1.index(lista_ext_N[i])
                        jpos.append(pos_leN)
                        lisext_pos_leN=e[pos_leN]
                        jlon.append(len(lisext_pos_leN))
                    elerep_jlon=[x for x,y in collections.Counter(jlon).items() if y>1]
                    x=min(jlon)
                    if x in elerep_jlon:
                        g=[]
                        for i in range(0,8):
                            if i not in cokhijo2:
                                g.append(i)
                        while len(cokhijo2)<8:
                            Nn=rm.choice(g)
                            g.remove(Nn)
                            cokhijo2.append(Nn)
                        N=Nn
                    else:
                        x_jlon=jlon.index(x)
                        x_jpos=jpos[x_jlon]
                        N=papa1[x_jpos]
            else:
                g=[]
                for i in range(0,8):
                    if i not in cokhijo2:
                        g.append(i)
                while len(cokhijo2)<8:
                    Nn=rm.choice(g)
                    g.remove(Nn)
                    cokhijo2.append(Nn)
                N=Nn
        pobla_hijos.append(khijo)
        pobla_hijos.append(khijo2)
    return pobla_hijos
