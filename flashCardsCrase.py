import pandas as pd
# Dados de flashcards sobre o tema "Crase"
dados_crase = [
    ["Quando se usa o sinal de crase antes de nomes femininos?", "Usa-se a crase antes de palavras femininas quando há a fusão da preposição 'a' com o artigo definido 'a' ou 'as'."],
    ["A crase é utilizada antes de palavras masculinas?", "Não, a crase não é utilizada antes de palavras masculinas."],
    ["A crase é aplicada antes de pronomes possessivos femininos?", "Sim, usa-se a crase antes de pronomes possessivos femininos quando há a preposição 'a' e o artigo definido 'a' ou 'as'."],
    ["Como fica a crase antes de nomes de cidades femininos conhecidos?", "Usa-se a crase se a cidade for feminina e aceitar o artigo 'a', como 'à Bahia'."],
    ["É correto usar crase antes de verbos?", "Não, não se usa crase antes de verbos."],
    ["A crase deve ser usada antes da palavra 'casa' quando esta está especificada?", "Sim, usa-se a crase se a palavra 'casa' estiver especificada, como em 'à minha casa'."],
    ["Como a crase é utilizada em locuções prepositivas femininas?", "Usa-se a crase em locuções prepositivas femininas, como 'à medida que', 'à frente de'."],
    ["A crase é utilizada antes de nomes de pessoas femininos?", "Usa-se a crase antes de nomes de pessoas femininos quando houver a preposição 'a' e o artigo 'a', como em 'à Maria'."],
    ["Quando não se usa a crase antes da palavra 'terra', referindo-se ao solo firme?", "Não se usa a crase quando a palavra 'terra' é usada em oposição a 'bordo', como em 'voltar a terra'."],
    ["É correto usar crase antes de pronomes de tratamento que iniciam com 'senhora' ou 'senhorita'?", "Sim, é correto usar crase nesses casos, como em 'à senhora' ou 'à senhorita'."]
]

# Criar DataFrame com os dados
df_crase = pd.DataFrame(dados_crase, columns=["Pergunta", "Resposta"])

# Caminho do arquivo CSV
caminho_csv_crase = "/home/otluix/Workspace/Português/flashCards/Flashcards_Crase.csv"

# Salvar como CSV
df_crase.to_csv(caminho_csv_crase, sep='\t', index=False, encoding='utf-8')

caminho_csv_crase

