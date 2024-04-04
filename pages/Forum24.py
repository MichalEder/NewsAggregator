import streamlit as st
from functions.database_interactions import read_resource_for_web

st.set_page_config(layout="wide")

@st.cache
def load_data():
    zahranicni = read_resource_for_web('zahraničí', 'forum24')
    domaci = read_resource_for_web('domácí', 'forum24')
    return zahranicni, domaci

def display_article(article):
    st.subheader(article[1])
    st.markdown(f"**[Link]({article[5]})** - {article[3]}")
    st.write(f"{article[4]}")

zahranicni, domaci = load_data()

st.title('Forum24.cz')


with st.expander('Zahraniční'):
    for article in zahranicni:
        display_article(article)
with st.expander('Domácí'):
    for article in domaci:
        display_article(article)