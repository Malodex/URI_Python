qtd=int(input())
resposta=[]
for i in range(0,qtd):
    palavra=input()
    palavra1=""
    palavra2=""
    palavra3=""
    for letra in palavra:
        if(letra.isalpha()):
            palavra1+=chr(ord(letra)+3)
        else:
            palavra1+=letra
    palavra2=palavra1[::-1]
    tam=len(palavra2)
    indice=0
    for letra in palavra2:
        if(indice>=(len(palavra2)//2)):
            palavra3+=chr(ord(letra)-1)
        else:
            palavra3+=letra
        indice+=1
    resposta.append(palavra3)
for i in range(0,qtd):
    print(resposta[i])