import streamlit as st
from functions.database_interactions import read_resource_for_web
from pages.Idnes import display_article as da_idnes
from pages.Forum24 import display_article as da_forum24
from pages.Novinky import display_article as da_novinky


st.set_page_config(layout="wide")


st.title("For navigation use sidebar on the left")

col1,col2, col3, col4, col5 = st.columns([3,0.5,3,0.5,3])
with col1:
    st.title('Forum24.cz')
    with st.expander('Zahraniční', expanded=True):
        for article in read_resource_for_web(limit=3, section='zahraničí', table_name='forum24'):
            da_forum24(article)
    with st.expander('Domácí', expanded=True):
        for article in read_resource_for_web(limit=3, section='domácí', table_name='forum24'):
            da_forum24(article)
with col3:
    st.title('Novinky')
    with st.expander('Zahraniční', expanded=True):
        for article in read_resource_for_web(limit=3, section='zahranicni', table_name='novinky'):
            da_novinky(article)
    with st.expander('Domácí', expanded=True):
        for article in read_resource_for_web(limit=3, section='domací', table_name='novinky'):
            da_novinky(article)
    with st.expander('Krimi', expanded=True):
        for article in read_resource_for_web(limit=3, section='krimi', table_name='novinky'):
            da_novinky(article)
with col5:
    st.title('Idnes')
    with st.expander('Zahraniční', expanded=True):
        for article in read_resource_for_web(limit=3, section='zahranicni', table_name='idnes'):
            da_idnes(article)
    with st.expander('Domácí', expanded=True):
        for article in read_resource_for_web(limit=3, section='domaci', table_name='idnes'):
            da_idnes(article)
    with st.expander('Krimi', expanded=True):
        for article in read_resource_for_web(limit=3, section='ekonomika', table_name='idnes'):
            da_idnes(article)





