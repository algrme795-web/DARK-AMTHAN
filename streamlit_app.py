import streamlit as st
import os
from PyPDF2 import PdfReader
import requests
import time

# 1. إعدادات المظهر والرسائل (كما طلبت تماماً)
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    .dripping-blood {
        color: #FF0000; font-size: 65px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive; text-shadow: 0 0 15px #7b0000;
        animation: blood-drip 2s infinite;
    }
    @keyframes blood-drip { 0%, 100% { text-shadow: 0 0 10px #7b0000; } 50% { text-shadow: 0 15px #7b0000; } }
    .welcome-msg { color: #FF0000; text-align: center; font-size: 28px; font-family: 'Courier New'; font-weight: bold; }
    .answer-box { background-color: rgba(20, 0, 0, 0.95); border: 3px solid #FF0000; padding: 20px; border-radius: 15px; color: white; box-shadow: 0 0 20px #FF0000; }
    .stProgress > div > div > div > div { background-color: #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. شريط التحميل والترحيب
if 'loaded' not in st.session_state:
    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        p_bar.progress(i + 1)
    st.markdown("<p class='welcome-msg'>Welcome to DARK...</p>", unsafe_allow_html=True)
    time.sleep(1)
    p_bar.empty()
    st.session_state['loaded'] = True

st.markdown("<p class='dripping-blood'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 3. وظيفة جلب المنهج من ملفات PDF
def get_curriculum():
    text = ""
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:10]: text += page.extract_text()
        except: continue
    return text

# 4. وظيفة الاتصال بـ Gemini عبر Requests (بدون Traceback)
def ask_gemini(prompt):
    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return "💀 عذراً، لم أستطع الوصول للحل حالياً. تأكد من اتصالك."

# 5. واجهة البحث
query = st.text_input("💀 اكتب سؤالك هنا للحصول على الحل الصافي:")

if query:
    with st.spinner("⏳ جاري نبش المنهج عن الحل..."):
        context = get_curriculum()
        full_prompt = f"منهج الدراسة: {context[:4000]}. أجب بوضوح على: {query}"
        
        solution = ask_gemini(full_prompt)
        
        st.markdown("<h2 style='color: #FF0000;'>✅ الحل النهائي:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{solution}</div>", unsafe_allow_html=True)

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
