prox=0
vint=0
vgre=0
total=0
empate=0
while(prox!=2):
    inter,gremio=list(map(int,input().split()))
    if(inter>gremio):
        vint+=1
    elif(gremio>inter):
        vgre+=1
    else:
        empate+=1
    total+=1
    prox=int(input())

for i in range(0,total):
    print("Novo grenal (1-sim 2-nao)")
print("{} grenais".format(total))
print("Inter:{}".format(vint))
print("Gremio:{}".format(vgre))
print("Empates:{}".format(empate))
if(vint>vgre):
    print("Inter venceu mais")
elif(vgre>vint):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")