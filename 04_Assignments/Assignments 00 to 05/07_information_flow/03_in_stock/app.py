# In Stock
import streamlit as st

# Page layout
st.set_page_config(page_title="Sophia's Fruit Store", page_icon="🍎")
st.title("Sophia's Fruit Store")

# Initialize session state
if "stock" not in st.session_state:
    st.session_state.stock = None
if "fruit" not in st.session_state:
    st.session_state.fruit = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to check fruit stock
def num_in_stock(fruit):
    fruit = fruit.lower().strip()
    if fruit == "apple":
        return 2
    elif fruit == "banana":
        return 4
    elif fruit == "mango":
        return 1000
    else:
        return 0

# App description
st.write("""
### What This App Does
Want to know if Sophia has your favorite fruit in stock?
- Type the **fruit name** in the sidebar.
- Click **'Check Stock'** to see how many are available.
- Use **'Clear'** to reset everything.
""")

# Sidebar for input
with st.sidebar:
    st.header("Check Fruit Stock")
    fruit = st.text_input("Enter a fruit name:", value="pear")
    check_button = st.button("Check Stock")
    clear_button = st.button("Clear")

# Handle Check button
if check_button:
    st.session_state.fruit = fruit
    st.session_state.stock = num_in_stock(fruit)
    st.session_state.results_shown = True
    st.write("### Stock Result")
    if st.session_state.stock == 0:
        st.error(f"🚫 Sorry! '{fruit}' is not in stock.")
    else:
        st.success(f"'{fruit}' is in stock! Quantity: **{st.session_state.stock}**")

# Clear button
if clear_button:
    st.session_state.stock = None
    st.session_state.fruit = ""
    st.session_state.results_shown = False
    st.rerun()

# Show results if already checked
if st.session_state.results_shown and not check_button:
    st.write("### Stock Result")
    if st.session_state.stock == 0:
        st.error(f"🚫 Sorry! '{st.session_state.fruit}' is not in stock.")
    else:
        st.success(f"'{st.session_state.fruit}' is in stock! Quantity: **{st.session_state.stock}**")