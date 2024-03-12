import sys
import re

# Definindo os tipos de token
patterns = [
    ('PALAVRA_CHAVE', r'(SELECT|FROM|WHERE)'),
    ('IDENTIFICADOR', r'[a-zA-Z_]+\.{0,1}[a-zA-Z0-9_]*|\*'),
    ('OPERADOR', r'(>=|<=|=|<|>)'),
    ('LITERAL_NUMERICO', r'\d+'),
    ('LITERAL_TEXTO', r"'[^']*'"),
    ('PONTUACAO', r'[,;()]')
]


def tokenize(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                code = code[match.end():].strip()
                break
        if not match:
            raise SyntaxError('Token inválido: %s' % code)
    return tokens

# Função para ler a entrada do usuário e exibir os tokens correspondentes
def main():
    while True:
        try:
            print("Introduza a query (ou exit para sair do programa):")
            code = sys.stdin.readline().strip()
            if code.lower() == 'exit':
                break
            tokens = tokenize(code)
            print("Tokens:")
            for token in tokens:
                print(token)
            print()
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    main()
