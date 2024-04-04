import streamlit as st
from functions.database_interactions import read_resource_for_web
from functions.display_functions import display_article_idnes as da

st.set_page_config(layout="wide")


def load_data():
    zahranicni = read_resource_for_web('zahranicni', 'idnes')
    domaci = read_resource_for_web('domaci', 'idnes')
    ekonomika = read_resource_for_web('ekonomika', 'idnes')
    return zahranicni, domaci, ekonomika


zahranicni, domaci, ekonomika = load_data()

st.title('Idnes.cz')

with st.expander('Zahraniční'):
    for article in zahranicni:
        da(article)
with st.expander('Domácí'):
    for article in domaci:
        da(article)
with st.expander('Eknomika'):
    for article in ekonomika:
        da(article)

