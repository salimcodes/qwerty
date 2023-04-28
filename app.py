import streamlit as st
import mindsdb_sdk
import pandas as pd

# Connecting to MindsDB
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login='salimoyinlola@gmail.com', password='+85758008Eg')
project = server.get_project("mindsdb")
model = project.list_models()
print(model)





import streamlit as st
import mindsdb_sdk
import pandas as pd

# Connecting to MindsDB
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login='user_name', password='my_password')
project = server.get_project("mindsdb")
model = project.list_models()[1]


# Web App title
st.title("MindsDB Loan Default Prediction")
st.subheader("Enter the Following Details")

# Retrieving Input from user
gender=st.sidebar.selectbox("Gender", options=["Male", "Female"])
loan_type=st.sidebar.selectbox("Loan Type", options=["type1", "type2", "type3"])
credit_worthiness=st.sidebar.selectbox("Credit Worthiness", options=["l1", "l2"])
open_credit=st.sidebar.selectbox("Open Credit", options=["opc", "npc"])
neg_ammortization=st.sidebar.selectbox("Neg Ammortization", options=["not_meg", "neg_amm"])
lump_sum_payment = st.sidebar.selectbox("Lump Sum Payment", options=["not_lpsm", "lpsm"])
age = st.sidebar.selectbox("Age", ['25-34', '55-64', '35-44', '45-54', '65-74', '>74', '<25'])
credit_score = st.sidebar.number_input("Credit Score", min_value=0, max_value=1000)
occupancy_type = st.sidebar.selectbox("Occupancy Type", options=['pr', 'sr', 'ir'])
secured_by = st.sidebar.radio("Secured By", options=["home", "land"])
loan_limit=st.sidebar.radio("Loan Limit", options=["cf", "ncf"])
approv_in_adv=st.sidebar.radio("Approve in Advance",options=["pre", "nopre"])
loan_purpose=st.selectbox("Loan Purpose", options=["p1", "p2", "p3", "p4"])
business_or_commercial= st.selectbox("Business or Commercial", options=["nob/c", "b/c"])
loan_amount=st.number_input("Loan Amount", min_value=50000.00, max_value=5000000.00)
term=st.slider("Loan Term", min_value=90, max_value=360, step=2)
interest_only = st.selectbox("Interest Only", options=["not_int", "int_only"])
property_value=st.number_input("Property Value", min_value=0.00, max_value=20e6)
income = st.number_input("Income", min_value=0.0, max_value=1e6)
construction_type = st.selectbox("Construction Type", options=["sb", "mh"])
total_units = st.selectbox("Total Units", options=['1U', '2U', '3U', '4U'])
credit_type = st.selectbox("Credit Type", options=['EXP', 'EQUI', 'CRIF', 'CIB'])
co_applicant_credit_type = st.selectbox("Co-Applicant Credit Type", options=['CIB', 'EXP'])
region = st.selectbox("Region", options=['south', 'North', 'central', 'North-East'])

# Create a dictionary to store value
variables = {
    "gender": gender,
    "loan_type": loan_type,
    "credit_worthiness": credit_worthiness,
    "open_credit": open_credit,
    "neg_ammortization": neg_ammortization,
    "lump_sum_payment": lump_sum_payment,
    "age": age,
    "credit_score": credit_score,
    "occupancy_type": occupancy_type,
    "secured_by": secured_by,
    "loan_limit": loan_limit,
    "approv_in_adv": approv_in_adv,
    "loan_purpose": loan_purpose,
    "business_or_commercial": business_or_commercial,
    "loan_amount": loan_amount,
    "term": term,
    "interest_only": interest_only,
    "property_value": property_value,
    "income": income,
    "construction_type": construction_type,
    "total_units": total_units,
    "credit_type": credit_type,
    "co_applicant_credit_type": co_applicant_credit_type,
    "region": region
}

# Convert result to Dataframe
result = pd.DataFrame(variables, index=[0])

# Handler to predict the result
if st.button("Predict"):
    if model.predict(result)["status"].loc[0] == 1:
        st.warning(f"This customer is at risk of defaulting on their loan. Please contact them to discuss their account😥.")
    st.success(f"This customer is not at risk of defaulting on their loan at this time.😉")
