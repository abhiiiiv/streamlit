import streamlit as st
from datetime import date
st.title("Srudent Registration form")
name=st.text_input("Name")
age=st.number_input("Age")
place=st.date_input("DOB",min_value=date(1990,1,1),max_value=date.today(),value=date(2000,1,1))
gender=st.radio("Gender",["Male","Female"])
qual=st.selectbox("Courses",["python","java","dotnet","testing"])
bt=st.button("Register")
if bt:
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",place)
    st.write("Gender:",gender)
    st.write("course:",qual)