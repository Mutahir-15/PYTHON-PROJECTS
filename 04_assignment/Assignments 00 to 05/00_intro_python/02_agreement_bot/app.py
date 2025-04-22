# Agreement Bot Web-App
import streamlit as st

#Page Configuration
st.set_page_config(
    page_title="Agreement Bot",
    page_icon="🤝",
)

st.title("🤝 Agreement Bot")

#Input Fields for agreement
partyone = st.text_input("Enter the first party name:")
partytwo = st.text_input("Enter the second party name:")
agreement_terms = st.text_area("Enter the terms of the agreement:")

if st.button("Generate Agreemnent"): 
    if partyone and partytwo and agreement_terms:
        st.write(f"Agreement between **{partyone}** and **{partytwo}**:")
        st.write(  agreement_terms)