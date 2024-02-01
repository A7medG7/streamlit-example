
import streamlit as st 

def run_communication():
    st.title('Created By : Ahmed Ghaniem ')
    number = st.button('Phon Number')
    if number :
        st.write('01021440967')
        
    facebook = st.button('Facebook')
    if facebook:
        st.write('https://www.facebook.com/MedOo.Ghaniem?mibextid=ZbWKwL')
    Linkedin = st.button('Linkedin')
    if Linkedin:
        st.write('https://www.linkedin.com/in/ahmed-ghanem')
    github = st.button('Github')
    if github:
        st.write('https://github.com/A7medG7')
    #st.image('photo.jpg', width=500,use_column_width=True)
