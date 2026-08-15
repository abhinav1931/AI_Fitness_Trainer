import streamlit as st
from chatbot import ask_ai

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config( 
    page_title="FitGenie AI",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)    

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Intialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## 🏋️ FitGenie AI")

    st.caption("💪 AI Powered Fitness Trainer")

    st.image("assets/logo.png", width=180)

    st.markdown("---")

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

    st.markdown("## 🚀 Features")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:22px;
    border-radius:18px;
    color:white;
    box-shadow:0px 8px 20px rgba(0,0,0,.35);
    margin-bottom:15px;
    ">

    <h3 style="margin-top:0;">🚀 Features</h3>

    ✅ Workout Guide<br><br>
    ✅ Diet Guide<br><br>
    ✅ Supplement Guide<br><br>
    ✅ BMI Calculator<br><br>
    ✅ Calorie Calculator<br><br>
    ✅ Protein Calculator

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("🟢 AI Running Offline")
    st.caption("Version 3.0")

st.markdown("---")

st.subheader("📊 Session Stats")

user_count = len(
    [m for m in st.session_state.messages if m["role"] == "user"]
)

assistant_count = len(
    [m for m in st.session_state.messages if m["role"] == "assistant"]
)

st.metric("💬 Questions Asked", user_count)

st.metric("🤖 Answers Generated", assistant_count)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A5F,#2C7BE5);
padding:35px;
border-radius:20px;
color:white;
text-align:center;
box-shadow:0px 10px 30px rgba(0,0,0,.35);
margin-bottom:25px;
">

<h1 style="margin:0;font-size:42px;">
🏋️ FitGenie AI
</h1>

<p style="font-size:20px;color:#dbeafe;margin-top:10px;">
Your Personal AI Fitness Trainer
</p>

<p style="font-size:16px;color:#e5f3ff;">
💪 Workout Plans &nbsp;&nbsp;|&nbsp;&nbsp;
🥗 Diet Plans &nbsp;&nbsp;|&nbsp;&nbsp;
💊 Supplements &nbsp;&nbsp;|&nbsp;&nbsp;
🔥 Calories &nbsp;&nbsp;|&nbsp;&nbsp;
⚖️ BMI Calculator
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Quick Stats
# -----------------------------

st.markdown("## 📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#1E3A5F,#2C7BE5);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(0,0,0,.35);
    ">
        <h2>📚</h2>
        <h3>Knowledge Base</h3>
        <h1>4</h1>
        <p>Fitness Guides</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#0F9D58,#34A853);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(0,0,0,.35);
    ">
        <h2>🤖</h2>
        <h3>AI Model</h3>
        <h1>Llama 3.2</h1>
        <p>Offline Mode</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#F57C00,#FF9800);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(0,0,0,.35);
    ">
        <h2>⚡</h2>
        <h3>Status</h3>
        <h1>Online</h1>
        <p>Ready to Answer</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("## 🔥 Try These Questions")

col1, col2 = st.columns(2)

with col1:

    if st.button("💪 Beginner Chest Workout", use_container_width=True):
        st.session_state["quick_question"] = "Give me a beginner chest workout."

    if st.button("🥗 Muscle Gain Diet Plan", use_container_width=True):
        st.session_state["quick_question"] = "Create a muscle gain diet plan."

    if st.button("🏋️ Push Day Workout", use_container_width=True):
        st.session_state["quick_question"] = "Suggest a beginner push day workout."

with col2:

    if st.button("💊 Creatine Guide", use_container_width=True):
        st.session_state["quick_question"] = "Explain creatine."

    if st.button("🔥 Calculate Calories", use_container_width=True):
        st.session_state["quick_question"] = "Calculate calories for muscle gain."

    if st.button("🍗 Best Protein Sources", use_container_width=True):
        st.session_state["quick_question"] = "Best protein sources for vegetarians."

# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input("💬 Ask your fitness question...")

if "quick_question" in st.session_state:
    question = st.session_state.pop("quick_question") 

if question:

    st.session_state.messages.append({
            "role": "user",
            "content": question
    })
    
    with st.chat_message("user"):
        st.markdown(question)

    placeholder = st.empty()

    with st.spinner("🤖 FitGenie AI is Thinking..."):
        answer, sources = ask_ai(question)

    placeholder.empty()

    full_answer = answer

    if sources:

        full_answer += "\n\n---\n"

        full_answer += "### 📚 Sources\n"

        for source in sources:

            filename = source.split("/")[-1]

            full_answer += f"✅ {filename}\n"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_answer
        }
    )

    with st.chat_message("assistant"):

        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#1E3A5F,#2C7BE5);
            padding:18px;
            border-radius:18px;
            color:white;
            margin-bottom:15px;
            box-shadow:0px 8px 20px rgba(0,0,0,.35);
    ">
           <h3 style="margin:0;">🤖 FitGenie AI</h3>
           <p style="margin-top:5px;color:#d8ecff;">
           AI Powered Fitness Assistant
        </p>
    </div>
    """, unsafe_allow_html=True)

        st.markdown(full_answer)

        if sources:
           st.divider()
           st.markdown("### 📚 Sources Used")

        with st.expander("Click to View Sources"):
            for source in sources:
               st.success(source.split("/")[-1])

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:gray;">
Made with ❤️ using LangChain + Ollama + Streamlit
<br>
FitGenie AI © 2026
</div>
""", unsafe_allow_html=True)