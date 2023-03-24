import matplotlib.pyplot as plt

dadosExternos = open("ArquivoDadosProjeto.csv", "r") # Abri o arquivo para leitura
linhas = dadosExternos.readlines() # Criei uma lista com todas as linhas do arquivo
linhas = [linha.strip() for linha in linhas] # Removi o "\n" de cada linha
cabecalho = linhas[0].split(';') # Separei o cabeçalho do arquivo

dados = [] # Criei uma lista para armazenar os dados
dadosMes = {} # Criei o dicionário para armazenar os dados de precipitação de cada dia

for linha in linhas[1:]: # Percorri o arquivo linha a linha
    valores = linha.split(";") # Separei os valores da linha no ";"
    data = valores[0].split("/") # Separei a data em dia, mês e ano
    tupla = (int(data[0]),int(data[1]),int(data[2]), float(valores[1]), float(valores[2]), float(valores[3]),float(valores[4]), float(valores[5]), float(valores[6]), float(valores[7])) # Criei uma tupla com os valores da linha
    valoresPositivos = [tupla[0]] + [0.0 if valor < 0 else valor for valor in tupla[1:]] # Troquei todos os valores negativos por "N/A" em cada tupla
    dados.append(valoresPositivos) # Adicionei a tupla na lista de dados 
    chave = (data[2], data[1])
    valor = valoresPositivos[3]
    if chave in dadosMes: # Verifica se a chave já existe no dicionário e, caso existir, adiciona o valor na correspondente chave no dicionário
        dadosMes[chave][int(data[0])-1] += valor
    else: # Se a chave não existe, cria uma nova lista de valores para o mês e adiciona o valor para o respectivo dia 
        diasNoMes = (31, 28 if int(data[2]) % 4 != 0 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # acima eu defini o número de dias em cada mês, caso o ano for bissexto, onde ele valida vendo se o ano é divisivel por 4, o mês de fevereiro possui 1 dia a mais
        valoresMes = [0]*diasNoMes[int(data[1])-1]  
        # criei uma lista com zeros para os dias do mês, multiplicando pelo número de dias de cada mês o valor 0
        valoresMes[int(data[0])-1] = valor  # atribui o valor para o dia correspondente
        dadosMes[chave] = valoresMes  # adicionei a lista de valores para o mês ao dicionário

def mesMaisChuvoso (chave,valoresMes,dadosMes):

    maiorMedia = 0.0
    chaveMaiorMedia = []

    for chave, valoresMes in dadosMes.items():
        media = sum(valoresMes) / len(valoresMes) #calculei a média de cada mês afim de encontrar o mês com a maior média de chuva

        if media > maiorMedia:  # verifiquei qual é a maior média de chuva
            maiorMedia = media  # atualiza caso verdadeiro
            chaveMaiorMedia = chave  # atualiza a chave correspondente caso verdadeiro 

    print(f"A) O mês mais chuvoso em todo esse período foi o mês {chaveMaiorMedia[1]} no ano de {chaveMaiorMedia[0]} com a média de {maiorMedia} mm")

def mediaEmodaAgosto(dados):
    
    temperaturasAgosto = {}
    umidadeArAgosto = {}
    velocidadeVentoAgosto = {}
    mediasTemperaturasAgosto = {}
    mediasUmidadeArAgosto = {}
    mediasVelocidadeVentoAgosto = {}
    modasTemperaturasAgosto = {}
    modasUmidadeArAgosto = {}
    modasVelocidadeVentoAgosto = {}

    for linha in dados:
        if linha[1] == 8 and linha[2] >= 2006: #validei o mês de agosto nos últimos 10 anos

            ano = linha[2]
            temperaturaMinima = linha[5]
            umidadeAr = linha[8]
            velocidadeVento = linha[9]

            if ano not in temperaturasAgosto: # Verifiquei se o ano já existe no dicionário, e caso não exista, criei uma nova lista para armazenar as temperaturas mínimas de agosto
                temperaturasAgosto[ano] = []
            temperaturasAgosto[ano].append(temperaturaMinima) # Adicionei a temperatura mínima de agosto para o ano correspondente

            if ano not in umidadeArAgosto: # Verifiquei se o ano já existe no dicionário, e caso não exista, criei uma nova lista para armazenar a umidade do ar de agosto
                umidadeArAgosto[ano] = []
            umidadeArAgosto[ano].append(umidadeAr) # Adicionei a umidade do ar de agosto para o ano correspondente

            if ano not in velocidadeVentoAgosto: # Verifiquei se o ano já existe no dicionário, e caso não exista, criei uma nova lista para armazenar a velocidade do vento de agosto
                velocidadeVentoAgosto[ano] = []
            velocidadeVentoAgosto[ano].append(velocidadeVento) # Adicionei a velocidade do vento de agosto para o ano correspondente

    for ano, temperaturas in temperaturasAgosto.items(): # Calculei a média de cada lista de temperaturas mínimas de agosto
        mediaTemperaturaMinima = sum(temperaturas) / len(temperaturas)
        mediasTemperaturasAgosto[ano] = mediaTemperaturaMinima
    
    for ano, temperaturas in temperaturasAgosto.items(): # Calculei a moda de cada lista de temperaturas mínimas de agosto
        modaTemp = max(set(temperaturas), key=temperaturas.count)
        modasTemperaturasAgosto[ano] = modaTemp

    for ano, umidadeAr in umidadeArAgosto.items(): # Calculei a média de cada lista de umidade do ar de agosto
        mediaUmidadeAr = sum(umidadeAr) / len(umidadeAr)
        mediasUmidadeArAgosto[ano] = mediaUmidadeAr
    
    for ano, umidadeAr in umidadeArAgosto.items(): # Calculei a moda de cada lista de umidade do ar de agosto
        modaUmidade = max(set(umidadeAr), key=umidadeAr.count)
        modasUmidadeArAgosto[ano] = modaUmidade

    for ano, velocidadeVento in velocidadeVentoAgosto.items(): # Calculei a média de cada lista de velocidade do vento de agosto
        mediaVelocidadeVento = sum(velocidadeVento) / len(velocidadeVento)
        mediasVelocidadeVentoAgosto[ano] = mediaVelocidadeVento
    
    for ano, velocidadeVento in velocidadeVentoAgosto.items(): # Calculei a moda de cada lista de velocidade do vento de agosto
        modaVento = max(set(velocidadeVento), key=velocidadeVento.count)
        modasVelocidadeVentoAgosto[ano] = modaVento

        print("B) A média da temperatura mínima de agosto para o ano de", ano, "foi de:", mediasTemperaturasAgosto[ano], "e a moda foi:", modasTemperaturasAgosto[ano])
        print("B) A média da umidade do ar de agosto para o ano de", ano, "foi de:", mediasUmidadeArAgosto[ano], "e a moda foi:", modasUmidadeArAgosto[ano])
        print("B) A média da velocidade do vento de agosto para o ano de", ano, "foi de:", mediasVelocidadeVentoAgosto[ano], "e a moda foi:", modasVelocidadeVentoAgosto[ano])

def calcularVolumeDecada(dados):
    volumeAnual = {}
    for valoresPositivos in dados:
        ano = valoresPositivos[2]
        chuva = valoresPositivos[3]
        if ano in volumeAnual:
            volumeAnual[ano] += chuva 
            # se o ano já existir no dicionário, somei o valor da chuva com o valor já existente
        else:
            volumeAnual[ano] = chuva # se o ano não existir no dicionário, criei uma nova chave com o valor da chuva

    decadas = [(1961, 1970), (1971, 1980), (1981, 1990), (1991, 2000), (2001, 2010), (2011, 2016)] # Criei uma tupla com as décadas citadas no enunciado
  
    volumePorDecada = {}
    mediaDecada = {}  # Cria um novo dicionário para armazenar a média de chuvas por década
    medias = []

    for decada in decadas:
        soma = 0
        numAnos = decada[1] - decada[0] + 1
        for ano in range(decada[0], decada[1]+1): # Percorri a tupla decada
            if ano in volumeAnual:
                soma += volumeAnual[ano] # somei o volume de chuva de cada ano da década
        media = soma / numAnos # Calculei a média de chuvas por década
        anoInicial, anoFinal = decada # Desempacotei a tupla decada
        mediaDecada[f"{anoInicial}-{anoFinal}"] = media  # Adicionei a média da década ao novo dicionário
        medias.append(media)

    decadaMaisChuvosa = max(mediaDecada, key=mediaDecada.get) # calculei a década mais chuvosa
    print("C) A década mais chuvosa foi:" , decadaMaisChuvosa) 

    # Gráfico de barras usando matplotlib para mostrar a média de chuva por década
    decadaGrafico = ["1961-1970", "1971-1980", "1981-1990", "1991-2000", "2001-2010", "2011-2016"]
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=8)
    plt.title("D) Gráfico de médias por década") # título do gráfico
    plt.ylim(0, 1500) # limita o eixo y 
    plt.xlabel ("Década") # nomeia o eixo x
    plt.ylabel ("Média de chuva em mm") # nomeia o eixo y
    plt.bar (decadaGrafico,medias, color = "blue", width=0.6) # cria o gráfico de barras
    plt.show() # exibe o gráfico
    

mesMaisChuvoso(chave,valoresMes,dadosMes)
mediaEmodaAgosto(dados)
calcularVolumeDecada(dados)