import streamlit as st
import os
from PyPDF2 import PdfReader
import requests
import time

# 1. الواجهة المظلمة (Deep Dark) والاسم الملون
st.set_page_config(page_title="DARK SYSTEM AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    
    /* تأثير الاسم الملون المتوهج */
    .glow-name {
        font-size: 75px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: colorShift 4s infinite alternate;
    }
    @keyframes colorShift {
        0% { color: #ff0000; text-shadow: 0 0 20px #ff0000; }
        50% { color: #ffffff; text-shadow: 0 0 30px #7b0000; }
        100% { color: #8b0000; text-shadow: 0 0 10px #ff0000; }
    }

    /* سجل البحث: أسود داكن بحدود حمراء عند التركيز */
    .stTextInput > div > div > input {
        background-color: #080808 !important;
        color: #ff0000 !important;
        border: 2px solid #222 !important;
        border-radius: 8px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff0000 !important;
        box-shadow: 0 0 15px #ff0000 !important;
    }

    /* الزر الدائري */
    .stButton > button {
        border-radius: 50%; width: 200px; height: 200px;
        background-color: #000; border: 4px solid #ff0000;
        color: #ff0000; font-size: 28px; font-weight: bold;
        box-shadow: 0 0 30px #ff0000; margin: 0 auto; display: block;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. نظام الدخول
if 'unlocked' not in st.session_state:
    p = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        p.progress(i+1)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("💀\nACTIVATE"):
        st.session_state['unlocked'] = True
        st.rerun()
    st.stop()

st.markdown("<p class='glow-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 3. محرك الحلول المتعددة (PDF + GOOGLE + RETRY)
def solve_everything(query):
    # استخراج النصوص بأمان
    context = ""
    try:
        files = [f for f in os.listdir('.') if f.endswith('.pdf')]
        for f in files:
            reader = PdfReader(f)
            for page in reader.pages[:5]: context += page.extract_text()
    except: pass

    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    # استخدام الإصدار المستقر v1
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": f"Context: {context[:3000]}\nQuestion: {query}\nInstruction: Search PDF first, then Google. Be precise."}]}],
        "tools": [{"google_search_retrieval": {}}]
    }

    # آلية المحاولات المتكررة لضمان 0% خطأ
    for attempt in range(3):
        try:
            response = requests.post(url, json=payload, timeout=15)
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            time.sleep(1) # انتظر ثانية قبل إعادة المحاولة
        except Exception as e:
            if attempt == 2: return f"💀 خطأ تقني نهائي: {str(e)}"
    return "💀 فشلت جميع المحاولات للاتصال بالنظام المظلم."

# 4. الواجهة
q = st.text_input("💀 اطلب العلم من المنهج أو قوقل:")
if q:
    with st.spinner("⏳ جاري نبش الإنترنت والملفات..."):
        ans = solve_everything(q)
        st.markdown(f"<div style='background: #0a0000; border: 2px solid red; padding: 20px; border-radius: 10px;'>{ans}</div>", unsafe_allow_html=True)
