import streamlit as st
from functions.database_interactions import read_resource_for_web
from functions.display_functions import display_article_novinky as da

st.set_page_config(layout="wide")


def load_data():
    zahranicni = read_resource_for_web('zahranicni', 'novinky')
    domaci = read_resource_for_web('domaci', 'novinky')
    krimi = read_resource_for_web('krimi', 'novinky')
    return zahranicni, domaci, krimi


zahranicni, domaci, krimi = load_data()

st.title('Novinky.cz')


with st.expander('Zahraniční'):
    for article in zahranicni:
        da(article)
with st.expander('Domácí'):
    for article in domaci:
        da(article)
with st.expander('Krimi'):
    for article in krimi:
        da(article)

