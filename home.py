
import pandas as pd
import streamlit as st
import joblib

def run_home():
    st.image('photo.jpg', width=300,use_column_width=True)
    # Load the pre-trained model
    model = joblib.load('best_model.pkl')

    # Load other necessary data
    Brand = joblib.load('Brand.pkl')
    Model = joblib.load('Model.pkl')
    Body = joblib.load('Body.pkl')
    Color = joblib.load('Color.pkl')
    Fuel = joblib.load('Fuel.pkl')
    Kilometers = joblib.load('Kilometers.pkl')
    Engine = joblib.load('Engine.pkl')
    Transmission = joblib.load('Transmission.pkl')
    Gov = joblib.load('Gov.pkl')
    Year = joblib.load('Year.pkl')

    # Streamlit app
    st.title("Used Car Price Prediction App")
    st.info("Easy App for Guess the car price")

    # User input options
    
    Brand_inputs = st.selectbox('Brand ', Brand)
   # Modify the Model selection in home.py
    Model_inputs = st.selectbox('Model ',Model )
  # Adjust options based on Brand
    Body_inputs = st.selectbox('Body ', Body)
    Color_inputs = st.selectbox('Color ', Color)
    Fuel_inputs = st.selectbox('Fuel ', Fuel)

    Kilometers_inputs = st.slider('Select Kilometers',min_value=100,max_value=200000,value=1000)
    width_percentage = max(10, len(str(Kilometers_inputs))) * 10
    # Display the selected year with dynamically adjusted font size
    st.write("You selected :", f"<span style=\"font-size: {width_percentage}%;\">{Kilometers_inputs}</span>", 
         unsafe_allow_html=True)
    Engine_inputs = st.selectbox('Engine ', Engine)
    Transmission_inputs = st.selectbox('Transmission ', Transmission)
    Gov_inputs = st.selectbox('Gov ', Gov)
    Year_inputs = st.slider("Select a year", min_value=1970, max_value=2023, value=2000)
    

# Display the selected year with dynamically adjusted font size
    st.write("You selected :", f"<span style=\"font-size: {width_percentage}%;\">{Year_inputs}</span>", 
         unsafe_allow_html=True)

    # Collect user input
    user_input = {
        'Brand': Brand_inputs,
        'Model': Model_inputs,
        'Body': Body_inputs,
        'Color': Color_inputs,
        'Year': Year_inputs,
        'Fuel': Fuel_inputs,
        'Kilometers': Kilometers_inputs,
        'Engine': Engine_inputs,
        'Transmission': Transmission_inputs,
        'Gov': Gov_inputs
    }

    # Convert user input to DataFrame
    user_df = pd.DataFrame([user_input])

    # Make predictions
    prediction = model.predict(user_df)
    st.write(f'Predicted Price: {prediction[0]:,.0f} EGP')
