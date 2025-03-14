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
absences = st.number_input("Absences", min_value=0, max_value=100, value=5)
age = st.number_input("Age", min_value=15, max_value=22, value=18)
romantic = st.selectbox("In a Romantic Relationship?", ["No", "Yes"])
famrel = st.slider("Family Relationship Quality (1-5)", min_value=1, max_value=5, value=3)

# Add missing features
reason = st.selectbox("Reason for Choosing School", ["Home", "Reputation", "Course", "Other"])
guardian = st.selectbox("Guardian", ["Mother", "Father", "Other"])
health = st.slider("Health Status (1-5)", min_value=1, max_value=5, value=3)
goout = st.slider("Going Out with Friends (1-5)", min_value=1, max_value=5, value=3)
Mjob = st.selectbox("Mother's Job", ["Teacher", "Health", "Services", "At_home", "Other"])
studytime = st.slider("Weekly Study Time (1-4)", min_value=1, max_value=4, value=2)
schoolsup = st.selectbox("Extra Educational Support", ["No", "Yes"])
Fedu = st.slider("Father's Education Level (0-4)", min_value=0, max_value=4, value=2)
activities = st.selectbox("Extracurricular Activities", ["No", "Yes"])
Fjob = st.selectbox("Father's Job", ["Teacher", "Health", "Services", "At_home", "Other"])
Walc = st.slider("Weekend Alcohol Consumption (1-5)", min_value=1, max_value=5, value=2)
traveltime = st.slider("Home to School Travel Time (1-4)", min_value=1, max_value=4, value=2)
Medu = st.slider("Mother's Education Level (0-4)", min_value=0, max_value=4, value=2)

# Convert categorical values to numerical (Label Encoding)
romantic = 1 if romantic == "Yes" else 0
schoolsup = 1 if schoolsup == "Yes" else 0
activities = 1 if activities == "Yes" else 0

# Convert categorical variables manually
reason_dict = {"Home": 0, "Reputation": 1, "Course": 2, "Other": 3}
guardian_dict = {"Mother": 0, "Father": 1, "Other": 2}
Mjob_dict = {"Teacher": 0, "Health": 1, "Services": 2, "At_home": 3, "Other": 4}
Fjob_dict = {"Teacher": 0, "Health": 1, "Services": 2, "At_home": 3, "Other": 4}

reason = reason_dict[reason]
guardian = guardian_dict[guardian]
Mjob = Mjob_dict[Mjob]
Fjob = Fjob_dict[Fjob]

# Create DataFrame with correct features
input_data = pd.DataFrame([[G2, absences, G1, age, romantic, famrel, reason, guardian, health, goout,
                            Mjob, studytime, schoolsup, Fedu, activities, Fjob, Walc, traveltime, Medu]],
                          columns=["G2", "absences", "G1", "age", "romantic", "famrel", "reason", "guardian", "health", 
                                   "goout", "Mjob", "studytime", "schoolsup", "Fedu", "activities", "Fjob", "Walc", 
                                   "traveltime", "Medu"])

# Prediction button
if st.button("Predict Score"):
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Final Grade (G3): {round(prediction[0], 2)}")
