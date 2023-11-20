import csv

def gerar_flashcards(arquivo_entrada, arquivo_saida, num_flashcards):
    # Lê o arquivo de texto
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        linhas = [linha.strip() for linha in file if linha.strip()]

    # Gera perguntas e respostas
    flashcards = []
    for i in range(0, min(num_flashcards * 2, len(linhas)), 2):
        if i + 1 < len(linhas):
            pergunta = f"O que diz o texto: '{linhas[i]}'?"
            resposta = linhas[i + 1]
            flashcards.append((pergunta, resposta))

    # Escreve os flashcards em um arquivo CSV
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for pergunta, resposta in flashcards:
            writer.writerow([pergunta, resposta])

# Configurações
arquivo_entrada = 'Lei_8112_Serv_Publicos.txt'
arquivo_saida = 'Lei_8112_Serv_Publicos.csv'
num_flashcards = 75

# Executando a função
gerar_flashcards(arquivo_entrada, arquivo_saida, num_flashcards)
