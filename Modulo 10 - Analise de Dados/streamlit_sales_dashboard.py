import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboar de Vendas", page_icon='', layout="wide")

@st.cache_data
def load_data(nrows):
    df = pd.read_excel("supermarket_sales.xlsx", sheet_name="Sales", skiprows=3, usecols="B:R", nrows=nrows)
    df.rename(lambda x: str(x).lower(), axis=1, inplace=True)
    df["hour"] = pd.to_datetime(df["time"], format="%H:%M:%S").dt.hour
    return df


    
data_load_state = st.text("Carregando dados")
data = load_data(10000)

st.sidebar.header("Filtros")
city = st.sidebar.multiselect(
        "Selecione uma cidade",
        options=data["city"].unique(),
        default=data["city"].unique(),
        placeholder="selecione uma opção")

customer_type = st.sidebar.multiselect(
        "Selecione o tipo de cliente",
        options=data["customer_type"].unique(),
        default=data["customer_type"].unique(),
        placeholder="Selecione uma opção"
)

gender = st.sidebar.multiselect(
        "Selecione um gênero",
        options=data["gender"].unique(),
        default=data["gender"].unique(),
        placeholder="Selecione uma opção"
)

filtered_data = data.query("city == @city & customer_type == @customer_type & gender == @gender")

if filtered_data.empty:
    st.warning("Não existem dados baseados nos filtros selecionados")
    st.stop()

st.title("Dashboard de Vendadas de 2021")
st.markdown("______**______")

total_sales = filtered_data["total"].sum()
average_rating = int(filtered_data["rating"].mean())
star_rating = "⭐" * average_rating
average_sales = filtered_data["total"].mean()


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total de vendas")
    st.subheader(f"${total_sales:,.2f}")
with middle_column:
    st.subheader("Média de avaliações")
    st.subheader(f"{average_rating}{star_rating}")
with right_column:
    st.subheader("Média de vendas")
    st.subheader(f"${average_sales:,.2f}")
    
sales_by_category = filtered_data.groupby("product line")["total"].sum().reset_index().sort_values(by="total", ascending=False)
fig_sales_by_category =px.bar(
    sales_by_category,
    x="total",
    y="product line",
    orientation="h",
    title="Vendas por categoria de produto",
    labels={"total": "Total", "product line": "Categoria de produto"},
)

sales_by_hour = filtered_data.groupby("hour")["total"].sum().reset_index()
fig_sales_by_hour = px.bar(
    sales_by_hour,
    x="hour",
    y="total",
    labels={"hour": "Hora", "total": "Total"},
    title="Vendas por hora",
)

st.plotly_chart(fig_sales_by_category, use_container_width=True)
st.plotly_chart(fig_sales_by_hour, use_container_width=True)