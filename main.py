def LerTXT(txt):
    with open(txt, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def EscreverTXT(conteudo, nome):
    with open(nome, 'w') as arquivo:
        arquivo.write(conteudo)

def Compactar(arquivoEntrada, arquivoSaida):

    texto = LerTXT(arquivoEntrada) #Lê o arquivo de entrada e o armazena em uma variavel

    conteudoComprimido = "" 
    contador = 1 
    caractereAnterior = texto[0] 

    for i in range(1, len(texto)): 
        if texto[i] == caractereAnterior: 
            contador += 1

        else:  
            if contador <= 4:
                conteudoComprimido += caractereAnterior * contador

            else:
                conteudoComprimido += '#' + str(contador) + caractereAnterior + '|'

            contador = 1
            caractereAnterior = texto[i]
            
    if contador <= 4:
        conteudoComprimido += caractereAnterior * contador

    else:
        conteudoComprimido += '#' + str(contador) + caractereAnterior + '|'

    EscreverTXT(conteudoComprimido, arquivoSaida) #Cria o arquivo de saida e o preenche com o texto comprimido
    
def Descompactar(arquivoEntrada, arquivoSaida):

    texto = LerTXT(arquivoEntrada)

    conteudoDescomprimido = ""
    i = 0

    while i < len(texto):
        if texto[i] == '#':
            for j in range(i, len(texto)):
                if texto[j] == '|':
                    print(texto[j-2])
                    contador = int(texto[i+1:j-1])
                    caractere = texto[j-1]
                    conteudoDescomprimido += caractere * contador
                    i = j + 1
                    break
        else:
            conteudoDescomprimido += texto[i]
            i += 1

    EscreverTXT(conteudoDescomprimido, arquivoSaida)


#precisa ler um TXT CONFERE
# e devolver o TXT comprimido CONFERE
#  e descomprimido. CONFERE
# E COLOCAR UMA FLAG CONFERE
# nao compactar o que ja ta compactado

def Test():

    Compactar("teste1.txt", "_teste1.txt")
    Compactar("teste2.txt", "_teste2.txt")
    Compactar("teste3.txt", "_teste3.txt")
    Compactar("teste4.txt", "_teste4.txt")

    Descompactar("_teste1.txt", "#teste1.txt")
    Descompactar("_teste2.txt", "#teste2.txt")
    Descompactar("_teste3.txt", "#teste3.txt")
    Descompactar("_teste4.txt", "#teste4.txt")

Test()