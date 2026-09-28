import streamlit as st
st.title("BMI")
n1=st.number_input("weight in kg:",min_value=0)
print(n1)
n2=st.number_input("height in cm:",min_value=0)
print(n2)
bt=st.button("BMI")
if bt:

    result = n1 / ((n2 / 100) ** 2)
    if result<18.5:

        st.info("underweight")
    elif 18.5 < result <= 24.9:
        st.success("healthy")
    elif 25<result<29.9:
        st.warning("overweight")
    elif result>30:
        st.error("obese")