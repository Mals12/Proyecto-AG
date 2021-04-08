def selec_padres(poblacion):
    fittotal=0
    pro_selec=[]
    val_esp=[]
    padres=[]
    for i in range(0,25):
        for i in range(len(poblacion)):
            fittotal+=apt_fit(poblacion[i])
        for i in range(len(poblacion)):
            proselec=apt_fit(poblacion[i])/fittotal
            pro_selec.append(proselec)
            valesp=pro_selec[i]*50
            val_esp.append(valesp)
            ele_max=max(pro_selec)
            pos_pro_selec=pro_selec.index(ele_max)
            papa1=poblacion[pos_pro_selec]
            ele_min=min(val_esp)
            pos_val_esp=val_esp.index(ele_min)
            papa2=poblacion[pos_val_esp]
        padres.append(papa1)
        padres.append(papa2)
    return padres