def Tri_insertion(tab):
    tab=[18,47,8,21,34]
    for i in range(1,n):
        j=i
        memoire=tab[i]
        while j>0 and memoire<tab[j-1]:
            tab[j-1],tab[j] = tab[j],tab[j-1]
            j = j - 1
        tab[j]=memoire
    return j