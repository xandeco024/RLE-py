def TransformarTXTParaString(arquivo):
    arquivo = open(arquivo, 'r')
    texto = arquivo.read()
    arquivo.close()
    return texto

def TransformarStringParaTXT(conteudo, nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    arquivo.write(conteudo)
    arquivo.close()

def Compactar(conteudo):
    conteudoComprimido = ""
    contador = 1 
    caractereAnterior = conteudo[0] 

    for i in range(1, len(conteudo)): 
        if conteudo[i] == caractereAnterior: 
            contador += 1

        else:  
            if contador <= 4:
                conteudoComprimido += caractereAnterior * contador

            else:
                conteudoComprimido += '#' + str(contador) + caractereAnterior + '|'

            contador = 1
            caractereAnterior = conteudo[i]

    if contador <= 4:
        conteudoComprimido += caractereAnterior * contador

    else:
        conteudoComprimido += '#' + str(contador) + caractereAnterior + '|'

    return conteudoComprimido

def Main():

    rodando = True
    while rodando:
        print("-=-=-=-=-=-=- SUPER DES/COM/PACTADOR 300 -=-=-=-=-=-=-")
        print("")
        print("Olá! Bem vindo ao compactador / descompactador de arquivos de texto!")
        print("")
        print("Selecione uma opção:")
        print("1 - Compactar")
        print("2 - Descompactar")
        print("3 - Sair")
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        opcao = input("Digite a opção desejada: ")
        while opcao != "1" and opcao != "2" and opcao != "3":
            print("Opção inválida! Tente novamente.")
            opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            arquivoEntrada = input("Digite o nome do arquivo de entrada: ")
            arquivoSaida = input("Digite o nome do arquivo de saída: ")
            texto = TransformarTXTParaString(arquivoEntrada)
            conteudoComprimido = Compactar(texto)
            TransformarStringParaTXT(conteudoComprimido, arquivoSaida)
            print("Arquivo compactado com sucesso!")
            print("")
        
        elif opcao == "2":
            pass

        elif opcao == "3":
            rodando = False
            print("Até mais!")

Main()