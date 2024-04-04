import streamlit as st
from functions.database_interactions import read_resource_for_web
from functions.display_functions import display_article_forum24 as da

st.set_page_config(layout="wide")


def load_data():
    zahranicni = read_resource_for_web('zahraničí', 'forum24')
    domaci = read_resource_for_web('domácí', 'forum24')
    return zahranicni, domaci


zahranicni, domaci = load_data()

st.title('Forum24.cz')


with st.expander('Zahraniční'):
    for article in zahranicni:
        da(article)
with st.expander('Domácí'):
    for article in domaci:
        da(article)