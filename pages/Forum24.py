import streamlit as st
from functions.database_interactions import read_resource_for_web

st.set_page_config(layout="wide")


zahranicni = read_resource_for_web('zahraničí', 'forum24')
domaci = read_resource_for_web('domácí', 'forum24')

st.title('Forum24.cz')


with st.expander('Zahraniční'):
    for articel in zahranicni:
        st.subheader(articel[1])
        st.markdown(f"[Link]({articel[5]}) {articel[3]}")
        st.write(f"{articel[4]}")
with st.expander('Domácí'):
    for articel in domaci:
        st.subheader(articel[1])
        st.markdown(f"[Link]({articel[5]}) {articel[3]}")
        st.write(f"{articel[4]}")