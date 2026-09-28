import streamlit as st
st.title("User Info")
name=st.text_input("Name")
age=st.number_input("Age")
place=st.text_input("Place")
gender=st.radio("Gender",["Male","Female"])
qual=st.selectbox("Qualification",["bba","bca","btech"])
bt=st.button("Submit")
if bt:
    st.write(name)
    st.write(age)
    st.write(place)
    st.write(gender)
    st.write(qual)