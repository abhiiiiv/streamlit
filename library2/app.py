from library_db import BookListCreateRetrieveUpdateDelete
import streamlit as st
b=BookListCreateRetrieveUpdateDelete()
tab1,tab2,tab3,tab4,tab5=st.tabs(["add","view","retreive","delete","update"])
with tab1:
    t = st.text_input("Title")
    a = st.text_input("Author")
    p = st.number_input("price")
    pages = st.number_input("pages:")
    lang = st.text_input("language")
    btn = st.button("add book")
    if btn:
        b.create(t,a,p,pages,lang)
