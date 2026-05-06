import streamlit as st
import os
from PyPDF2 import PdfReader
import requests
import time

# 1. إعدادات الصفحة والألوان (أسود داكن + أحمر)
st.set_page_config(page_title="DARK SYSTEM AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    /* الخلفية سوداء داكنة جداً */
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)), 
                          url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
    }

    /* اسم يتغير لونه باستمرار */
    .changing-color-name {
        font-size: 70px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: neon-glow 3s infinite;
    }
    @keyframes neon-glow {
        0% { color: #FF0000; text-shadow: 0 0 20px #FF0000; }
        50% { color: #500000; text-shadow: 0 0 30px #FF0000; }
        100% { color: #ffffff; text-shadow: 0 0 10px #ffffff; }
    }

    /* مكان سجل البحث: أسود يتحول للأحمر عند الضغط */
    .stTextInput > div > div > input {
        background-color: #000000 !important;
        color: #FF0000 !important;
        border: 2px solid #333333 !important;
        border-radius: 10px;
        font-size: 20px;
        transition: 0.5s;
    }
    .stTextInput > div > div > input:focus {
        border: 2px solid #FF0000 !important;
        box-shadow: 0 0 15px #FF0000 !important;
    }

    /* الزر الدائري الكبير للفتح */
    .stButton > button {
        border-radius: 50%; width: 220px; height: 220px;
        background-color: #000; border: 4px solid #FF0000;
        color: #FF0000; font-size: 35px; font-weight: bold;
        box-shadow: 0 0 40px #7b0000; transition: 0.4s;
        margin: 0 auto; display: block;
        font-family: 'Creepster', cursive;
    }
    .stButton > button:hover { transform: scale(1.1) rotate(5deg); box-shadow: 0 0 60px #FF0000; background-color: #100000; }

    .answer-box { background-color: #0a0000; border: 2px solid #FF0000; padding: 25px; border-radius: 15px; color: white; box-shadow: inset 0 0 10px #FF0000; }
    .stProgress > div > div > div > div { background-color: #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. وظيفة الرعد والضحكة
def play_dark_intro():
    st.components.v1.html("""
    <audio id="thunder" autoplay><source src="https://www.soundjay.com/nature/sounds/thunder-rain-1.mp3"></audio>
    <audio id="laugh" autoplay><source src="https://www.soundbox.com/storage/samples/evil-laugh.mp3"></audio>
    """, height=0)

# 3. مرحلة الدخول (شريط التحميل + الزر)
if 'unlocked' not in st.session_state:
    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        p_bar.progress(i + 1)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("💀\nENTER\nSYSTEM"):
            play_dark_intro()
            st.session_state['unlocked'] = True
            st.rerun()
    st.stop()

st.markdown("<p class='changing-color-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 4. محرك البحث (PDF + الإنترنت)
def get_final_answer(query):
    # محاولة قراءة الملفات
    content = ""
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            pdf = PdfReader(f)
            for page in pdf.pages[:5]: content += page.extract_text()
        except: continue

    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # تحسين البرومبت ليحل مشكلة الاتصال
    prompt = f"استخدم النص التالي كمرجع: {content[:3000]}. إذا لم تجد الإجابة، ابحث في قوقل وأجب على: {query}"
    
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "💀 النظام يواجه ضغطاً من الأرواح.. حاول مرة أخرى بعد قليل."

# 5. واجهة البحث
user_input = st.text_input("💀 سجل البحث (اطلب ما تريد من المنهج أو قوقل):")

if user_input:
    with st.spinner("⏳ جاري نبش المعلومات..."):
        result = get_final_answer(user_input)
        st.markdown("<h2 style='color: #FF0000;'>✅ الحل النهائي:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{result}</div>", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='color: red; text-align: center;'>DARK SIDE</h2>", unsafe_allow_html=True)
st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
