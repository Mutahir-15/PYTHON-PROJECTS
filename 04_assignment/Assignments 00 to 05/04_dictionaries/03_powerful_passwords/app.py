# powerful password
import streamlit as st
from hashlib import sha256

# Page layout
st.set_page_config(page_title="Password Verifier", page_icon=":lock:")
st.title("Password Verifier")

# Stored logins (email: hashed password)
STORED_LOGINS = {
    "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
    "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # "karel"
    "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # "123!456?789"
}

# Initialize session state to store login attempts
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = []

# Function to hash a password
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Function to verify login
def login(email, stored_logins, password_to_check):
    if email not in stored_logins:
        return False
    return stored_logins[email] == hash_password(password_to_check)

# Explanation of the program (in the main area)
st.write("""
### What This Program Does
This program verifies login credentials by comparing hashed passwords.
- Select an email from the dropdown in the sidebar.
- Enter a password to check.
- Click 'Verify Login' to see if the password is correct.
- The result will be displayed below, along with a history of your login attempts.
- Click 'Clear History' to start over.
""")

# Add the input fields and buttons to the sidebar
with st.sidebar:
    st.header("Login Verification")
    
    # Email selection
    email = st.selectbox("Select an email:", list(STORED_LOGINS.keys()))
    
    # Password input
    password = st.text_input("Enter password:", type="password")
    
    # Buttons
    verify_button = st.button("Verify Login")
    clear_button = st.button("Clear History")

# verify button
if verify_button:
    if not password:
        st.error("Please enter a password.")
    else:
        result = login(email, STORED_LOGINS, password)
        st.session_state.login_attempts.append((email, password, result))
        st.write("### Latest Login Attempt")
        if result:
            st.success(f"Login successful for {email}!")
        else:
            st.warning(f"Login failed for {email}. Incorrect password.")

# clear button
if clear_button:
    st.session_state.login_attempts = []
    st.rerun()

# Display the history of login attempts
if st.session_state.login_attempts:
    st.write("### History of Login Attempts")
    for i, (email, password, result) in enumerate(st.session_state.login_attempts, 1):
        st.write(f"**Attempt {i}: {email}**")
        if result:
            st.success(f"Login successful! Password: {password}")
        else:
            st.warning(f"Login failed. Password: {password}")