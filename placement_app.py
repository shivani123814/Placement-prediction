import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Page title
st.set_page_config(page_title="Placement Prediction System")

st.title("🎓 Placement Prediction System")
st.write("Enter student details to predict placement status")

# Input fields
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ", min_value=0, max_value=200, step=1)
profile_score = st.number_input("Enter Profile Score", min_value=0, max_value=100, step=1)

# Prediction button
if st.button("Predict Placement"):
     # Create input array
    input_data = np.array([[cgpa, iq, profile_score]])
    
    # Predict
    prediction = model.predict(input_data)
    
    # Output result
    if prediction[0] == 1:
        st.success("✅ Student is Likely to be Placed")
    else:
        st.error("❌ Student is Not Likely to be Placed")