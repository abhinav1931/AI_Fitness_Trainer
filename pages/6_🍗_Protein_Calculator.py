import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Protein Calculator",
    page_icon="🍗",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🍗 Daily Protein Calculator")
st.write("Calculate your daily protein requirement based on your fitness goal.")

st.divider()

# -----------------------------
# User Input
# -----------------------------
weight = st.number_input(
    "Weight (kg)",
    min_value=20,
    max_value=250,
    value=70
)

goal = st.selectbox(
    "Fitness Goal",
    [
        "Muscle Gain",
        "Fat Loss",
        "Maintenance"
    ]
)

meals = st.slider(
    "Meals Per Day",
    min_value=3,
    max_value=6,
    value=4
)

st.divider()

# -----------------------------
# Calculate
# -----------------------------
if st.button("🍗 Calculate Protein"):

    if goal == "Muscle Gain":
        protein_per_kg = 2.2

    elif goal == "Fat Loss":
        protein_per_kg = 2.0

    else:
        protein_per_kg = 1.6

    total_protein = round(weight * protein_per_kg)
    protein_per_meal = round(total_protein / meals)
    water = round(weight * 35)   # ml/day

    st.subheader("📊 Your Daily Nutrition")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🍗 Protein", f"{total_protein} g/day")

    with col2:
        st.metric("🍽️ Per Meal", f"{protein_per_meal} g")

    with col3:
        st.metric("💧 Water", f"{water/1000:.1f} L/day")

    st.divider()

    st.markdown("## 🍗 Example Protein Sources")

    protein_table = {
        "Food": [
            "Chicken Breast (100g)",
            "Eggs (1 whole)",
            "Paneer (100g)",
            "Greek Yogurt (100g)",
            "Milk (250ml)",
            "Whey Protein (1 Scoop)",
            "Soya Chunks (100g)"
        ],
        "Protein": [
            "31 g",
            "6 g",
            "18 g",
            "10 g",
            "8 g",
            "24 g",
            "52 g"
        ]
    }

    st.table(protein_table)

    st.divider()

    st.markdown("## 💡 Recommendations")

    st.markdown(f"""
- Aim for **{total_protein} g** protein every day.
- Split protein into **{meals} meals**.
- Consume approximately **{protein_per_meal} g** protein per meal.
- Drink at least **{water/1000:.1f} liters** of water daily.
- Include high-quality protein sources in every meal.
- Combine protein intake with resistance training for best results.
""")

    st.success("✅ Protein calculation completed successfully!")