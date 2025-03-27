# Celsuis to Fahrenheit
import streamlit as st

# Page layout
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")
st.title("🌡️ Temperature Converter")
st.sidebar.title("🌡️ How to Use (Instructions)")
st.sidebar.info(
        """
        1. Enter the temperature in Celsius in the text box.
        2. Click the "Convert" button.
        3. The temperature in Fahrenheit will be displayed.
        """
    )

st.text_input("Enter temperature in Celsius:", key="celsius")
celsius = st.session_state.celsius
st.button("Convert", key="convert")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
if st.session_state.convert:
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    st.write(f"{celsius}°C is {fahrenheit}°F")
