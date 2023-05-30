L=[0,1,2,3,4,5,6,7]
classes=['R','T','C','C','C','R','R','R']
x=8
k=3

def distance(L,classes):
    return abs(L-classes)

def Kvoisins(L,k,x):
    listeDistanceIndice=[]
    for i in range(len(L)):
        d= distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort()
    voisins=[]
    for i in range(k):
       voisins.append(listeDistanceIndice[i][1])
    return voisins

print('liste des indices',Kvoisins(L,k,x))

def predireClasse(L,classes,k,x):
    voisins=Kvoisins(L,k,x)
    classespossibles = ['C','T','R']
    decompte=[0,0,0]
    for v in voisins:
        if classes[v]=='C':
            decompte[0] +=1
        elif classes[v]=='T':
            decompte[1] +=1
        elif classes[v]=='R':
            decompte[2] +=1
    if decompte[0]>decompte[1] and decompte[0]>decompte[2]:
        classeChoisie=classespossibles[0]
    elif decompte[1]>decompte[2] and decompte[1]>decompte[0]:
        classeChoisie=classespossibles[1]
    elif decompte[2]>decompte[0] and decompte[2]>decompte[1]:
        classeChoisie=classespossibles[2]
    return  classeChoisie

print('classe du nouvel element',predireClasse(L,classes,k,x))