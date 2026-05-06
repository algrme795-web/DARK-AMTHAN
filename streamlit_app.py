import streamlit as st
import PyPDF2
import requests
import os
import time

# ------------------ إعداد الصفحة ------------------
st.set_page_config(page_title="DARK AMTHAN AI", layout="wide")

# ------------------ CSS مرعب ------------------
st.markdown("""
<style>
body {
    background-color: black;
    color: red;
}

.main-title {
    font-size: 50px;
    color: red;
    text-shadow: 0 0 10px darkred;
    animation: flicker 1.5s infinite;
}

@keyframes flicker {
  0% {opacity: 1;}
  50% {opacity: 0.7;}
  100% {opacity: 1;}
}

.typing {
    font-size: 25px;
    border-right: 2px solid red;
    white-space: nowrap;
    overflow: hidden;
    animation: typing 3s steps(30), blink .5s step-end infinite alternate;
}

@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

@keyframes blink {
  50% { border-color: transparent }
}
</style>
""", unsafe_allow_html=True)

# ------------------ عنوان ------------------
st.markdown('<div class="main-title">DARK AMTHAN AI</div>', unsafe_allow_html=True)

# ------------------ تأثير الكتابة ------------------
st.markdown('<div class="typing">Welcome to DARK...</div>', unsafe_allow_html=True)

# ------------------ Progress Bar ------------------
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# ------------------ قراءة PDF ------------------
def read_pdfs(folder="data"):
    text = ""
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            with open(os.path.join(folder, file), "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
    return text

pdf_text = read_pdfs()

# ------------------ إدخال المستخدم ------------------
question = st.text_input("اكتب سؤالك من المنهج...")

# ------------------ Gemini API باستخدام requests ------------------
def ask_ai(context, question):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=YOUR_API_KEY"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [{
            "parts": [{
                "text": f"اعتمد فقط على هذا النص:\n{context}\n\nالسؤال: {question}"
            }]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return "خطأ في الاتصال"

# ------------------ عرض الإجابة ------------------
if question:
    answer = ask_ai(pdf_text, question)
    st.write("### الإجابة:")
    st.write(answer)
    st.markdown(f"""
<style>
.stApp {{
    background: url("https://i.gifer.com/7VE.gif");
    background-size: cover;
}}
</style>
""", unsafe_allow_html=True)
    .stApp::before {
    content: "";
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.7);
}
