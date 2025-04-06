# Pop up show
import streamlit as st

# Page layout
st.set_page_config(page_title="Fruit Shop Calculator")
st.title("Fruit Shop Calculator")

# Dictionary of fruits and their prices
FRUITS = {'apple': 1.5, 'banana': 50, 'watermalon': 80, 'kiwi': 1, 'cherry': 1.5, 'mango': 5}

# Initialize session state to store quantities
if "quantities" not in st.session_state:
    st.session_state.quantities = {fruit: 0 for fruit in FRUITS}

# Explanation of the program (in the main area)
st.write("""
### What This Program Does
This program helps you calculate the total cost of fruits you want to buy from a pop-up shop.
- The available fruits and their prices are listed below.
- Enter the quantity for each fruit in the sidebar.
- Click 'Calculate Total' to see the breakdown and total cost.
- Click 'Clear Quantities' to start over.
""")

# Display the fruit prices
st.write("### Available Fruits and Prices")
for fruit, price in FRUITS.items():
    st.write(f"{fruit.capitalize()}: ${price}")

# Add quantity inputs to the sidebar
with st.sidebar:
    st.header("Select Quantities")
    for fruit in FRUITS:
        st.session_state.quantities[fruit] = st.number_input(
            f"How many {fruit} do you want?",
            min_value=0,
            value=st.session_state.quantities[fruit],
            step=1,
            key=f"quantity_{fruit}"
        )
    calculate_button = st.button("Calculate Total")
    clear_button = st.button("Clear Quantities")

# Handle the calculate button
if calculate_button:
    total_cost = 0
    st.write("### Purchase Breakdown")
    for fruit in FRUITS:
        quantity = st.session_state.quantities[fruit]
        if quantity > 0:  # Only show fruits with non-zero quantities
            price = FRUITS[fruit]
            cost = price * quantity
            total_cost += cost
            st.success(f"{fruit.capitalize()}: {quantity} × ${price} = ${cost}")
    
    if total_cost == 0:
        st.warning("You haven't selected any fruits.")
    else:
        st.success(f"Your total is ${total_cost}")

# Handle the clear button
if clear_button:
    st.session_state.quantities = {fruit: 0 for fruit in FRUITS}
    st.rerun()