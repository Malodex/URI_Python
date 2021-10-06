quantiade=int(input())
for i in range(0,quantiade):
    soma=0
    lista=[]
    numero=int(input())
    for j in range(1,numero):
        if(numero%j==0):
            lista.append(j)
    for j in range(0,len(lista)):
        soma+=lista[j]
    if(soma==numero):
        print("{} eh perfeito".format(numero))
    else:
        print("{} nao eh perfeito".format(numero))
