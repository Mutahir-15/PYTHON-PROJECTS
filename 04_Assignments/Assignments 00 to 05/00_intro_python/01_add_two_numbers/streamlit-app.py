# Simple Calculator
import streamlit as st

# Page Configuratioon section
set_page_config = st.set_page_config(
    page_title="Simple Calculator",
    page_icon="✏",
)
# Arithmatic functions
def calculator():
    st.title("✏ Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0, format="%d")
    num2 = st.number_input("Enter second number", value=0, format="%d")
    
    # Operation selection
    operation = st.selectbox("Select operation", ["Add +", "Subtract -", "Multiply *", "Divide /"])
    
    # Perform calculation
    result = None
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
    
    # Display results here
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    calculator()