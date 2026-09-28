import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("retrive")
i=st.number_input("enter id:")
btn=st.button("retrieve")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    records=b.retrieve(i)
    print(records)