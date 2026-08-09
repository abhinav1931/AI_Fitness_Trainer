import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) instantly.")

st.divider()

# -----------------------------
# User Input
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

with col2:
    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=250,
        value=70
    )

st.divider()

# -----------------------------
# Calculate BMI
# -----------------------------
if st.button("📊 Calculate BMI"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI: **{bmi:.2f}**")

    # BMI Category
    if bmi < 18.5:
        category = "🔵 Underweight"
        advice = """
- Increase calorie intake
- Eat protein-rich foods
- Strength train 3–5 days/week
- Get enough sleep
"""
    elif bmi < 25:
        category = "🟢 Normal Weight"
        advice = """
- Maintain a balanced diet
- Continue regular exercise
- Stay hydrated
- Sleep 7–8 hours
"""
    elif bmi < 30:
        category = "🟠 Overweight"
        advice = """
- Reduce processed foods
- Walk 8,000–10,000 steps daily
- Increase protein intake
- Start resistance training
"""
    else:
        category = "🔴 Obese"
        advice = """
- Consult a healthcare professional
- Follow a calorie-controlled diet
- Exercise regularly
- Track your progress weekly
"""

    st.success(f"Category: {category}")

    st.markdown("### 💡 Health Recommendations")
    st.markdown(advice)

    st.divider()

    st.info(
        "⚠️ BMI is only a general health indicator. "
        "It does not account for muscle mass, age, or body composition."
    )
    