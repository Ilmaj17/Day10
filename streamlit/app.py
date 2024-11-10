import streamlit as st
import pickle 

with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Salary Prediction App")

yoe = st.number_input("Enter years of experience: ")
hpw = st.number_input("Enter hours per week: ")


if st.button("Predict"):
    result = int(model.predict([[yoe, hpw]]))
    st.write(f"Predicted Salary: {result}")