def definir_dicionario():
    # Abra o arquivo CSV em modo de leitura
    with open('TPC1\emd.csv', 'r', encoding='utf-8') as arquivo:
        # Leia todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Dividindo os cabeçalhos
    cabecalho = linhas[0].strip().split(',')

    # Criando um dicionário para armazenar os dados
    dicionario = {}

    # Iterando sobre as linhas para extrair os dados
    for linha in linhas[1:]:
        valores = linha.strip().split(',')
        # Criando um dicionário para armazenar os dados de cada linha relacionando com o cabeçalho
        dicionario_linha = {}
        for i, valor in enumerate(valores):
            dicionario_linha[cabecalho[i]] = valor
        # Usando o _id como chave para cada dicionário e armazenando-os no dicionário de dados
        dicionario[dicionario_linha['_id']] = dicionario_linha

    # Retornando o dicionário de dados
    return dicionario

#LISTA ORDENADA ALFABETICAMENTE DAS MODALIDADES
def ex1(dicionario):
    modalidades = set()
    for linha in dicionario.values():
        modalidades.add(linha['modalidade'])
    modalidades_ordenadas = sorted(list(modalidades))
    print("EXERCÍCIO 1:")
    print(modalidades_ordenadas)


#PERCENTAGENS DE ATLETAS APTOS E INAPTOS PARA A PRÁTICA DESPORTIVA
def ex2(dicionario):
    aptos = 0
    inaptos = 0
    for linha in dicionario.values():
        if (linha['resultado'] == 'true'):
            aptos += 1
        else:
            inaptos += 1
    percentagem_aptos = aptos/len(dicionario) *100
    percentagem_inaptos = inaptos/len(dicionario) *100
    print("EXERCÍCIO 2:")
    print("Aptos: " + str(percentagem_aptos) + "%; Inaptos: " + str(percentagem_inaptos) + "%")

#DISTRIBUIÇÃO DE ATLETAS POR ESCALÃO ETÁRIO (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
def ex3(dicionario):
    atletas_por_escalao = {}

    for linha in dicionario.values():
        idade = int(linha['idade'])
        escalao = (idade // 5) * 5

        if escalao in atletas_por_escalao:
            atletas_por_escalao[escalao].append(linha)
        else:
            atletas_por_escalao[escalao] = [linha]


    print("Atletas por escalão etário:")
    for escalao, atletas in sorted(atletas_por_escalao.items()):
        limite_inferior = escalao
        limite_superior = escalao + 4
        print(f"[{limite_inferior}-{limite_superior}]:")
        for atleta in atletas:
            print(f"  {atleta['nome/primeiro']} {atleta['nome/último']} - {atleta['idade']} anos")



if __name__ == "__main__":
    dicionario = definir_dicionario()
    ex1(dicionario)
    ex2(dicionario)
    ex3(dicionario)
