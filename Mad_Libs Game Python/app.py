import streamlit as st

# App Configuration
st.set_page_config(page_icon="✨", page_title="Mad Libs Game")
st.header("🎭 Welcome to Mad Libs Game!")
st.write("💪 Are you ready to create a hilarious story? Fill in the blanks below!")

# Input Section
with st.form("madlibs_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name:", placeholder="e.g., Alex")
        profession = st.text_input("Your Profession:", placeholder="e.g., Astronaut")
        food = st.text_input("Favorite Food:", placeholder="e.g., Pizza")
    
    with col2:
        city = st.text_input("Your City:", placeholder="e.g., New York")
        animal = st.text_input("Favorite Animal:", placeholder="e.g., Panda")
        mood = st.selectbox("Your Mood:", ["Happy", "Excited", "Curious", "Surprised"])
    
    # Submit Button
    if st.form_submit_button("✨ Generate Story"):
        if all([name, profession, food, city, animal]):
            # Story with fields
            story = f"""
            One day, **{name}**, a passionate **{profession}** from **{city}**, decided to try something new for dinner.
            Instead of the usual fare, **{name}** ordered a delicious **{food}** at a local restaurant. As the savory flavors danced on their tongue,
            an unexpected visitor—a friendly **{animal}**—joined the fun. **{name}** felt **{mood.lower()}** and realized that sometimes,
            the best moments in life come with a side of adventure. 🎉
            """
            
            # Story displayed here
            st.balloons()
            st.subheader("🌟 Your Mad Libs Story:")
            st.write(story)
            
            st.sidebar(
            
            )