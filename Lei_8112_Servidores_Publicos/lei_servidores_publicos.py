import pandas as pd

# Dados das perguntas e respostas sobre a Lei nº 8.112 (Lei dos Servidores Públicos)
dados_lei_8112 = [
    ["O que regula a Lei nº 8.112?", "Regula o regime jurídico dos servidores públicos civis da União, das autarquias e das fundações públicas federais."],
    ["Qual o regime de trabalho dos servidores da Lei nº 8.112?", "Regime estatutário."],
    ["Quais são as formas de provimento de cargo público segundo a Lei nº 8.112?", "Nomeação, promoção, readaptação, reversão, aproveitamento, reintegração e recondução."],
    ["O que é a estabilidade no serviço público conforme a Lei nº 8.112?", "É adquirida após 3 anos de efetivo exercício, por servidor nomeado por concurso público."],
    ["Como pode ser feita a vacância de cargo público segundo a Lei nº 8.112?", "Por exoneração, demissão, promoção, readaptação, aposentadoria, posse em outro cargo inacumulável e falecimento."],
    ["Qual é o prazo para o servidor empossado em cargo público entrar em exercício?", "15 dias contados da posse."],
    ["O que é remoção e como é tratada na Lei nº 8.112?", "É a transferência do servidor, a pedido ou de ofício, no âmbito do mesmo quadro, com ou sem mudança de sede."],
    ["Como a Lei nº 8.112 aborda a questão de horas extras?", "Serviço extraordinário será remunerado com acréscimo de 50% em relação à hora normal de trabalho."],
    ["Quais são os tipos de licença previstos na Lei nº 8.112?", "Licença por motivo de doença em família, por motivo de afastamento do cônjuge, para o serviço militar, para atividade política, para capacitação, para tratar de interesses particulares e para desempenho de mandato classista."],
    ["O que a Lei nº 8.112 estabelece sobre aposentadoria?", "Estabelece diferentes regras de aposentadoria, incluindo por invalidez, compulsória e voluntária."],
    ["Qual é a jornada de trabalho no serviço público federal, conforme a Lei nº 8.112?", "40 horas semanais, salvo disposição legal em contrário."],
    ["Qual o prazo para o servidor estável requerer a sua recondução?", "30 dias a partir da publicação do ato que reintegrar ou aproveitar o anterior ocupante do cargo."],
    ["Como é a questão da acumulação de cargos públicos na Lei nº 8.112?", "É proibida a acumulação remunerada de cargos públicos, exceto em casos específicos previstos na Constituição."],
    ["Como a Lei nº 8.112 trata o direito de petição?", "Assegura o direito de requerimento aos servidores, observados os prazos para defesa e recurso administrativo."],
    ["Qual é o período de estágio probatório segundo a Lei nº 8.112?", "24 meses a partir da posse do servidor."],
    ["Quais são as penalidades disciplinares previstas na Lei nº 8.112?", "Advertência, suspensão, demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão."],
    ["O que é o Rendimento Global na Lei nº 8.112?", "É o somatório dos vencimentos com as vantagens pecuniárias permanentes estabelecidas em lei."],
    ["Como a Lei nº 8.112 aborda a questão de ajuda de custo?", "Ajuda de custo destina-se a compensar despesas de instalação do servidor que, no interesse do serviço, passar a ter exercício em nova sede."],
    ["Qual a previsão da Lei nº 8.112 sobre férias dos servidores públicos?", "30 dias por ano, podendo ser acumuladas, até o máximo de dois períodos, no interesse do serviço."],
    ["Qual é a abordagem da Lei nº 8.112 sobre responsabilidade civil do servidor?", "O servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições."]
    ]

# Criar DataFrame
df = pd.DataFrame(dados_lei_8112, columns=["Pergunta", "Resposta"])

# Caminho do arquivo CSV
caminho_csv = "~/Concursos/Leis/Lei_8112_Servidores_Publicos/Flashcards_Lei_8112.csv"

# Salvar como CSV
df.to_csv(caminho_csv, sep='\t', index=False, encoding='utf-8')

caminho_csv
