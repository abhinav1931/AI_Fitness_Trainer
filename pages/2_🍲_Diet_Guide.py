import streamlit as st
from chatbot import ask_ai
import re

st.set_page_config(
    page_title="Diet Guide",
    page_icon="🍲",
    layout="wide"
)

st.title("🍲 Diet Guide")
st.write("Generate personalized AI diet plans based on your goal.")

st.subheader("Select Your Goal")

goal = st.selectbox(
    "Goal",
    [
        "Muscle Gain",
        "Weight Loss",
        "Maintenance"
    ]
)

st.subheader("Select Diet Type")

diet = st.selectbox(
    "Diet Type",
    [
        "Vegetarian",
        "Non-Vegetarian"
    ]
)

if st.button("🍲 Generate Diet Plan"):

    question = f"Give me a {diet.lower()} diet plan for {goal.lower()} "

    try:
        answer, sources = ask_ai(question)

        st.markdown(f"""
         <div style="
            background: linear-gradient(135deg, #0f2027,#203a43,#2c5364);
            padding: 30px;
            border-radius: 22px;
            margin-top: 25px;
            margin-bottom: 25px;
            color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        ">

        <h2 style="margin-top:0; color:#ffffff;">
        🍽️ {goal} Diet Plan
        </h2>

        "<div style="
        color:#e8f5ff;
        font-size:16px;
        ">
        {answer.replace(chr(10), "<br>")}
        /div>
                
        </div>
        """, unsafe_allow_html=True)

        if sources:
            with st.expander("📚 View Sources"):
                for source in sources:
                    st.write(source)

    except Exception as e:
        st.error(f"Error occurred: {e}")