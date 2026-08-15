import streamlit as st
from chatbot import ask_ai

st.set_page_config(
    page_title="Workout Guide",
    page_icon="🏋️"
)

st.title("🏋️ Workout Guide")
st.write("Choose your fitness level and ask workout-related questions.")

st.subheader("Select Your Level")

level = st.selectbox(
    "Training Level",
    [
        "Beginner",
        "Intermediate",
    ]
)

st.subheader("Select Muscle Group")

muscle = st.selectbox(
    "Muscle Group",
    [
        "Chest",
        "Back",
        "Shoulders",
        "Arms",
        "Legs",
    ]
)

if st.button("🔥 Generate Workout Plan"):

    question = f"Give me a {level.lower()} {muscle.lower()} workout."

    try:
        answer, sources = ask_ai(question)

        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
            padding:30px;
            border-radius:20px;
            color:white;
            box-shadow:0 10px 30px rgba(0,0,0,0.35);
            margin-top:20px;
            margin-bottom:25px;
            line-height:1.7;
        ">

        <h2 style="margin-top:0; color:#ffffff;">
        🏋️ {level} {muscle} Workout
        </h2>

       <div style="
           color:#e8f5ff;
           font-size:16px;
        ">
        {answer.replace(chr(10), "<br>")}
        </div>

        </div>
        """, unsafe_allow_html=True)

        with st.expander("📚 View Sources"):
            for source in sources:
                st.write(source)

    except Exception as e:
        st.error(f"An error occurred: {e}")