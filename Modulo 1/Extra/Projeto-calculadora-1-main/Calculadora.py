#Funçoes das operaçoes basicas.
def somar (n1,n2):
    return n1 + n2 

def subtrair(n1,n2):
    return n1-n2 

def multiplicar (n1,n2):
    return n1 * n2 

#Boa pratica (evitar erro.)
def dividir(n1,n2):
    return n1 / n2

def calcular(n1,n2,operaçao): 
    if operaçao == "+":
     return somar(n1,n2)
    
    elif operaçao =="-":
        return subtrair(n1,n2)
    
    elif operaçao == "*":
        return multiplicar(n1,n2)
    
    elif operaçao =="/":
        return dividir(n1,n2)
    else:
        return "Operaçao invalida."
