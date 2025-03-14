import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("student_score_model.pkl")

# Streamlit UI
st.title("🎓 Student Score Prediction System")
st.write("Enter student details to predict the final grade (G3)")

# Input fields
G1 = st.number_input("G1 (First Term Grade)", min_value=0, max_value=20, value=10)
G2 = st.number_input("G2 (Second Term Grade)", min_value=0, max_value=20, value=10)
absences = st.number_input("Absences (Number of Absences)", min_value=0, max_value=100, value=5)
age = st.number_input("Age", min_value=15, max_value=22, value=18)
romantic = st.selectbox("In a Romantic Relationship?", ["No", "Yes"])
famrel = st.slider("Family Relationship Quality (1-5)", min_value=1, max_value=5, value=3)

# Process input data
romantic = 1 if romantic == "Yes" else 0
input_data = pd.DataFrame([[G2, absences, G1, age, romantic, famrel]],
                          columns=["G2", "absences", "G1", "age", "romantic", "famrel"])

# Prediction button
if st.button("Predict Score"):
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Final Grade (G3): {round(prediction[0], 2)}")
