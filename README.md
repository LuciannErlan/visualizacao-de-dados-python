# 📊 Trilha de Visualização de Dados em Python: Matplotlib, Seaborn & Plotly

> Um guia prático, didático e comparativo explorando a tríade fundamental de bibliotecas de visualização de dados do ecossistema Python sobre uma base real de mais de 70.000 vendas.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Base%20Visualization-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Data%20Viz-4c72b0)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)

---

## 🎯 Sobre o Projeto

Este repositório reúne um estudo aprofundado sobre **Visualização de Dados em Python**, demonstrando como a mesma base de negócios (`Novo_Vendas`) pode ser explorada sob diferentes perspectivas, necessidades e ferramentas.

O projeto está estruturado em três scripts principais, totalmente comentados linha a linha para servir como material de estudo e referência técnica para análises exploratórias de dados (EDA) e inteligência de negócios (BI).

---

## ⚖️ A Tríade da Visualização: Qual ferramenta escolher?

| Biblioteca | Foco Principal | Vantagens | Quando usar? |
| :--- | :--- | :--- | :--- |
| **Matplotlib** 🧱 | Controle e Estrutura | Controle granular de cada pixel, linha, eixo e legenda. Base de todo o ecossistema. | Relatórios estáticos, artigos técnicos e customizações milimétricas de layout. |
| **Seaborn** 🎨 | Análise Estatística | Integração nativa com DataFrames do Pandas, temas elegantes e o poder do parâmetro `hue`. | Análise exploratória inicial (EDA), distribuições, correlações e comparação de categorias. |
| **Plotly** 🌐 | Interatividade & Web | Gráficos dinâmicos no navegador (hover, zoom, isolamento de categorias) e recursos de Storytelling. | Apresentações executivas, dashboards web e exploração interativa de métricas de negócios. |

---

## 📂 Estrutura do Repositório

```text
├── Novo_Vendas(base_de_dados).xlsx   # Base de dados com mais de 70.000 registros de vendas
├── aprendendo_matplotlib.py           # 15 exemplos práticos (linhas, barras, subplots, pie, scatter, hist, boxplot)
├── aprendendo_seaborn.py              # Visualizações estatísticas com barplot, scatterplot (hue), histplot (KDE) e boxplot
├── aprendendo_plotly.py               # Mais de 30 visualizações interativas com Plotly Express, temas e data storytelling
├── .gitignore                         # Arquivos e pastas temporárias ignoradas pelo Git
└── README.md                          # Documentação oficial do projeto
```

---

## 🚀 Conteúdo Abordado em Cada Módulo

### 1. `aprendendo_matplotlib.py`
* **Fundamentos de Arquitetura:** Conceito de `Figure` (tela) vs. `Axes` (gráfico).
* **Personalização Completa:** Espessura de linha, cores, marcadores (`marker='o'`) e estilos de linha (`linestyle='--'`).
* **Comparação Categórica:** Barras verticais e horizontais (`plt.bar` e `plt.barh`) com rotação de eixos (`plt.xticks(rotation=45)`).
* **Subplots Orientados a Objetos:** Criação de painéis com `plt.subplots()` e adição automática de rótulos de dados (`ax.bar_label`).
* **Visualizações Estatísticas:** Gráficos de setores/pizza (`plt.pie`), dispersão (`plt.scatter`), histograma (`plt.hist`) e boxplots (`plt.boxplot`).
* **Estilos Globais:** Aplicação de temas pré-configurados com `plt.style.use('ggplot')`.

### 2. `aprendendo_seaborn.py`
* **Estética Automática:** Ativação de temas globais com `sns.set_theme(style="whitegrid")`.
* **Cálculos Integrados:** Gráficos de barras que calculam agregações automaticamente (`estimator=sum` e `errorbar=None`).
* **O Poder do `hue`:** Quebra de gráficos de dispersão por categorias em cores sem necessidade de loops manuais.
* **Distribuição Contínua:** Histogramas combinados com Curva de Densidade Suave (`kde=True`).
* **Análise de Variabilidade:** Boxplots comparativos entre categorias com paletas de cores refinadas (`palette="Set2"`).

### 3. `aprendendo_plotly.py`
* **Interatividade Web:** Renderização dinâmica em HTML/JavaScript direto no navegador.
* **Barras Empilhadas vs. Agrupadas:** Controle de comparação ano contra ano com `barmode='group'`.
* **Múltiplos Gráficos Interativos:** Painéis com `make_subplots` combinando barras e linhas.
* **Design Moderno:** Gráfico de rosca (*Donut Chart*) com furo central via `hole=0.6`.
* **Gráficos de Bolhas:** Adição de terceira dimensão com diâmetro variável (`size="Lucro"`).
* **Temas Corporativos:** Aplicação de modo escuro executivo com `template="plotly_dark"`.
* **Data Storytelling:** Anotações personalizadas com setas apontando para quedas e picos críticos (`fig.add_annotation`).

---

## 💻 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LuciannErlan/visualizacao-de-dados-python.git
   cd visualizacao-de-dados-python
   ```

2. **Instale as dependências necessárias:**
   ```bash
   pip install pandas openpyxl matplotlib seaborn plotly
   ```

3. **Execute qualquer um dos módulos no terminal:**
   ```bash
   python aprendendo_matplotlib.py
   python aprendendo_seaborn.py
   python aprendendo_plotly.py
   ```

---

## 👤 Autor

Desenvolvido por **Luciann Erlãn** como parte da trilha prática de estudos em Ciência e Análise de Dados.

* **GitHub:** [@LuciannErlan](https://github.com/LuciannErlan)
* **LinkedIn:** [Luciann Erlãn](https://www.linkedin.com/)

---
*⭐ Se este projeto te ajudou ou serviu como referência de estudos, deixe uma estrela no repositório!*

