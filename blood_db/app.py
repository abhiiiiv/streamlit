from blood import BookListCreateRetrieveUpdateDelete
import streamlit as st
from datetime import date
b=BookListCreateRetrieveUpdateDelete()
tab1,tab2,tab3,tab4,tab5=st.tabs(["POST","GET","GETID","PUT","DELETE"])
with tab1:
    t = st.text_input("Name")
    a = st.selectbox("Blood Group",["A+","A-","B+","B-","O+","O-","AB+","AB-"])
    p = st.text_input("Phone")

    c = st.text_input("City")
    d=st.date_input("Last Donation")
    btn = st.button("add donor")
    if btn:
        b.post(t,a,p,c,d)
with tab2:
    records = b.list()
    print("hello")
    print(records)


