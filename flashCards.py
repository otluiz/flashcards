# Dados dos flashcards para os tópicos de Língua Portuguesa
dados_lingua_portuguesa = [
    ["O que é compreensão e interpretação de textos?", "É a capacidade de entender e explicar o significado de um texto, considerando suas ideias principais e detalhes."],
    ["O que é tipologia textual?", "Refere-se aos diferentes tipos de textos, como narrativo, descritivo, expositivo, argumentativo e injuntivo."],
    ["Quais são as regras da ortografia oficial?", "Incluem as normas do Acordo Ortográfico da Língua Portuguesa sobre a escrita correta das palavras."],
    ["Como funciona a acentuação gráfica na língua portuguesa?", "Baseia-se em regras específicas para indicar a sílaba tônica das palavras e facilitar a pronúncia correta."],
    ["Qual é a importância do emprego das classes de palavras?", "Cada classe (substantivo, adjetivo, verbo, etc.) tem uma função específica na formação das frases, contribuindo para a clareza e precisão do texto."],
    ["Quando se usa o sinal indicativo de crase?", "Utiliza-se antes de palavras femininas e indica a fusão da preposição 'a' com o artigo 'a' ou 'as', ou com o 'a' inicial dos pronomes aquele(s), aquela(s) e aquilo."],
    ["O que é a sintaxe da oração e do período?", "É o estudo da estrutura e formação das orações (frases simples) e períodos (frases compostas), analisando a disposição das palavras e a relação entre elas."],
    ["Como é utilizada a pontuação na língua portuguesa?", "Emprega sinais gráficos (vírgula, ponto, ponto e vírgula, etc.) para organizar o texto, delimitar frases ou orações e indicar diferentes entonações e pausas."],
    ["O que é concordância nominal e verbal?", "É a adequação de gênero e número entre nomes e adjetivos (concordância nominal) e a correlação entre o verbo e seu sujeito em número e pessoa (concordância verbal)."],
    ["Como funciona a regência nominal e verbal?", "Refere-se à relação de subordinação entre um nome ou verbo (regente) e seus complementos, definindo o uso correto das preposições."]
]

# Criar DataFrame com os dados
df_lingua_portuguesa = pd.DataFrame(dados_lingua_portuguesa, columns=["Pergunta", "Resposta"])

# Caminho do arquivo CSV
caminho_csv_lingua_portuguesa = "/mnt/data/Flashcards_Lingua_Portuguesa.csv"

# Salvar como CSV
df_lingua_portuguesa.to_csv(caminho_csv_lingua_portuguesa, sep='\t', index=False, encoding='utf-8')

caminho_csv_lingua_portuguesa

