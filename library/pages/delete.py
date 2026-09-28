import streamlit as st
from streamlit.elements.widgets import number_input

from library_db import BookListCreateRetrieveUpdateDelete

st.title("delete")
id=st.number_input("Enter id:")
btn=st.button("delete:")
if btn:

    b=BookListCreateRetrieveUpdateDelete()
    b.delete(id)