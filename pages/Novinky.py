import streamlit as st
from functions.database_interactions import read_resource_for_web

st.set_page_config(layout="wide")

@st.cache
def load_data():
    zahranicni = read_resource_for_web('zahranicni', 'novinky')
    domaci = read_resource_for_web('domaci', 'novinky')
    krimi = read_resource_for_web('krimi', 'novinky')
    return zahranicni, domaci, krimi

def display_article(article):
    st.subheader(article[1])
    st.markdown(f"[Link]({article[4]}) {article[6].split(' ')[0]}")
    st.write(f"{article[3]} ")

zahranicni, domaci, krimi = load_data()

st.title('Novinky.cz')


with st.expander('Zahraniční'):
    for article in zahranicni:
        display_article(article)
with st.expander('Domácí'):
    for article in domaci:
        display_article(article)
with st.expander('Krimi'):
    for article in krimi:
        display_article(article)

