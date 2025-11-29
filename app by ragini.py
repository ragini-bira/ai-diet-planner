import streamlit as st
import datetime

st.set_page_config(page_title="AI Diet Planner", page_icon="🍎", layout="centered")

# ---------------------------------
#  MAIN APP DIRECT SCREEN
# ---------------------------------

st.title("🍎 AI Diet Planner")
st.subheader("Smart Diet Recommendation System")

st.write("Just enter your basic details and get your personalized diet plan instantly!")

age = st.number_input("Enter your Age", min_value=1, max_value=120)
weight = st.number_input("Enter your Weight (kg)", min_value=10, max_value=300)
height = st.number_input("Enter your Height (cm)", min_value=10, max_value=250)

activity = st.selectbox("Activity Level", 
                        ["Sedentary", "Light Active", "Moderately Active", "Very Active"])

goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])

if st.button("Generate Diet Plan"):
    st.success("✔ Personalized Diet Plan Generated!")

    if goal == "Weight Loss":
        st.write("""
        **Breakfast:** Oats + Fruits  
        **Lunch:** Roti + Dal + Salad  
        **Dinner:** Soup + Veg Sabji  
        **Snacks:** Fruits / Dry fruits  
        """)
    elif goal == "Weight Gain":
        st.write("""
        **Breakfast:** Peanut Butter Bread + Banana  
        **Lunch:** Rice + Paneer + Ghee  
        **Dinner:** Dal Khichdi + Curd  
        **Snacks:** Milkshake + Nuts  
        """)
    else:
        st.write("""
        **Breakfast:** Poha/Upma  
        **Lunch:** Balanced Roti + Dal + Veg + Rice  
        **Dinner:** Light Roti + Veg  
        **Snacks:** Fruit Bowl  
        """)

st.info("✨ No login required. App is now ready for college presentation!")
