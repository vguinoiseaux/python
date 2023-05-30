def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis

objets=[[6,5.0,'chaussures'],[5,5.0,'habits'],[4.5,2.0,'trousse de toilette'],[4,2.0,'crêmes'],[3,8.0,'livres'],[2,2.0,'palmes tuba'],[1,0.5,'guide touristique']]

poidsMax=23
print('Les objets choisis sont')
print('poids max embarqué',poidsMax)
objetsChoisis=remplirSac(objets,poidsMax)
for n in range(len(objetsChoisis)):
   if objetsChoisis[n]==1:
      print(objets[n][2])