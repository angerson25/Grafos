grafo={"F":["B","G"],"B":["A","D","J"],"":["D"]}
origen=input("Digite origen: ")
if origen.upper() not in grafo:
    print("El nodo no esta en el grafo")


else:
    un=[]
    dos=[]
    recorrido=[]
    visitados=[origen]
    while (len(visitados))!=0:
        nodo=visitados.pop(0)
        if nodo.upper() not in recorrido:
            recorrido.append(nodo.upper())
        if nodo.upper() not in grafo:
            continue
        for subnodo in grafo[nodo.upper()]:
            visitados.append(subnodo)
            
    for i in range(len(recorrido)):
        if i%2==0:
            un.append(recorrido[i])
        else:
            dos.append(recorrido[i])
            
    print(un)
    print(dos)
    recorrido=[]
    for i in range(len(un)):
        recorrido.append(un[i])
        recorrido.append(dos[i])
        

    print(recorrido)