def RLE(texto): #Cria a função "Run Length Encoding"

    stringComprimida = "" #Cria o texto que será devolvido como texto comprimido, e o inicializa como vazio
    contador = 1 #Cria a variavel que vai armazenar quantas vezes o caractere se repete, e a inicializa como 1
    caractereAnterior = texto[0] #Cria a variavel que vai armazenar o caractere anterior, e a inicializa como o primeiro caractere do texto

    for i in range(1, len(texto)): #Cria um loop que vai percorrer o texto, começando do primeiro caractere
        if texto[i] == caractereAnterior: #Se o caracterer atual for igual ao anterior, o contador é incrementado
            contador += 1
        
        else:  #Senão, é adicionado ao texto "Valor,Letra" tipo 3W, e o contador é reiniciado para 1
            stringComprimida += str(contador) + caractereAnterior
            contador = 1
            caractereAnterior = texto[i]

    stringComprimida += str(contador) + caractereAnterior #Adiciona o ultimo caractere ao texto comprimido

    return stringComprimida #Retorna o texto comprimido

#precisa ler um TXT e devolver o TXT comprimido e descomprimido. E COLOCAR UMA FLAG

def lerTXT(txt):
    with open(txt, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def exemplo(texto):

    caractereAnterior = texto[0]
    contador = 1
    textoComprimido = ""

    for i in range(0, len(texto)):

        if texto[i] == caractereAnterior:
            contador += 1

        else:
            textoComprimido += str(contador) + caractereAnterior
            contador = 1
            caractereAnterior = texto[i]

    textoComprimido += str(contador) + caractereAnterior

    return textoComprimido

'''def ANTIRLE(texto):
    
    stringDescomprimida = ""
    contador = 1
    caractereAnterior = texto[0]

    for i in range(1, len(texto)):
        if texto[i].isdigit():
            contador = int(texto[i])
        else:
            stringDescomprimida += caractereAnterior * contador
            caractereAnterior = texto[i]'''

print(RLE(lerTXT("teste.txt")))