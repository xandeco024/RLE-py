def TransformarTXTParaString(arquivo): #Função que transforma o conteudo de um arquivo de texto em uma string.
    arquivo = open(arquivo, 'r') #Abre o arquivo em modo de leitura. (R de READ)
    texto = arquivo.read()  #Lê o conteudo do arquivo e armazena na variavel texto.
    arquivo.close() #Fecha o arquivo, pois não é mais necessário.
    return texto #Retorna o texto, para que possa ser manipulado.

def TransformarStringParaTXT(conteudo, nomeArquivo): #Função que transforma uma string em um arquivo de texto.
    arquivo = open(nomeArquivo, 'w') #Abre o arquivo em modo de escrita. (W de WRITE). caso o arquivo não exista, ele será criado.
    arquivo.write(conteudo) #Escreve o conteudo no arquivo.
    arquivo.close() #Fecha o arquivo, pois não é mais necessário.

def Compactar(conteudo):

    if len(conteudo) == 0: #Se o texto estiver vazio, não é necessário comprimir, então retorna o texto original.
        # lembrando que -> len(variavel) retorna o tamanho da variavel, ou seja, a quantidade de caracteres que ela possui.
        return conteudo

    conteudoComprimido = "" #Variavel que armazenará o texto comprimido, iniciado vazio, pois ainda não foi comprimido.

    repeticoes = 1 #Variavel que armazenará a quantidade de vezes que um caractere se repete, iniciado em 1 pois cada caracter se repete ao menos uma vez.
    
    caractereAnterior = conteudo[0] #Variavel que armazenará o caractere anterior ao atual, iniciado com o primeiro caractere do texto. 
                                    #digamos que o texto = "BANANA", texto[0] = B, texto[1] = A e por ai vai...

    #Aqui é onde começa o algoritmo de compressão, ele funciona da seguinte maneira
    # o arquivo "AAAAA" será comprimido para "#05A"
    # o arquivo "AAAAAAAAAA" será comprimido para "#10A"
    # 100 vezes a letra A será comprimida para "#99AA" ou seja, o algoritmo só aceita 2 digitos para a quantidade de repetições.
    # o arquivo "AAAA" não será comprimido.
    # o arquivo "AA" não também não será comprimido pois neste caso e no acima seria burrice. AA -> #02A 2 caracteres seriam transformados em 4.
    # Para que haja a compressão, é necessario que o caractere se repita mais de 4 vezes.
    # o arquivo "ABABABABAB" será comprimido para "ABABABABAB" esté é o caso em que o algoritmo tem pior performance.

    for caractereIndice in range(1, len(conteudo)): #Percorre o texto a partir do segundo caractere até o ultimo (len(conteudo)), pois o primeiro já foi armazenado na variavel caractereAnterior
        if conteudo[caractereIndice] == caractereAnterior:
            repeticoes += 1 #Se o caractere atual for igual ao anterior, incrementa o contador

            if repeticoes == 99: #PULE PARA A LINHA 43, E DEPOIS VOLTE PRA CÁ 
                #Se o contador chegar a 99, então é necessário comprimir, pois o contador só aceita 2 digitos.
                conteudoComprimido += "#" + str(repeticoes) + caractereAnterior #Adiciona a flag de compressão, a quantidade de repetições e o caractere.
                repeticoes = 0 #Reseta o contador para 0

        else:  #Se o caractere atual for diferente do anterior, então é hora de comprimir!
            if repeticoes <= 4: #Se o contador for menor ou igual a 4, não é necessário comprimir.
                conteudoComprimido += caractereAnterior * repeticoes #adiciona o caractere anterior a quantidade de vezes que ele se repete.

            else: #Se o contador for maior que 4, então é necessário comprimir, então adiciona uma flag para indicar a compressão
                if repeticoes <= 9: #Se o contador for menor ou igual a 9, adiciona um 0 a esquerda para manter o padrão de 2 digitos.
                    conteudoComprimido += "#0" + str(repeticoes) + caractereAnterior #AAAA -> #04A
                else: #Se o contador for maior que 9, então não é necessário adicionar o 0 a esquerda.
                    conteudoComprimido += "#" + str(repeticoes) + caractereAnterior #AAAAAAAAAA -> #10A

            repeticoes = 1 #Reseta o contador para 1, pois o caractere atual é diferente do anterior.
            caractereAnterior = conteudo[caractereIndice] #Atualiza o caractere anterior para o caractere atual. 

    if repeticoes <= 4: #Aqui, a mesma logica se repete, mas desta vez, para lidar com o ultimo caractere do texto.
        conteudoComprimido += caractereAnterior * repeticoes
    else:
        if repeticoes <= 9:
            conteudoComprimido += "#0" + str(repeticoes) + caractereAnterior
        else:
            conteudoComprimido += "#" + str(repeticoes) + caractereAnterior

    return conteudoComprimido #Finalmente, retorna o texto comprimido, para que possa ser inserido em um arquivo :)

def RemoverEspacoVazio(conteudo):
    conteudoComprimido = ""
    repeticoes = 1

    caractereAnterior = conteudo[0]

    for caractereIndice in range(1, len(conteudo)):
        if conteudo[caractereIndice] == " ": #Se o caractere atual for igual a um espaço, então é necessário comprimir.
            repeticoes += 1

        else:
            if repeticoes <= 4:
                conteudoComprimido += caractereAnterior * repeticoes

            else:
                if repeticoes <= 9:
                    conteudoComprimido += "#0" + str(repeticoes) + caractereAnterior
                else:
                    conteudoComprimido += "#" + str(repeticoes) + caractereAnterior

            repeticoes = 1
            caractereAnterior = conteudo[caractereIndice]

    if repeticoes <= 4:
        conteudoComprimido += caractereAnterior * repeticoes
    else:
        if repeticoes <= 9:
            conteudoComprimido += "#0" + str(repeticoes) + caractereAnterior
        else:
            conteudoComprimido += "#" + str(repeticoes) + caractereAnterior

    return conteudoComprimido

def Descompactar(conteudo): 
    if len(conteudo) == 0: #Se o texto estiver vazio, não é necessário descomprimir, então retorna o texto original.
        return conteudo

    conteudoDescomprimido = "" #Variavel que armazenará o texto descomprimido, iniciado vazio, pois ainda não foi descomprimido.

    caractereAtual = 0 #Variavel que armazenará a posição do caractere atual, iniciado em 0 pois o primeiro caractere é o 0.
    repeticoes = 0 #Variavel que armazenará a quantidade de vezes que um caractere se repete, iniciado em 0 pois ainda não foi definido.

    while caractereAtual < len(conteudo): #Percorre o texto até o ultimo caractere.
        if conteudo[caractereAtual] == "#": #Se o caractere atual for igual a flag de compressão, então é necessário descomprimir.

            #Aqui, o algoritmo vai pegar a quantidade de repetições, que está entre o caractere atual + 1 e o caractere atual + 3. e vai tarnsformar em um inteiro (int()), pois atualmente é uma string
            #EXEMPLO: #05A (caractere atual = #, caractere atual + 1 = 0, caractere atual + 2 = 5, caractere atual + 3 = A)
            #O que está entre o caractere atual + 1 e o caractere atual + 3 é -> 05, que é a quantidade de repetições. ALELUIA!
            repeticoes = int(conteudo[caractereAtual + 1:caractereAtual + 3])
            caractere = conteudo[caractereAtual + 3] #O caractere que será repetido é o caractere atual + 3, pois é o que vem depois da quantidade de repetições.
            conteudoDescomprimido += caractere * repeticoes #Adiciona o caractere a quantidade de vezes que ele se repete.
            caractereAtual += 4 #Atualiza o caractere atual para o proximo caractere, pulando a flag de compressão e a quantidade de repetições.
            #EXEMPLO: #05AB -> caractereAtual += 4 -> B, pois pulou a flag de compressão, a quantidade de repetições e o caractere, ai é só seguir a descompressão.

        else: #Se o caractere atual não for a flag de compressão, então não é necessário descomprimir.
            conteudoDescomprimido += conteudo[caractereAtual] #Adiciona o caractere atual ao texto descomprimido.
            caractereAtual += 1 #Atualiza o caractere atual para o proximo caractere.

    return conteudoDescomprimido #Finalmente, retorna o texto descomprimido, para que possa ser inserido em um arquivo :)

def Testar(conteudoOriginal, conteudoFinal): #besteira minha, ignorar :)
    if conteudoOriginal == conteudoFinal:
        return True
    else :
        return False