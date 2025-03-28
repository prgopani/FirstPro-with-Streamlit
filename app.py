import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('timelytics_model.pkl')

# Streamlit UI
st.title("Timelytics: Delivery Time Prediction")
st.write("Provide the order details to predict the expected delivery time.")

# Input fields
Type_of_order = st.selectbox('Type_of_order', ['Buffet', 'Drinks', 'Meal', 'Snack'])
Type_of_vehicle = st.selectbox('Type_of_vehicle', ['bicycle', 'motorcycle', 'scooter','electric_scooter'])
distance = st.number_input('Enter distance (in Km)')
Delivery_person_Age = st.number_input('Enter Delivery_person_Age (in integer)', min_value=1, max_value=100, step=1)
Delivery_person_Ratings = st.number_input('Enter Delivery_person_Ratings (0 to 5)', min_value=0, max_value=5, step=1)

# Predict Button
if st.button('Predict Delivery Time'):
    # Create input data
    input_data = pd.DataFrame({
        'Delivery_person_Age': [Delivery_person_Age],
        'Delivery_person_Ratings': [Delivery_person_Ratings],
        'distance': [distance],
        'Type_of_order': [Type_of_order],
        'Type_of_vehicle': [Type_of_vehicle]
    })
    
    # Prediction
    prediction = model.predict(input_data)
    st.success(f"Expected Delivery Time: {prediction[0]} (minutes)")
