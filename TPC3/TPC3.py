import re

def somar_digitos_arquivo(nome_arquivo):
    soma = 0
    sequencia_atual = ""

    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()

        # Remover todas as quebras de linha
        texto = texto.replace('\n', '')

        # Encontrar todas as correspondências dos padrões onde não devemos somar
        padroes_exclusao = re.findall(r'(OFF).*?(ON?|$)', texto, re.IGNORECASE)

        # Combinar os padrões de exclusão em uma única expressão regular
        padrao_exclusao_completo = '|'.join(re.escape(p[0]) + '.*?' + re.escape(p[1]) for p in padroes_exclusao)

        # Substituir os padrões de exclusão por uma string vazia
        texto_sem_exclusoes = re.sub(padrao_exclusao_completo, '', texto, flags=re.IGNORECASE)

        # Iterar sobre cada caractere no texto
        for char in texto_sem_exclusoes:
            if char.isdigit():
                sequencia_atual += char
            elif sequencia_atual:
                soma += int(sequencia_atual)
                sequencia_atual = ""

            # Exibir a soma atual sempre que encontrar o caracter '='
            if char == '=':
                print("Soma até o momento:", soma)

if __name__ == "__main__":
    nome_arquivo = 'TPC3/exemplo.txt'
    somar_digitos_arquivo(nome_arquivo)
