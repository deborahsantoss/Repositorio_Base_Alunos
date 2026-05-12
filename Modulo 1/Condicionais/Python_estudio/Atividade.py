numero = int(input("Digite o numero da tabuada: "))  
numero_inicial = int(input("Digite da onde a tabuada começa: "))
numero_final = int(input("Digite ate qual numero vai: "))

for i in range(numero_inicial,numero_final+1):
    print(i)
    print(f" {i} x {numero} = {i * numero}")
    
