from recursos.funcoes import limparTela, aguarde

while True:
    limparTela()
    print("(o)Sair") 
    print("(1) Cadastro")
    print("(2)Lista ")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        print("Cadastro de Pessoas:")
        nome = input("Nome:")
        listaPessoas.append(nome)
        arquivo = open("bd.atitus","w" encondig="utf-8") #w r a
        for pessoa in listaPessoas:
            arquivo.write(pessoas+"\n")
        arquivo.close()
        
        print("Dados Salvos com Sucesso!")
        aguarde(3)
    elif opcao == "2":
        print("Lista de Pessoas Cadastradas!")
        try:
        arquivo = open("bd.atitus", "r")
        dados = arquivo.read()
        arquivo.close()
        print(dados)
    except:
    print("Arquivo de dados não encontrados!")
        
    else:
        print("Opção Inválida!")
        aguarde(3)