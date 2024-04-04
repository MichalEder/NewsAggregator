import streamlit as st
from functions.database_interactions import read_resource_for_web

st.set_page_config(layout="wide")


def load_data():
    zahranicni = read_resource_for_web('zahranicni', 'idnes')
    domaci = read_resource_for_web('domaci', 'idnes')
    ekonomika = read_resource_for_web('ekonomika', 'idnes')
    return zahranicni, domaci, ekonomika

def display_article(article):
    st.subheader(article[1])
    st.markdown(f"[Link]({article[3]}) {article[4].split('T')[0]}")
    st.write(f"{article[5]}")

zahranicni, domaci, ekonomika = load_data()

st.title('Idnes.cz')

with st.expander('Zahraniční'):
    for article in zahranicni:
        display_article(article)
with st.expander('Domácí'):
    for article in domaci:
        display_article(article)
with st.expander('Eknomika'):
    for article in ekonomika:
        display_article(article)

