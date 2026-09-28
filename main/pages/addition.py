import streamlit as st
st.title("Addition")
n1=st.number_input("n1:",min_value=0)
print(n1)
n2=st.number_input("n2:",min_value=0)
print(n2)
bt=st.button("Add")
if bt:
    result=n1+n2
    print(result)
    st.write("sum",result)