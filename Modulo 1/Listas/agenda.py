import os 
    
def limpa_tela():
        os.system("cls")


def adiciona_nome(lista_nomes, nome):
    lista_nomes.append(nome) #Adiciona nome na lista_nomes.
    
def remover_nome(lista_nomes, nome):
     lista_nomes.remove(nome) #Remove nome na lista_nomes.

def mostrar_nomes(lista_nomes):
    for nome in lista_nomes: #["Joao", "Maria","Ana"]
        print(nome)
limpa_tela()
nomes = [] 

while True: 
 limpa_tela()
 menu =input("Escolha sua opcao:\n[1] - Listae nomes\n[2] - Adicionar nomes\n[3] -  Remover nomes\n[0] - Sair\nSua opcao:")
 if menu == "0":
     break
 elif menu == "1": 
  mostrar_nomes(nomes) 
  input("Aperte enter para continuar")                                                                                                                                                  
 elif menu == "2": 
  nome_salvar = input("Digite o nome que deseja adicionar: ")
  adiciona_nome(nomes, nome_salvar)
 elif menu == "3":
     nome_remover = input("Digite o nome que deseja remover: ")
     remover_nome(nomes, nome_remover)
 else:
     print("Opcao invalida.")
     input(" Aperte enter para continuar")

     

  




   