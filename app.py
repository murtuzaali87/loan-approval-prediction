import streamlit as st
import joblib
import pandas as pd

st.title("Loan Approval Prediction")

model = joblib.load("loan_approval_model.pkl")

st.write("Enter Applicant Details")

Applicant_Income = st.number_input("Applicant Income")
Coapplicant_Income = st.number_input("Coapplicant Income")

Employment_Status = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-employed", "Contract", "Unemployed"]
)

Age = st.number_input("Age", min_value=18, max_value=100)

Marital_Status = st.selectbox(
    "Marital Status",
    ["Married", "Single"]
)

Dependents = st.number_input("Dependents", min_value=0)

Credit_Score = st.number_input("Credit Score", min_value=0)

Existing_Loans = st.number_input("Existing Loans", min_value=0)

DTI_Ratio = st.number_input("DTI Ratio")

Savings = st.number_input("Savings")

Collateral_Value = st.number_input("Collateral Value")

Loan_Amount = st.number_input("Loan Amount")

Loan_Term = st.number_input("Loan Term")

Loan_Purpose = st.selectbox(
    "Loan Purpose",
    ["Personal", "Car", "Business", "Home", "Education"]
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

Education_Level = st.selectbox(
    "Education Level",
    ["Not Graduate", "Graduate"]
)

Gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

Employer_Category = st.selectbox(
    "Employer Category",
    ["Private", "Government", "Unemployed", "MNC", "Business"]
)

if st.button("Predict Loan Approval"):

    input_data = pd.DataFrame([{
        "Applicant_Income": Applicant_Income,
        "Coapplicant_Income": Coapplicant_Income,
        "Employment_Status": Employment_Status,
        "Age": Age,
        "Marital_Status": Marital_Status,
        "Dependents": Dependents,
        "Credit_Score": Credit_Score,
        "Existing_Loans": Existing_Loans,
        "DTI_Ratio": DTI_Ratio,
        "Savings": Savings,
        "Collateral_Value": Collateral_Value,
        "Loan_Amount": Loan_Amount,
        "Loan_Term": Loan_Term,
        "Loan_Purpose": Loan_Purpose,
        "Property_Area": Property_Area,
        "Education_Level": Education_Level,
        "Gender": Gender,
        "Employer_Category": Employer_Category
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")