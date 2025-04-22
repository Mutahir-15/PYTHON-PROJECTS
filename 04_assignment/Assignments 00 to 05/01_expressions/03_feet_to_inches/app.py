# Feet to Inches
import streamlit as st

# Page layout
st.set_page_config(page_title='Feet to Inches', page_icon='📏')
st.title('📏 Feet to Inches')
st.sidebar.header("Instructions")
st.sidebar.info("Enter the valid feet value, inches will be calculated instantly.")

# Constant 
inches_in_foot = 12

#Input for feet
feet = st.number_input('Enter feet:', min_value=0.0, format='%f')

#Calculation
if feet > 0:
    inches = feet * inches_in_foot
    st.write(f'There are {inches_in_foot} inches in one foot.')
    st.success(f'{feet} feet is equal to {feet * inches_in_foot} inches.')
else:
    st.warning('Please enter a positive number of feet.')