import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🔥",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🔥 Daily Calorie Calculator")
st.write("Calculate your daily calorie needs using the Mifflin-St Jeor Equation.")

st.divider()

# -----------------------------
# User Input
# -----------------------------
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)

height = st.number_input(
    "Height (cm)",
    min_value=100,
    max_value=250,
    value=170
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20,
    max_value=250,
    value=70
)

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary (Little or no exercise)",
        "Lightly Active (1–3 days/week)",
        "Moderately Active (3–5 days/week)",
        "Very Active (6–7 days/week)",
        "Extra Active (Twice/day or physical job)"
    ]
)

st.divider()

# -----------------------------
# Calculate Button
# -----------------------------
if st.button("🔥 Calculate Calories"):

    # BMR
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Activity Multiplier
    if activity.startswith("Sedentary"):
        multiplier = 1.2
    elif activity.startswith("Lightly"):
        multiplier = 1.375
    elif activity.startswith("Moderately"):
        multiplier = 1.55
    elif activity.startswith("Very"):
        multiplier = 1.725
    else:
        multiplier = 1.9

    maintenance = round(bmr * multiplier)
    fat_loss = maintenance - 500
    muscle_gain = maintenance + 300

    # -----------------------------
    # Results
    # -----------------------------
    st.subheader("📊 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔥 Maintenance", f"{maintenance} kcal")

    with col2:
        st.metric("📉 Fat Loss", f"{fat_loss} kcal")

    with col3:
        st.metric("📈 Muscle Gain", f"{muscle_gain} kcal")

    st.divider()

    st.markdown("### 💡 Recommendations")

    st.markdown(f"""
- **Maintenance:** {maintenance} kcal/day
- **Fat Loss:** {fat_loss} kcal/day
- **Muscle Gain:** {muscle_gain} kcal/day

### Tips
- Eat enough protein (1.6–2.2 g/kg body weight)
- Drink 2–3 liters of water daily
- Sleep 7–9 hours
- Strength train regularly
- Track progress every 2–4 weeks
""")

    st.info(
        "These are estimates based on the Mifflin-St Jeor Equation. "
        "Your actual calorie needs may vary."
    )