d=1
n=1
soma=0
resposta=[]
while(True):
    res=""
    d,n=list(map(int,input().split()))
    if(d==0 and n==0):
        break
    d=str(d)
    n=str(n)
    for letra in n:
        if(letra==d):
            soma+=1
            continue
        elif(letra!=d):
            res+=letra
    if(soma==len(n)):
        res+="0"
    res=int(res)
    resposta.append(res)
    soma=0
for i in range(0,len(resposta)):
    print(resposta[i])