import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('placement.pkl', 'rb'))

# Page settings
st.set_page_config(page_title="Package Prediction App")

# Title
st.title("🎓 Student Package Prediction System")

st.write("Enter CGPA to predict expected placement package")

# Input
cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

# Prediction
if st.button("Predict Package"):

    # Convert input into array
    input_data = np.array([[cgpa]])

    # Predict package
    prediction = model.predict(input_data)

    # Show output
    st.success(f"Expected Package: {prediction[0]:.2f} LPA")
