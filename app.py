import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

ARQUIVO = "dados.csv"

# Configuração da página
st.set_page_config(page_title="Status das Máquinas", layout="centered")
st.title("📋 Status das Máquinas por Setor")

# ---- Estilo mobile-friendly ----
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        padding: 16px;
        font-size: 20px;
        border-radius: 10px;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    .stSelectbox, .stNumberInput, .stTextInput {
        font-size: 18px !important;
        margin-bottom: 10px;
    }
    .stDataFrame {
        font-size: 14px !important;
    }
    .stMarkdown h3, .stMarkdown h4 {
        margin-top: 10px;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Configurações ----
setores = {
    "Pintura": ["Máquina 1", "Máquina 2"],
    "Tubo Loose": ["Máquina 1", "Máquina 2"],
    "SZ": ["Máquina 1", "Máquina 2"],
    "Capas": ["Máquina 1", "Máquina 2"],
    "Drop": ["Máquina 1", "Máquina 2"]
}
status_opcoes = ["Rodando", "Manutenção", "Parada", "Outros"]
lideres = ["Líder 1", "Líder 2", "Líder 3"]

# ---- Formulário ----
with st.form("formulario"):
    turno = st.number_input("Turno", min_value=1, max_value=3, step=1)
    lider = st.selectbox("Escolha o Líder responsável", lideres)
    registros = {}

    for setor, maquinas in setores.items():
        st.subheader(f"🟢 {setor}")
        for m in maquinas:
            col1, col2 = st.columns([2,3])
            with col1:
                st.markdown(f"**{m}**")
            with col2:
                status = st.selectbox(f"Status {setor} {m}", status_opcoes, key=f"{setor}_{m}")
                if status == "Outros":
                    descricao = st.text_input(f"Descreva status de {setor} {m}", key=f"{setor}_{m}_outro")
                    status = descricao if descricao.strip() else "Outros"
                registros[f"{setor} {m}"] = status

    enviado = st.form_submit_button("✅ Enviar Registro")

# ---- Salvamento ----
if enviado:
    data_hora = datetime.now()
    nova_linha = {
        "Data e Hora": data_hora.strftime("%d/%m/%Y %H:%M"),
        "Turno": turno,
        "Líder": lider
    }
    nova_linha.update(registros)

    df_nova = pd.DataFrame([nova_linha])

    try:
        df_existente = pd.read_csv(ARQUIVO)
        df = pd.concat([df_existente, df_nova], ignore_index=True)
    except FileNotFoundError:
        df = df_nova

    df.to_csv(ARQUIVO, index=False)
    st.success("✅ Registro salvo com sucesso!")

# ---- Visualização ----
st.header("📊 Status das Máquinas por Setor e Turno")

try:
    df = pd.read_csv(ARQUIVO)

    if "Líder" not in df.columns:
        df["Líder"] = "Desconhecido"

    df_grafico = df.melt(
        id_vars=["Data e Hora", "Turno", "Líder"],
        var_name="Máquina",
        value_name="Status_maquina"
    )
    df_grafico["Setor"] = df_grafico["Máquina"].apply(lambda x: x.split()[0])

    # 🔹 Gráficos tipo pizza por setor e turno
    for setor in setores.keys():
        st.subheader(f"📌 {setor}")
        for t in sorted(df_grafico["Turno"].unique()):
            df_setor_turno = df_grafico[(df_grafico["Setor"] == setor) & (df_grafico["Turno"] == t)]
            if not df_setor_turno.empty:
                st.markdown(f"**Turno {t}**")
                fig = px.pie(
                    df_setor_turno,
                    names="Status_maquina",
                    color="Líder",
                    title=f"Status das máquinas do setor {setor} - Turno {t}",
                    hole=0.4
                )
                st.plotly_chart(fig, use_container_width=True)

    # 🔹 Gráfico geral de barras agrupadas
    st.subheader("📊 Visão Geral - Todas as Máquinas")
    fig_bar = px.bar(
        df_grafico,
        x="Setor",
        y="Máquina",
        color="Status_maquina",
        barmode="group",
        text="Líder",
        hover_data=["Turno", "Líder", "Máquina"],
        title="Status de todas as máquinas por setor"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ---- Tabela opcional ----
    st.subheader("📋 Últimos Registros")
    if st.button("Ver últimos registros"):
        st.dataframe(df.tail(10), use_container_width=True)

except FileNotFoundError:
    st.info("Nenhum registro enviado ainda.")
