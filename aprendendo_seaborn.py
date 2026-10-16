
# VISUALIZAÇÃO ESTATÍSTICA DE DADOS COM SEABORN

# O que é o Seaborn?
# O Seaborn é uma biblioteca de visualização de dados de alto nível construída por cima do Matplotlib.
# Enquanto no Matplotlib precisamos fazer agrupamentos e contas manualmente antes de plotar,
# o Seaborn foi feito para trabalhar DIRETAMENTE com DataFrames do Pandas:
#
# Principais Vantagens do Seaborn:
# 1. Menos linhas de código: calcula somas, médias e estatísticas automaticamente.
# 2. O superpoder do 'hue': quebra qualquer gráfico por uma terceira variável com apenas um parâmetro.
# 3. Estética moderna: temas prontos, paletas de cores refinadas e grades suaves por padrão.
# Documentação oficial: https://seaborn.pydata.org/


# 1. IMPORTAÇÃO DAS BIBLIOTECAS E ESTILO GERAL DO SEABORN

import pandas as pd                # Manipulação e estruturação dos dados tabulares
import matplotlib.pyplot as plt    # Usado para controlar tamanho de figuras (plt.figure) e exibir gráficos (plt.show)
import seaborn as sns              # Biblioteca especializada em visualização estatística e estética refinada

# sns.set_theme(style="whitegrid"): ativa o tema visual global do Seaborn
# 'whitegrid' aplica um fundo branco limpo com linhas de grade cinzas bem suaves,
# ideal para relatórios corporativos e artigos analíticos
sns.set_theme(style="whitegrid")

# Carregamento da base de dados direto do arquivo Excel:
df = pd.read_excel("Novo_Vendas(base_de_dados).xlsx")

print("Base de dados carregada com sucesso!")
print(df.head(2))


# 2. GRÁFICO DE BARRAS COM SEABORN (sns.barplot)

# plt.figure(figsize=(10, 5)): define a largura (10) e altura (5) da tela em polegadas
plt.figure(figsize=(10, 5))

# sns.barplot: cria o gráfico de barras calculando estatísticas automaticamente
# data=df: o DataFrame do Pandas de onde as colunas serão extraídas
# x="Categoria": coluna com os nomes das categorias (eixo horizontal)
# y="Lucro": coluna com os valores numéricos a serem calculados (eixo vertical)
# estimator=sum: define a operação matemática que o Seaborn fará em cada categoria
#                (por padrão o Seaborn calcula a MÉDIA; com estimator=sum ele calcula a SOMA TOTAL)
# errorbar=None: desativa a barra preta de intervalo de confiança / erro no topo das barras
# palette="Blues_d": paleta de cores degradê em tons de azul escuro
ax = sns.barplot(data=df, x="Categoria", y="Lucro", estimator=sum, errorbar=None, palette="Blues_d")

plt.title("Lucro Total por Categoria", fontsize=15, weight="bold")
plt.xlabel("Categoria", fontsize=12)
plt.ylabel("Lucro Total (R$)", fontsize=12)

# Adicionando rótulos numéricos no topo de cada barra com ax.bar_label:
# ax.containers: lista com os conjuntos de barras desenhados na figura
# fmt="R$ {:,.0f}": formata o texto com o prefixo 'R$', separador de milhar e sem casas decimais
# padding=3: distância em pixels entre o topo da barra e o número do rótulo
for container in ax.containers:
    ax.bar_label(container, fmt="R$ {:,.0f}", padding=3)

# Dica de Posicionamento do Rótulo de Dados:
# label_type='edge': coloca o texto exatamente no topo/borda de cada barra (padrão)
# label_type='center': coloca o texto centralizado dentro do corpo de cada barra

plt.show()


# 3. GRÁFICO DE DISPERSÃO COM O PODER DO 'HUE' (sns.scatterplot)

plt.figure(figsize=(10, 6))

# sns.scatterplot: plota pontos para cruzar duas variáveis contínuas
# data=df: base de dados
# x="Custo": valor financeiro de custo de fabricação no eixo X
# y="Lucro": retorno financeiro no eixo Y
# hue="Categoria": O SUPERPODER DO SEABORN!
#                  Aplica automaticamente uma cor diferente para cada Categoria de produto,
#                  criando a legenda sozinho sem precisar de filtros manuais ou múltiplos loops!
# alpha=0.7: transparência dos círculos (70% opaco) para revelar pontos sobrepostos
# palette="tab10": paleta com 10 cores contrastantes e de fácil diferenciação visual
sns.scatterplot(
    data=df, 
    x="Custo", 
    y="Lucro", 
    hue="Categoria",
    alpha=0.7, 
    palette="tab10"
)

plt.title("Relação Custo vs Lucro por Categoria", fontsize=15, weight="bold")
plt.xlabel("Custo (R$)", fontsize=12)
plt.ylabel("Lucro (R$)", fontsize=12)
plt.show()


# 4. HISTOGRAMA COM CURVA DE DENSIDADE KDE (sns.histplot)

plt.figure(figsize=(9, 5))

# sns.histplot: gera o histograma de distribuição com recursos estatísticos modernos
# data=df: base de dados
# x="Custo Unitário": variável quantitativa contínua a ser distribuída em intervalos
# kde=True: (Kernel Density Estimation) desenha uma curva suave de densidade contínua
#           sobre as barras, facilitando enxergar o formato e a assimetria da distribuição
# color="teal": cor verde-azulada sofisticada para as barras
# bins=20: divide os dados em exatamente 20 faixas/intervalos de custos
sns.histplot(data=df, x="Custo Unitário", kde=True, color="teal", bins=20)

plt.title("Distribuição do Custo Unitário com Curva KDE", fontsize=15, weight="bold")
plt.xlabel("Custo Unitário (R$)", fontsize=12)
plt.ylabel("Contagem de Itens", fontsize=12)
plt.show()


# 5. BOXPLOT COMPARATIVO POR CATEGORIA (sns.boxplot)

plt.figure(figsize=(10, 5))

# sns.boxplot: gera o diagrama de caixas comparativo de forma extremamente rápida
# x="Categoria": desenha uma caixa estatística separada para cada categoria lado a lado
# y="Lucro": analisa a distribuição dos lucros dentro de cada um dos grupos
# palette="Set2": paleta suave e elegante de tons pastéis
#
# O que cada parte do Boxplot nos ensina sobre os dados:
# - Barra horizontal central: Mediana (o valor do meio da categoria)
# - Caixa retangular: 50% central de todas as vendas (entre o 1º e o 3º quartil)
# - Hastes verticais (whiskers): alcance normal dos lucros
# - Pontos isolados além das hastes: Outliers (vendas excepcionais ou atípicas)
sns.boxplot(data=df, x="Categoria", y="Lucro", palette="Set2")

plt.title("Distribuição e Outliers de Lucro por Categoria", fontsize=15, weight="bold")
plt.xlabel("Categoria", fontsize=12)
plt.ylabel("Lucro (R$)", fontsize=12)
plt.show()