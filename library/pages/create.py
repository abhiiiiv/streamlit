import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Add new book record")

from datetime import date
t=st.text_input("Title")
a=st.text_input("Author")
p=st.number_input("price")
pages=st.number_input("pages:")
lang=st.text_input("language")
btn=st.button("add book")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(t,a,p,pages,lang)

