import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("read")
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
print("hello")
print(records)