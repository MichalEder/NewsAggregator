import streamlit as st


def display_article_forum24(article):
    st.subheader(article[1])
    st.markdown(f"**[Link]({article[5]})** - {article[3]}")
    st.write(f"{article[4]}")


def display_article_idnes(article):
    st.subheader(article[1])
    st.markdown(f"**[Link]({article[3]})** {article[4].split('T')[0]}")
    st.write(f"{article[5]}")


def display_article_novinky(article):
    st.subheader(article[1])
    st.markdown(f"**[Link]({article[4]})** {article[6].split(' ')[0]}")
    st.write(f"{article[3]} ")