
# VISUALIZAÇÃO INTERATIVA DE DADOS COM PLOTLY EXPRESS

# O que é o Plotly Express?
# O Plotly Express (px) é uma biblioteca de alto nível em Python para criação rápida de gráficos interativos.
# Diferente do Matplotlib e do Seaborn que geram imagens estáticas, o Plotly gera gráficos em HTML/JavaScript 
# onde você pode passar o mouse (hover), dar zoom, arrastar a tela e isolar categorias clicando na legenda!
# Documentação oficial: https://plotly.com/python/plotly-express/


# 1. IMPORTAÇÃO DAS BIBLIOTECAS E CARREGAMENTO DOS DADOS

import pandas as pd                # Biblioteca para manipulação e análise de dados tabulares
import plotly.express as px        # Módulo simplificado do Plotly para criar gráficos interativos com poucas linhas

# Carregamento da base de dados
df = pd.read_excel("Novo_Vendas(base_de_dados).xlsx")

# Configurações de exibição do Pandas no terminal:
pd.set_option('display.max_columns', 100)           # Permite visualizar até 100 colunas sem truncar com '...'
pd.options.display.float_format = '{:20,.2f}'.format # Formata números decimais com 2 casas e separador de milhar
print("Primeiras 5 linhas da base de vendas:")
print(df.head(5))


# 2. GRÁFICO DE LINHAS BÁSICO (COM LISTAS DE EXEMPLO)

# Criando listas simples de dados para entender o funcionamento básico da função px.line:
meses = ['jan', 'fev', 'mar', 'abr', 'mai']
vendas = [120, 150, 80, 200, 90]

# px.line: função que cria um gráfico de linhas
# x=meses: valores que ficarão no eixo horizontal
# y=vendas: valores que ficarão no eixo vertical
# title: título exibido no topo do gráfico
fig = px.line(x=meses, y=vendas, title="Vendas mensais")

# fig.show(): renderiza e abre o gráfico interativo na tela
fig.show()


# 3. GRÁFICO DE LINHAS COM DADOS REAIS (LUCRO POR MÊS)

# Agrupando a base pelo campo "mes-ano", somando o "Lucro" e transformando de volta em DataFrame com .reset_index()
lucro_mes = df.groupby("mes-ano")["Lucro"].sum().reset_index()
print(lucro_mes.head())

# Criando a linha com o DataFrame real:
# 1º parâmetro (lucro_mes): o DataFrame que contém os dados
# x="mes-ano": nome da coluna do DataFrame para o eixo X
# y="Lucro": nome da coluna do DataFrame para o eixo Y
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês")
fig.show()


# 4. ADICIONANDO MARCADORES DE PONTOS NA LINHA

# markers=True: adiciona marcadores circulares em cima de cada ponto da linha,
# facilitando visualizar exatamente onde cada mês está posicionado e passar o mouse sobre ele
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True)
fig.show()


# 5. PERSONALIZANDO O ESTILO DA LINHA (PONTILHADA, ESPESSURA E COR)

fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True)

# fig.update_traces: permite modificar propriedades visuais das "linhas/traços" já criados
# line=dict(...): dicionário com as propriedades de estilo da linha:
#   dash="dot": transforma a linha contínua em pontilhada (opções: "solid", "dot", "dash", "dashdot")
#   width=3: define a espessura da linha em pixels
#   color="blue": define a cor da linha
fig.update_traces(line=dict(dash="dot", width=3, color="blue"))
fig.show()


# 6. GRÁFICO DE BARRAS VERTICAIS (QUANTIDADE POR MARCA)

# Agrupando por Marca, somando a Quantidade e ordenando do menor para o maior (ascending=True)
total_marca = df.groupby("Marca")["Quantidade"].sum().sort_values(ascending=True).reset_index()
print(total_marca)

# px.bar: cria um gráfico de barras
# x="Marca": categorias no eixo horizontal (barras verticais)
# y="Quantidade": altura das barras baseada no total vendido
fig = px.bar(total_marca, x="Marca", y="Quantidade", title="Total Produtos vendidos por Marca")
fig.show()


# 7. GRÁFICO DE BARRAS HORIZONTAIS (FACILITA A LEITURA DOS NOMES)

# No Plotly, para transformar o gráfico em barras horizontais basta INVERTER o x e o y:
# x="Quantidade": o valor numérico vai para o eixo horizontal (comprimento da barra)
# y="Marca": os nomes vão para o eixo vertical (leitura muito mais confortável)
fig = px.bar(total_marca, x="Quantidade", y="Marca", title="Total Produtos vendidos por Marca")
fig.show()


# 8. BARRAS EMPILHADAS POR ANO (QUEBRANDO UMA VARIÁVEL POR COR)

# Agrupando por duas variáveis ao mesmo tempo: Marca e Ano Venda
total_marca_ano = df.groupby(["Marca", "Ano Venda"])["Quantidade"].sum().reset_index()

# CONVERSÃO CRUCIAL: Convertemos "Ano Venda" para texto (str).
# Se deixarmos como número, o Plotly tentará criar uma escala contínua de cores (gradiente).
# Como texto, ele entende que são categorias discretas e cria uma legenda com cores separadas!
total_marca_ano["Ano Venda"] = total_marca_ano["Ano Venda"].astype(str)

# color="Ano Venda": divide cada barra em fatias coloridas empilhadas, uma para cada ano
fig = px.bar(total_marca_ano, x="Marca", y="Quantidade", title="Total Produtos vendidos por Marca",
             color="Ano Venda")
fig.show()


# 9. BARRAS AGRUPADAS LADO A LADO (barmode='group')

# barmode='group': em vez de empilhar as barras dos anos uma sobre a outra,
# coloca as barras de cada ano lado a lado para facilitar a comparação direta ano contra ano
fig = px.bar(total_marca_ano, x="Marca", y="Quantidade", title="Total Produtos vendidos por Marca",
             color="Ano Venda", barmode='group')
fig.show()


# 10. SUBPLOTS (PAINEL COM MÚLTIPLOS GRÁFICOS LADO A LADO)

from plotly.subplots import make_subplots

# 1º Criamos os dois gráficos separadamente:

fig_bar = px.bar(total_marca, x="Quantidade", y="Marca")
fig_line = px.line(lucro_mes, x="mes-ano", y='Lucro', markers=True)

# 2º Criamos a estrutura/grade dos subplots:

# rows=1: 1 linha
# cols=2: 2 colunas (gráficos lado a lado)
# subplot_titles: lista com o título individual de cada gráfico
fig = make_subplots(rows=1, cols=2, subplot_titles=["Produtos vendidos por Marca", "Lucro por Mês"])

# 3º Adicionamos os rastros/dados de cada gráfico dentro da célula correspondente da grade:

# fig_bar.data[0]: pega a camada de desenho do gráfico de barras e coloca na Linha 1, Coluna 1
fig.add_trace(fig_bar.data[0], row=1, col=1)
# fig_line.data[0]: pega a camada do gráfico de linhas e coloca na Linha 1, Coluna 2
fig.add_trace(fig_line.data[0], row=1, col=2)

fig.show()


# 11. RÓTULOS DE DADOS NAS BARRAS (EXIBINDO VALORES NUMÉRICOS)

# text="Quantidade": imprime automaticamente o valor numérico de cada barra dentro ou na ponta dela
fig = px.bar(total_marca, x="Quantidade", y="Marca", title="Total Produtos vendidos por Marca",
             text="Quantidade")
fig.show()


# 12. GRÁFICO DE PIZZA (LUCRO POR CATEGORIA)

total_categoria = df.groupby("Categoria")["Lucro"].sum().reset_index()

# px.pie: cria o gráfico de setores (pizza)
# values="Lucro": coluna numérica que define o tamanho/fatia de cada pedaço
# names="Categoria": coluna com os rótulos de texto que identificam cada pedaço
fig = px.pie(total_categoria, values="Lucro", names="Categoria", title="Lucro por categoria")
fig.show()


# 13. GRÁFICO DE ROSCA (DONUT CHART COM hole=0.6)

# hole=0.6: cria um furo no meio da pizza equivalente a 60% do raio,
# transformando a pizza tradicional em um gráfico de rosca (mais moderno e com melhor apelo estético)
fig = px.pie(total_categoria, values="Lucro", names="Categoria", title="Lucro por categoria",
             hole=0.6)
fig.show()


# 14. GRÁFICO DE DISPERSÃO (SCATTER PLOT) BÁSICO

# px.scatter: plota pontos para analisar a correlação entre duas variáveis contínuas
# x="Custo": posição horizontal do ponto
# y="Lucro": posição vertical do ponto
fig = px.scatter(df, x="Custo", y="Lucro", title="Relação Custo x Lucro")
fig.show()


# 15. DISPERSÃO COM DIFERENCIAÇÃO POR CORES (color="Categoria")

# color="Categoria": aplica uma cor diferente para cada Categoria de produto,
# permitindo descobrir visualmente quais categorias geram mais lucro com menor custo
fig = px.scatter(df, x="Custo", y="Lucro", title="Relação Custo x Lucro", color="Categoria")
fig.show()


# 16. GRÁFICO DE BOLHAS (BUBBLE CHART COM size="Lucro")

# size="Lucro": adiciona uma terceira dimensão visual aos pontos!
# O diâmetro de cada bolha agora reflete o tamanho do Lucro daquela venda
fig = px.scatter(df, x="Custo", y="Lucro", title="Relação Custo x Lucro", color="Categoria",
                 size="Lucro")
fig.show()


# 17. HISTOGRAMA BÁSICO (DISTRIBUIÇÃO DE FREQUÊNCIAS)

# px.histogram: divide uma variável numérica contínua em faixas/intervalos (bins)
# e conta quantas vendas caíram dentro de cada faixa
fig = px.histogram(df, x="Custo Unitário", title="Histograma Custo Unitário")
fig.show()


# 18. HISTOGRAMA COM NÚMERO DE FAIXAS CONTROLADO (nbins=20)

# nbins=20: força o histograma a dividir os dados em aproximadamente 20 barras (intervalos mais refinados)
fig = px.histogram(df, x="Custo Unitário", title="Histograma Custo Unitário", nbins=20)
fig.show()


# 19. BOXPLOT BÁSICO (DIAGRAMA DE CAIXA)

# px.box: exibe mediana, quartis (25% e 75%), limites inferior/superior e identifica outliers (pontos isolados)
fig = px.box(df, y="Custo Unitário")
fig.show()


# 20. BOXPLOT COMPARATIVO ENTRE CATEGORIAS

# x="Categoria": desenha uma caixa para cada categoria lado a lado
# y="Lucro": analisa a distribuição e dispersão do lucro para cada grupo
fig = px.box(df, x="Categoria", y="Lucro")
fig.show()


# 21. CATÁLOGO VISUAL DE CORES QUALITATIVAS DO PLOTLY

# px.colors.qualitative.swatches(): gera uma visualização de todas as paletas de cores padrão do Plotly Express
# (ex: Plotly, D3, G10, T10, Alphabet, Dark24, Light24, Set1, Pastel, Vivid, etc.)
fig = px.colors.qualitative.swatches()
fig.show()


# 22. APLICANDO PALETA DE CORES PRÉ-DEFINIDA (Vivid)

# color_discrete_sequence: aceita uma paleta do catálogo do Plotly ou uma lista de cores
# px.colors.qualitative.Vivid: paleta com cores vivas e contrastantes
fig = px.bar(total_marca, x="Quantidade", y="Marca", title="Total Produtos vendidos por Marca",
             text="Quantidade", color_discrete_sequence=px.colors.qualitative.Vivid)
fig.show()


# 23. APLICANDO UMA COR ÚNICA COM NOME ("black")

# color_discrete_sequence=["black"]: pinta todas as barras com uma cor preta sólida
fig = px.bar(total_marca, x="Quantidade", y="Marca", title="Total Produtos vendidos por Marca",
             text="Quantidade", color_discrete_sequence=["black"])
fig.show()


# 24. APLICANDO UMA COR CORPORATIVA HEXADECIMAL ("#3e4095")

# color_discrete_sequence=["#3e4095"]: aceita qualquer código HEX (muito usado para seguir a identidade visual de empresas)
fig = px.bar(total_marca, x="Quantidade", y="Marca", title="Total Produtos vendidos por Marca",
             text="Quantidade", color_discrete_sequence=["#3e4095"])
fig.show()


# 25. ALTERANDO TEMAS/BACKGROUNDS: TEMPLATE "ggplot2"

# template="ggplot2": aplica o estilo clássico do ggplot (fundo cinza com grade branca), muito popular em R
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="ggplot2")
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.show()


# 26. TEMPLATE ESCURO / DARK MODE: "plotly_dark"

# template="plotly_dark": aplica fundo escuro/preto elegante para apresentações ou dashboards com dark mode
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark")
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.show()


# 27. REMOVENDO AS LINHAS DE GRADE (showgrid=False)

# fig.update_layout: método para customizar o layout geral da figura (eixos, legendas, margens, etc.)
# xaxis = dict(showgrid=False): desativa a grade vertical do eixo X
# yaxis = dict(showgrid=False): desativa a grade horizontal do eixo Y (deixa o visual mais minimalista)
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark")
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False)
)
fig.show()


# 28. CENTRALIZANDO O TÍTULO DO GRÁFICO (title_x = 0.5)

# title_x: define o alinhamento horizontal do título na escala de 0 a 1:
#   0.0 = alinhado totalmente à esquerda
#   0.5 = centralizado perfeitamente no meio do gráfico
#   1.0 = alinhado totalmente à direita
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark")
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title_x=0.5 # Centralizando o título
)
fig.show()


# 29. RENOMEANDO OS RÓTULOS DOS EIXOS COM labels={...}

# labels={"mes-ano": "Mês", "Lucro": "Lucro Mensal"}:
# Substitui os nomes técnicos das colunas do banco de dados por nomes amigáveis para quem lê o relatório
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark",
              labels={"mes-ano": "Mês", "Lucro": "Lucro Mensal"})
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title_x=0.5 # Centralizando o título
)
fig.show()


# 30. DEFININDO O TAMANHO FIXO DO GRÁFICO (width e height)

# width=600: largura fixa em pixels
# height=400: altura fixa em pixels (ideal para padronizar relatórios e evitar que o gráfico ocupe a tela toda)
fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark",
              labels={"mes-ano": "Mês", "Lucro": "Lucro Mensal"}, width=600, height=400)
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title_x=0.5 # Centralizando o título
)
fig.show()


# 31. ADICIONANDO ANOTAÇÕES COM TEXTO E SETA (STORYTELLING COM DADOS)

fig = px.line(lucro_mes, x="mes-ano", y='Lucro', title="Lucro por Mês", markers=True, template="plotly_dark",
              labels={"mes-ano": "Mês", "Lucro": "Lucro Mensal"})
fig.update_traces(line=dict(dash="dot", color="#f37135"))
fig.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title_x=0.5 # Centralizando o título
)

# fig.add_annotation: desenha uma anotação textual personalizada com seta apontando para um ponto crítico do gráfico:
fig.add_annotation(
    x="2018-01",                                      # Posição no eixo X onde a ponta da seta deve mirar
    y=1890000.79,                                     # Posição no eixo Y onde a ponta da seta deve mirar
    text="Queda de 48% comparado ao mês anterior",     # Mensagem textual da anotação
    showarrow=True,                                   # True para exibir a seta apontando
    arrowhead=3,                                      # Estilo/desenho da ponta da seta (valores de 0 a 8)
    ax=20,                                            # Deslocamento horizontal do texto em relação à ponta (em pixels)
    ay=30                                             # Deslocamento vertical do texto em relação à ponta (em pixels)
)
fig.show()