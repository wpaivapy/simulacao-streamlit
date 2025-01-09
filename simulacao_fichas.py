import random
import plotly.graph_objects as go
import streamlit as st

# Configuração da página Streamlit
st.set_page_config(page_title="Simulação de Retiradas", layout="wide")

# Título e descrição
st.title("Simulação de Retiradas - Lei dos Grandes Números")
st.write("Informe os dados para simular retiradas de fichas e visualizar como as frequências relativas se aproximam das probabilidades teóricas.")

# Seção sobre a Lei dos Grandes Números
st.header("📘 O que é a Lei dos Grandes Números?")
st.markdown("""
A **Lei dos Grandes Números** é um princípio fundamental da probabilidade e estatística que afirma que, ao repetir um experimento aleatório muitas vezes, a frequência relativa de um evento tende a se aproximar de sua probabilidade teórica.

Por exemplo, se a probabilidade teórica de obter uma ficha verde é 40%, e você realiza muitas retiradas, a proporção de fichas verdes retiradas se aproximará cada vez mais de 40%. Porém, em poucas tentativas, podem ocorrer variações maiores devido à aleatoriedade.

Esta simulação ajuda a visualizar esse comportamento.
""")

# Entrada do usuário
with st.sidebar:
    st.header("Configurações")
    fichas_verdes = st.number_input("Quantidade de fichas verdes", min_value=1, value=4, step=1)
    fichas_amarelas = st.number_input("Quantidade de fichas amarelas", min_value=1, value=3, step=1)
    fichas_vermelhas = st.number_input("Quantidade de fichas vermelhas", min_value=1, value=3, step=1)
    num_retiradas_max = st.number_input("Número de retiradas", min_value=10, value=50, step=10)

# Criando a lista de fichas com base nas entradas
fichas = ['verde'] * fichas_verdes + ['amarelo'] * fichas_amarelas + ['vermelho'] * fichas_vermelhas
probabilidades_teoricas = {
    'verde': fichas_verdes / len(fichas),
    'amarelo': fichas_amarelas / len(fichas),
    'vermelho': fichas_vermelhas / len(fichas)
}

# Simulação das retiradas
resultados_cumulativos = {'verde': [], 'amarelo': [], 'vermelho': []}
contagem = {'verde': 0, 'amarelo': 0, 'vermelho': 0}

for i in range(1, int(num_retiradas_max) + 1):
    ficha = random.choice(fichas)
    contagem[ficha] += 1

    # Frequências relativas acumuladas
    for cor in contagem:
        frequencia_relativa = contagem[cor] / i
        resultados_cumulativos[cor].append(frequencia_relativa)

# Criando o gráfico com Plotly
cores = {'verde': 'green', 'amarelo': 'gold', 'vermelho': 'red'}
fig = go.Figure()

# Adicionando as linhas simuladas
for cor, valores in resultados_cumulativos.items():
    fig.add_trace(go.Scatter(
        x=list(range(1, int(num_retiradas_max) + 1)),
        y=valores,
        mode='lines',
        name=f"{cor.capitalize()} (Simulado)",
        line=dict(color=cores[cor])
    ))

# Adicionando as linhas teóricas
for cor, prob in probabilidades_teoricas.items():
    fig.add_trace(go.Scatter(
        x=[1, int(num_retiradas_max)],
        y=[prob, prob],
        mode='lines',
        name=f"{cor.capitalize()} (Teórico)",
        line=dict(color=cores[cor], dash='dash')
    ))

# Configurando o layout do gráfico
fig.update_layout(
    title="Aproximação das Frequências Relativas - Lei dos Grandes Números",
    xaxis_title="Número de Retiradas",
    yaxis_title="Frequência Relativa",
    legend_title="Legenda",
    template="plotly_white"
)

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

# Exibindo informações adicionais
st.write("### Probabilidades Teóricas:")
st.write(f"- Verde: {probabilidades_teoricas['verde']:.2%}")
st.write(f"- Amarelo: {probabilidades_teoricas['amarelo']:.2%}")
st.write(f"- Vermelho: {probabilidades_teoricas['vermelho']:.2%}")

# Rodapé
st.markdown("""
---
Desenvolvido por [William Paiva](https://www.linkedin.com/in/william-paiva-fin/).
""")
