from algoritmos import *
import os

rodando = True
while rodando:
    os.system("cls" if os.name == "nt" else "clear")

    print("-=-=-=-=-=-=- SUPER DES/COM/PACTADOR 3000 -=-=-=-=-=-=-")
    print("")
    print("Olá! Bem vindo ao compactador / descompactador de arquivos de texto!")
    print("")
    print("Selecione uma opção:")
    print("1 - Compactar")
    print("2 - Descompactar")
    print("3 - Testar")
    print("4 - Créditos")
    print("5 - Sair")
    print("")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    opcao = input("Digite a opção desejada: ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        print("Opção inválida! Tente novamente.")
        opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")

        print("-=-=-=-=-=-=- COMPACTADOR -=-=-=-=-=-=-")
        print("")
        print("Para compactar varios arquivos de uma vez, digite o nome dos arquivos separados por espaço.")
        arquivosEntrada = input("Digite o nome dos arquivos de entrada: ")
        
        arquivosEntrada = arquivosEntrada.split(" ")
        for arquivo in arquivosEntrada:
            extensao = arquivo.split(".")
            arquivoSaida = extensao[0] + "_compactado" + "." + extensao[1]
            texto = TransformarTXTParaString(arquivo)
            conteudoComprimido = Compactar(texto)
            TransformarStringParaTXT(conteudoComprimido, arquivoSaida)
        print("")
        print("Arquivos compactados com sucesso!")
        print("")
        input("Pressione qualquer tecla para voltar ao menu principal...")

    elif opcao == "2":
        os.system("cls" if os.name == "nt" else "clear")

        print("-=-=-=-=-=-=- DESCOMPACTADOR -=-=-=-=-=-=-")
        print("")
        print("Para descompactar varios arquivos de uma vez, digite o nome dos arquivos separados por espaço.")
        arquivosEntrada = input("Digite o nome dos arquivos de entrada: ")
        
        arquivosEntrada = arquivosEntrada.split(" ")
        for arquivo in arquivosEntrada:
            extensao = arquivo.split(".")
            arquivoSaida = extensao[0] + "_descompactado" + "." + extensao[1]
            texto = TransformarTXTParaString(arquivo)
            conteudoDescomprimido = Descompactar(texto)
            TransformarStringParaTXT(conteudoDescomprimido, arquivoSaida)
        print("")
        print("Arquivos descompactados com sucesso!")
        print("")
        input("Pressione qualquer tecla para voltar ao menu principal...")


    elif opcao == "3":
        os.system("cls" if os.name == "nt" else "clear")

        print("-=-=-=-=-=-=- TESTADOR -=-=-=-=-=-=-")
        print("")
        arquivoEntrada = TransformarTXTParaString(input("Digite o nome do arquivo de entrada: "))
        arquivoSaida = TransformarTXTParaString(input("Digite o nome do arquivo de saída: "))
        print("Testando...")
        if Testar(arquivoEntrada, arquivoSaida):
            print("Compactação e descompactação bem sucedidas!")
        else:
            print("Falhou :c")
        print("")
        input("Pressione qualquer tecla para voltar ao menu principal...")

    elif opcao == "4":
        os.system("cls" if os.name == "nt" else "clear")

        print("-=-=-=-=-=-=- CRÉDITOS -=-=-=-=-=-=-")
        print("")
        print("Desenvolvido por:")
        print("Gabriel Alexander Pinheiro Bravo")
        print("https//github.com/xandeco024")
        print("")
        print("Te desejo um ótimo dia!")
        print("")
        input("Pressione qualquer tecla para voltar ao menu principal...")

    elif opcao == "5":
        rodando = False
        print("Até mais!")