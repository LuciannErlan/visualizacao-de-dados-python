
# VISUALIZAÇÃO DE DADOS COM MATPLOTLIB

# O que é o Matplotlib?
# O Matplotlib é a biblioteca pioneira e mais fundamental de visualização de dados em Python.
# Praticamente todas as outras ferramentas (como Seaborn e as funções gráficas do Pandas)
# foram construídas sobre ela. O Matplotlib oferece controle absoluto sobre cada elemento visual:
# linhas, espessuras, fontes, eixos, legendas, anotações e molduras de gráficos.
#
# Conceitos Fundamentais:
# 1. Figure (fig): É a "tela em branco" ou folha de desenho geral.
# 2. Axes (ax): É o "gráfico em si", a área com eixos X e Y onde os dados são traçados.
#    Uma Figure pode conter um único Axes ou múltiplos Axes (painéis/subplots).


# 1. IMPORTAÇÃO DAS BIBLIOTECAS E CARREGAMENTO DOS DADOS

import pandas as pd                # Biblioteca principal para manipulação e estruturação de tabelas de dados
import matplotlib.pyplot as plt    # Submódulo do Matplotlib que fornece a interface de plotagem (pyplot)

# Carregamento da base de dados direto do arquivo Excel:
df = pd.read_excel("Novo_Vendas(base_de_dados).xlsx")

# Configurações globais de exibição do Pandas no terminal:
pd.set_option('display.max_columns', None)           # Exibe todas as colunas sem omitir com reticências (...)
pd.options.display.float_format = '{:20,.2f}'.format # Formata números com separador de milhar e 2 casas decimais
print("Primeiras 5 linhas da base de vendas:")
print(df.head())


# 2. GRÁFICO DE LINHAS BÁSICO (COM LISTAS DE EXEMPLO)

# Criando duas listas numéricas para demonstrar como o Matplotlib mapeia pontos cartesianos:
x = [2, 4, 6, 8, 10]               # Coordenadas do eixo horizontal (eixo X)
y = [1, 2, 3, 4, 5]                # Coordenadas do eixo vertical (eixo Y)

# plt.plot(x, y): desenha uma linha conectando os pontos (2,1), (4,2), (6,3), etc.
plt.plot(x, y)

# plt.show(): renderiza a janela gráfica na tela e exibe o resultado final
plt.show()


# 3. PERSONALIZANDO O GRÁFICO (CORES, ESTILOS, MARCADORES E LEGENDA)

# plt.plot com argumentos visuais específicos:
# color='red': define a cor da linha como vermelha
# linestyle='--': transforma a linha contínua em tracejada (dashed)
# marker='o': coloca um marcador circular em cada ponto coordenado
# markersize=10: define o diâmetro do marcador em pontos tipográficos
# label='Linha 1': texto identificador que aparecerá na legenda
plt.plot(x, y, color='red', linestyle='--', marker='o', markersize=10, label='Linha 1')

# plt.legend(): ativa a exibição da caixa de legenda no gráfico (usando os textos definidos em 'label')
plt.legend()
plt.show()


# 4. GRÁFICO COM TÍTULOS, RÓTULOS DE EIXOS E GRADE

# linewidth=2: define a espessura da linha
plt.plot(x, y, color='black', linestyle='-', marker='o', linewidth=2)

# plt.title(): adiciona o título principal no topo do gráfico (fontsize define o tamanho da fonte)
plt.title('Gráfico de Linhas', fontsize=16)

# plt.xlabel() e plt.ylabel(): adicionam nomes descritivos aos eixos X e Y
plt.xlabel('Eixo X', fontsize=14)
plt.ylabel('Eixo Y', fontsize=14)

# plt.grid(True): adiciona linhas de grade ao fundo para facilitar a leitura das medidas
# linestyle='--': grade com traços pontilhados
# alpha=0.6: nível de transparência da grade (0.0 invisível até 1.0 totalmente opaco)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Documentação de apoio:
# Marcadores disponíveis: https://matplotlib.org/stable/api/markers_api.html
# Estilos de linha disponíveis: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html


# 5. GRÁFICO DE LINHAS COM DADOS REAIS: LUCRO POR MÊS

# df.groupby('mes_venda')['Lucro'].sum(): agrupa as vendas por mês e calcula a soma total do lucro
lucro_mes = df.groupby('mes_venda')['Lucro'].sum()

# lucro_mes.index: contém os números dos meses (1, 2, ..., 12) -> Eixo X
# lucro_mes.values: contém os valores acumulados de lucro em reais -> Eixo Y
plt.plot(lucro_mes.index, lucro_mes.values, marker='o', color='green')

plt.title('Lucro por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=14)
plt.ylabel('Lucro Total (R$)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# 6. GRÁFICO DE BARRAS VERTICAIS: LUCRO POR MÊS

# plt.bar(): desenha barras verticais para comparar valores entre categorias discretas
# 1º parâmetro: categorias no eixo X (os meses)
# 2º parâmetro: altura das barras no eixo Y (o lucro acumulado)
# color='blue': define a cor das barras
plt.bar(lucro_mes.index, lucro_mes.values, color='blue')

plt.title('Lucro por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=14)
plt.ylabel('Lucro Total (R$)', fontsize=14)

# axis='y': aplica as linhas de grade apenas na horizontal (guiando a leitura da altura das barras)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# 7. GRÁFICO DE BARRAS VERTICAIS: QUANTIDADE POR MARCA

# Agrupa por Marca, soma a Quantidade vendida e ordena do maior para o menor com sort_values(ascending=False)
total_marca = df.groupby('Marca')['Quantidade'].sum().sort_values(ascending=False).reset_index()

plt.bar(total_marca['Marca'], total_marca['Quantidade'], color='orange')
plt.title('Quantidade de Pedidos por Marca', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Quantidade Total', fontsize=14)

# plt.xticks(rotation=45): rotaciona os nomes das marcas no eixo X em 45 graus para não sobrepor o texto
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# 8. GRÁFICO DE BARRAS HORIZONTAIS: QUANTIDADE POR MARCA (plt.barh)

# plt.barh(): inverte os eixos para criar barras horizontais (ideal quando os nomes das marcas são longos)
# 1º parâmetro (total_marca['Marca']): vai para o eixo vertical (Y)
# 2º parâmetro (total_marca['Quantidade']): define o comprimento horizontal da barra (X)
total_marca = df.groupby('Marca')['Quantidade'].sum().sort_values(ascending=False).reset_index()
plt.barh(total_marca['Marca'], total_marca['Quantidade'], color='orange')

plt.title('Quantidade de Pedidos por Marca', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Quantidade Total', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# 9. SUBPLOTS E RÓTULOS DE DADOS AUTOMÁTICOS (ABORDAGEM ORIENTADA A OBJETOS)

total_marca = df.groupby('Marca')['Quantidade'].sum().sort_values(ascending=False).reset_index()
lucro_mes = df.groupby('mes_venda')['Lucro'].sum()

# plt.subplots(1, 2, figsize=(16, 6)):
# Cria uma grade com 1 linha e 2 colunas de gráficos lado a lado em uma tela de largura 16 e altura 6
# fig: representa a moldura inteira
# axs: array com os 2 subplots individuais -> axs[0] é o da esquerda e axs[1] é o da direita
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico da Esquerda (axs[0]): Barras horizontais de marcas
# Guardamos o retorno em 'barras1' para poder anexar os rótulos depois
barras1 = axs[0].barh(total_marca['Marca'], total_marca['Quantidade'], color='orange')
axs[0].set_title('Quantidade de Pedidos por Marca', fontsize=14)

# axs[0].bar_label(): função mágica do Matplotlib que coloca os números exatos ao lado de cada barra
# padding=3: espaço em pixels entre o final da barra e o número do rótulo
axs[0].bar_label(barras1, padding=3)

# Gráfico da Direita (axs[1]): Linha temporal de lucro por mês
axs[1].plot(lucro_mes.index, lucro_mes.values, marker='o', color='green', linewidth=2)
axs[1].set_title('Lucro por Mês', fontsize=14)
axs[1].set_xlabel('Mês', fontsize=12)
axs[1].set_ylabel('Lucro (R$)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)

# plt.tight_layout(): reorganiza automaticamente os espaçamentos entre gráficos para não cortar títulos nem eixos
plt.tight_layout()
plt.show()


# 10. GRÁFICO DE PIZZA USANDO A EXTENSÃO DO PANDAS (.plot.pie)

# O Pandas permite criar gráficos direto de um groupby chamando o método .plot:
# autopct='%1.1f%%': formata a fatia para exibir a porcentagem com 1 casa decimal (ex: 35.4%)
# startangle=90: rotaciona o início da primeira fatia para começar exatamente no topo (90 graus)
# shadow=True: adiciona um efeito sutil de sombra tridimensional embaixo da pizza
# figsize=(8, 8): define dimensões quadradas para que a pizza não fique ovalada
lucro_categoria = df.groupby('Categoria')['Lucro'].sum().plot.pie(autopct='%1.1f%%', startangle=90, shadow=True, figsize=(8, 8))
plt.title('Lucro por Categoria', fontsize=16)

# plt.get_cmap("tab20c"): acessa uma paleta de cores categorizada do Matplotlib
cmap = plt.get_cmap("tab20c")
autopct = "%.1f%%"
plt.show()


# 11. GRÁFICO DE PIZZA COM MATPLOTLIB PURO (plt.pie)

cmap = plt.get_cmap("tab20c")
total_categoria = df.groupby('Categoria')['Lucro'].sum().reset_index()

# plt.pie():
# 1º argumento (total_categoria['Lucro']): valores numéricos que definem o tamanho de cada fatia
# labels=total_categoria['Categoria']: rótulos com os nomes das categorias ao redor da pizza
# colors=cmap.colors: aplica a sequência de cores da paleta 'tab20c' nas fatias
plt.pie(total_categoria['Lucro'], labels=total_categoria['Categoria'], autopct='%.1f%%', startangle=90, shadow=True, colors=cmap.colors)
plt.title('Lucro por Categoria', fontsize=16)

# Dica de Ouro (Transformar Pizza em Rosca / Donut Chart):
# Se você descomentar a linha abaixo, ela desenha um círculo branco com 60% do raio no centro:
# plt.pie([1], colors="white", radius=0.6)

plt.show()


# 12. GRÁFICO DE DISPERSÃO (SCATTER PLOT): RELAÇÃO CUSTO X LUCRO

# plt.scatter(): plota pares ordenados (X, Y) para identificar correlação entre duas variáveis quantitativas
# x: df['Custo'] -> quanto foi investido na fabricação/aquisição
# y: df['Lucro'] -> quanto retornou financeiramente
# color='purple': cor dos pontos
# alpha=0.6: transparência dos pontos (permite ver regiões onde centenas de vendas se concentram)
plt.scatter(df['Custo'], df['Lucro'], color='purple', alpha=0.6)
plt.title('Dispersão entre Custo e Lucro', fontsize=16)
plt.xlabel('Custo (R$)', fontsize=14)
plt.ylabel('Lucro (R$)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# 13. HISTOGRAMA (DISTRIBUIÇÃO DE FREQUÊNCIAS DO CUSTO UNITÁRIO)

# plt.hist(): divide uma variável contínua em intervalos (bins) e conta a frequência de observações
# df["Custo Unitário"]: coluna analisada
# color="red": cor de preenchimento das barras
# edgecolor="black": adiciona uma linha de contorno preta em cada barra para destacá-las visualmente
# bins=10: agrupa os dados em exatamente 10 faixas de valores
plt.hist(df["Custo Unitário"], color="red", edgecolor="black", bins=10)
plt.xlabel('Custo Unitário (R$)', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.title('Distribuição do Custo Unitário', fontsize=16)
plt.show()  


# 14. BOXPLOT (DIAGRAMA DE CAIXA: DETECÇÃO DE OUTLIERS E QUARTIS)

# plt.boxplot(): desenha uma caixa estatística dividida em:
# - Linha central: Mediana (o ponto central dos dados)
# - Corpo da caixa: Intervalo Interquartil (IQR: 50% dos dados centrais, entre Q1 25% e Q3 75%)
# - Hastes (whiskers): limites superior e inferior esperados
# - Pontos isolados além das hastes: Outliers (valores anômalos ou muito distantes do padrão)
plt.boxplot(df["Custo Unitário"])
plt.title('Boxplot do Custo Unitário', fontsize=16)
plt.ylabel('Custo Unitário (R$)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# 15. APLICANDO ESTILOS PRÉ-CONFIGURADOS DO MATPLOTLIB (plt.style.use)

# plt.style.use('ggplot'): aplica o tema clássico do ggplot (fundo cinza suave e grade branca)
# aos próximos gráficos gerados no script, padronizando a estética geral
plt.style.use('ggplot')
# Catálogo completo de estilos visuais do Matplotlib:
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html