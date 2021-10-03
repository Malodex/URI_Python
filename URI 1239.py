while True:
    try:
        texto=input()
        resultado=""
        negrito=False
        italico=False
        for letra in texto:
            if(letra=="_" and italico==False):
                resultado+="<i>"
                italico=True
            elif(letra=="_" and italico==True):
                resultado+="</i>"
                italico=False
            elif(letra!="_" and letra!="*"):
                resultado+=letra
            elif(letra=="*" and negrito==False):
                resultado+="<b>"
                negrito=True
            elif(letra=="*" and negrito==True):
                resultado+="</b>"
                negrito=False
        print(resultado)
    except EOFError:
        break
