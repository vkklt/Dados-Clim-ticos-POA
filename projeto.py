dadosExternos = open("ArquivoDadosProjeto.csv", "r") # Abri o arquivo para leitura
linhas = dadosExternos.readlines() # Criei uma lista com todas as linhas do arquivo
linhas = [linha.strip() for linha in linhas] # Removi o "\n" de cada linha
cabecalho = linhas[0].split(';') # Separei o cabeçalho do arquivo
print (cabecalho) # Imprimi o cabeçalho

dados = [] # Criei uma lista para armazenar os dados

for linha in linhas[1:]: # Percorri o arquivo linha a linha
    valores = linha.split(";") # Separei os valores da linha no ";"
    data = valores[0].split("/") # Separei a data em dia, mês e ano
    tupla = (int(data[0]),int(data[1]),int(data[2]), float(valores[1]), float(valores[2]), float(valores[3]),float(valores[4]), float(valores[5]), float(valores[6]), float(valores[7])) # Criei uma tupla com os valores da linha
    valoresPositivos = [tupla[0]] + ["N/A" if valor < 0 else valor for valor in tupla[1:]] # Troquei todos os valores negativos por "N/A" em cada tupla
    dados.append(valoresPositivos) # Adicionei a tupla na lista de dados 
    print (valoresPositivos)

def Precipitacao (valoresPositivos):     
    while True: # Criei um loop para que o usuário possa digitar o mês e o ano que deseja obter informação, validando as informações digitadas
        try:
            while True:
                try:
                    mesPrecipitacao = int(input("Digite o número do mês no qual se deseja obter informação da precipitação: "))
                    if mesPrecipitacao > 12 or mesPrecipitacao < 1 : # Validei o mês
                        raise ValueError("Mês inválido :/ Por favor digite um número de 1 a 12")  # Mensagem de erro
                    break  
                except:
                    print("Mês inválido :/ Por favor digite um número de 1 a 12")  # Mensagem de erro

            while True:
                try:
                    anoPrecipitacao = int(input("Digite o número do ano no qual se deseja obter informação da precipitação: "))
                    if anoPrecipitacao < 1961 or anoPrecipitacao > 2016 : # Validei o ano
                        raise ValueError("Ano inválido :/ Por favor digite um número de 1 a 12")  # Mensagem de erro
                    break  
                except:
                    print("Ano inválido :/ Por favor digite um ano entre 1961 e 2016")
            if mesPrecipitacao > 7 and anoPrecipitacao == 2016: # Validei o mês e o ano (pois só possuem dados até o mês de julho de 2016)
                raise ValueError ("Somente possuem dados até o mês de julho de 2016 :/")  # Mensagem de erro
            break  
        except:
            print("Somente possuem dados até o mês de julho de 2016 :/")  # Mensagem de erro

    # !valores_precipitacao = []
    for item in dados: # Percorri a lista de dados
        if item[1] == mesPrecipitacao and item[2] == anoPrecipitacao: # Verifiquei na lista de dados o mês e ano digitados
            print("Dia: ",item[0],"Precipitação: ", item[9])
        # !valores_precipitacao.append(item[9])
        # !return print (valores_precipitacao)

    # as linhas comentadas iniciando em (!) acima foram usadas para testar a função apenas.

def Temperatura (valoresPositivos):
    
    while True: # Criei um loop para que o usuário possa digitar o mês e o ano que deseja obter informação, validando as informações digitadas
        try:
            anoTemperatura = int(input("Digite o número do ano no qual se deseja obter informação da temperatura: "))
            if anoTemperatura < 1961 or anoTemperatura > 2016 : # Validei o ano
                raise ValueError("Ano inválido ;-; Por favor digite um número de 1 a 12 ^-^ )")  # Mensagem de erro
            break  
        except:
            print("Ano inválido ;-; Por favor digite um número de 1 a 12 ^-^ )") # Mensagem de erro
    
    # duas listas para armazenar os valores de temperatura máxima dos 7 dias de cada mês
    max_temps = []    
    max_temp_mes = []

    for i in range(1, 13):  # Percorri os meses
        for item in dados:  # Percorri a lista de dados
            if item[2] == anoTemperatura and item[1] == i and item[0] <= 7:  # Verifiquei na lista de dados o mês e ano digitados
                print("Dia: ", item[0], "Mês: ", item[1], "Ano: ", item[2], "Máxima: ", item[4]) 
                max_temp_mes.append(item[4]) # Adicionei os valores de temperatura máxima dos 7 dias de cada mês na lista  
        if len(max_temp_mes) > 0: # Verifiquei se a lista está vazia    
            max_temps.append(max(max_temp_mes))  # Adicionei o valor máximo das temperaturas máximas dos 7 dias de cada mês em outra lista
            print("Temperatura máxima dos 7 dias: ", max(max_temp_mes))
            max_temp_mes.clear() # Limpei a lista para que os valores de temperatura máxima dos 7 dias de cada mês não sejam repetidos 
        else:
            print("Não há dados para os primeiros 7 dias do mês", i) # Mensagem de erro (principalmente para o ano de 2016, onde só há dados até o mês de julho)
                        
Precipitacao(valoresPositivos)
Temperatura(valoresPositivos)

dadosExternos.close() # Fechei o arquivo