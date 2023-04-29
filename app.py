import streamlit as st
import mindsdb_sdk
import pandas as pd

# Connecting to MindsDB
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login='salimoyinlola@gmail.com', password='')
project = server.get_project("mindsdb")
model = project.list_models()[4] #Selecting the model to use. The index 4 is used because this is the fifth model in the list of models


# Web App title
st.title("QWERTY Churn Predict")
st.subheader("A Machine Learning App that predicts which customers are likely to stop using a bank")
st.subheader("Enter the Following Details")

# Retrieving Input from user
credit_score = st.sidebar.slider("Credit Score", min_value=350, max_value=850)
country = st.sidebar.radio("Country of Residence", options=["France", "Spain", "Germany"], horizontal=True)
gender = st.sidebar.radio("Gender", options= ["Male", "Female"], horizontal=True)
age = st.sidebar.slider("Age", min_value=18, max_value=100)
tenure = st.sidebar.slider("From how many years he/she is having bank acc in ABC Bank", min_value=0, max_value=10)
balance = st.sidebar.slider("Account Balance", min_value=0, max_value=250000)
products_number = st.sidebar.slider("Number of Products", min_value=1, max_value=4)
credit_card = st.sidebar.slider("Does the customer have a credit card? 0 for no, 1 for yes", min_value=0, max_value=1)
active_member = st.sidebar.slider("Is the customer an active member? 0 for no, 1 for yes", min_value=0, max_value=1)

# Create a dictionary to store value
variables = {
    "credit_score": credit_score,
    "country": country,
    "gender": gender,
    "age": age,
    "tenure": tenure,
    "balance": balance,
    "products_number": products_number,
    "credit_card": credit_card,
    "active_member": active_member
}

# Convert result to Dataframe
result = pd.DataFrame(variables, index=[0])


# Handler to predict the result
if st.button("Predict"):
    if model.predict(result)["churn"].loc[0] == 1:
        st.write(f"This customer is likely to stop using the bank. Please contact them to discuss their account and how they feel about the bank.")
    else:
        st.success(f"This customer is not likely to stop using the bank!")







