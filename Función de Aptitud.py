def apt_fit(individuo):
    fittnes=0
    for i in range(0,8):
        y1=individuo[i]
        for j in range(i+1,8):
            y2=individuo[j]
            m=np.abs((y2-y1)/(j-i))
            if m==1:
                fittnes+=1
    return fittnes
