import re

def markdown_to_html(markdown):
    linhas_html = []

    for linha in markdown:
        # Cabeçalhos
        if re.match(r'^(#{1,6})\s+(.*?)\s*$', linha):
            match = re.match(r'^(#{1,6})\s+(.*?)\s*$', linha)
            nivel = len(match.group(1))
            linhas_html.append(f'<h{nivel}>{match.group(2)}</h{nivel}>')

        # Negrito
        elif re.match(r'\*\*(.*?)\*\*', linha):
            linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)
            linhas_html.append(linha)

        # Itálico
        elif re.match(r'\*(.*?)\*', linha):
            linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)
            linhas_html.append(linha)

        # Listas numeradas
        elif re.match(r'^(\d+\.\s+)(.*?)$', linha):
            linhas_html.append(f'<ol>')
            for linha in markdown:
                  if re.match(r'^(\d+\.\s+)(.*?)$', linha):
                        match = re.match(r'^(\d+\.\s+)(.*?)$', linha)
                        linhas_html.append(f'<li>{match.group(2)}</li>')
            linhas_html.append(f'</ol>')

        # Listas não numeradas
        elif re.match(r'^([\+|\*|\-])\s+(.*?)$', linha):
            linhas_html.append(f'<ul>')
            match = re.match(r'^([\+|\*|\-])\s+(.*?)$', linha)
            linhas_html.append(f'<li>{match.group(2)}</li>')
            linhas_html.append(f'</ul>')

        # Links
        elif re.match(r'\[([^\]]+)\]\(([^)]+)\)', linha):
            linha = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', linha)
            linhas_html.append(linha)

        # Imagens
        elif re.match(r'!\[([^\]]+)\]\(([^)]+)\)', linha):
            linha = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', linha)
            linhas_html.append(linha)

        # Outras linhas de texto
        else:
            linhas_html.append(f'<p>{linha.strip()}</p>')

    return '\n'.join(linhas_html)

if __name__ == "__main__":
	with open('TPC2/exemplo.md', 'r') as file_md:
		text_md = file_md.readlines()

	text_html = markdown_to_html(text_md)

	with open('TPC2/exemplo.html', 'w') as file_html:
		file_html.write(text_html)
