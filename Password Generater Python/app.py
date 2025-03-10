# Password Strength Meter 

import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    length = len(password)
    
    # Length checking section
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
        
    # Characters checking section
    checks = {
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'digit': r'\d',
        'special': r'[!@#$%^&*]'
    }
    
    for name, pattern in checks.items():
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(f"❌ Missing {name} characters")
    
    # Common password detecting 
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "password123"]
    if password.lower() in common_passwords:
        score = max(0, score - 2)
        feedback.append("⚠️ Warning: This is a commonly used password")
    
    # Maximum Score
    return min(score, 5), feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    password += random.choices(characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)

# Streamlit UI Section
st.set_page_config(page_icon="🔐", page_title="Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter and Generator")
st.write("### Check and improve your password security")

with st.expander("🔧 Password Generator", expanded=True):
    if st.button("Generate Strong Password"):
        generated_pw = generate_strong_password()
        st.session_state.generated_pw = generated_pw
    if 'generated_pw' in st.session_state:
        st.code(st.session_state.generated_pw)

password = st.text_input("Enter password to analyze:", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    # Strength Checker
    strength_level = "Weak" if score < 3 else "Moderate" if score < 5 else "Strong"
    color = "#ff0000" if strength_level == "Weak" else "#ffa500" if strength_level == "Moderate" else "#00ff00"
    
    st.markdown(f"""
    <div style="height: 20px; background: {color}; 
                width: {score*20}%; border-radius: 5px; 
                margin: 10px 0; transition: all 0.3s ease;">
    </div>
    <h3>Security Rating: {strength_level} ({score}/5)</h3>
    """, unsafe_allow_html=True)
    
    # Feedback section
    if feedback:
        st.write("### Improvement Suggestions:")
        for msg in feedback:
            st.write(msg)

# Instructions section
st.sidebar.header("🔍 Password Requirements")
st.sidebar.markdown("""
- Minimum 8 characters (12+ recommended)
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&*)
- Not a commonly used password
""")

st.sidebar.header("⚙️ How It Works")
st.sidebar.markdown("""
1. Enter your password
2. Get instant security analysis
3. Review improvement suggestions
4. Generate new passwords if needed
""")