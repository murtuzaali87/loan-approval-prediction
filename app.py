import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("loan_approval_model.pkl")

# Page settings
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Loan Approval Prediction")
st.write("Enter the applicant details below to predict loan approval.")

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Column 1
with col1:
    Applicant_Income = st.number_input("Applicant Income")
    
    Age = st.number_input(
        "Age",
        min_value=18,
        max_value=100
    )
    
    Credit_Score = st.number_input(
        "Credit Score",
        min_value=0
    )
    
    Savings = st.number_input("Savings")
    
    Loan_Term = st.number_input("Loan Term")

    Education_Level = st.selectbox(
        "Education Level",
        ["Not Graduate", "Graduate"]
    )


# Column 2
with col2:
    Coapplicant_Income = st.number_input("Coapplicant Income")
    
    Marital_Status = st.selectbox(
        "Marital Status",
        ["Married", "Single"]
    )
    
    Existing_Loans = st.number_input(
        "Existing Loans",
        min_value=0
    )
    
    Collateral_Value = st.number_input("Collateral Value")
    
    Loan_Purpose = st.selectbox(
        "Loan Purpose",
        ["Personal", "Car", "Business", "Home", "Education"]
    )
    
    Gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )


# Column 3
with col3:
    Employment_Status = st.selectbox(
        "Employment Status",
        ["Salaried", "Self-employed", "Contract", "Unemployed"]
    )
    
    Dependents = st.number_input(
        "Dependents",
        min_value=0
    )
    
    DTI_Ratio = st.number_input("DTI Ratio")
    
    Loan_Amount = st.number_input("Loan Amount")
    
    Property_Area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )
    
    Employer_Category = st.selectbox(
        "Employer Category",
        ["Private", "Government", "Unemployed", "MNC", "Business"]
    )


# Prediction button
st.write("")

if st.button("🔮 Predict Loan Approval", use_container_width=True):

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
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
