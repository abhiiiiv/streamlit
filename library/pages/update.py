import streamlit as st
st.title("update")
from library_db import BookListCreateRetrieveUpdateDelete



t=st.text_input("Title")
a=st.text_input("Author")
p=st.number_input("price",min_value=0)
pages=st.number_input("pages:",min_value=0)
lang=st.text_input("language")
id=st.number_input("id:",min_value=0)
btn=st.button("add book")

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.update(id,t,a,p,pages,lang)