import streamlit as st
from chatbot import ask_ai

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Supplements Guide",
    page_icon="💊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("💊 Supplements Guide")
st.write("Learn about fitness supplements with AI.")

# -----------------------------
# Select Supplement
# -----------------------------
supplement = st.selectbox(
    "Choose Supplement",
    [
        "Whey Protein",
        "Creatine",
        "Multivitamin",
        "Fish Oil",
        "Vitamin D",
        "BCAA",
        "Pre Workout"
    ]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("💊 Explain Supplement"):

    question = f"""
    Explain {supplement}.

    Include:
    - Benefits
    - Side Effects
    - Recommended Dosage
    - Best Time to Take
    - Who Should Use It
    """

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
                💊 {supplement} Guide
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
        st.error(f"Error: {e}")