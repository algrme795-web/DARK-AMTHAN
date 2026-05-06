import streamlit as st
import os
from PyPDF2 import PdfReader
import requests
import time

# 1. تنسيق الواجهة (أسود داكن + سجل أحمر + اسم ملون)
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    /* الاسم الملون المتوهج */
    .glow-name {
        font-size: 60px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: colorShift 3s infinite alternate;
    }
    @keyframes colorShift {
        0% { color: #ff0000; text-shadow: 0 0 20px #ff0000; }
        50% { color: #ffffff; text-shadow: 0 0 30px #7b0000; }
        100% { color: #8b0000; text-shadow: 0 0 10px #ff0000; }
    }

    /* سجل البحث: أسود داكن بحدود حمراء متوهجة */
    .stTextInput > div > div > input {
        background-color: #050505 !important;
        color: #ff0000 !important;
        border: 2px solid #222 !important;
        border-radius: 10px;
        font-size: 20px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff0000 !important;
        box-shadow: 0 0 20px #ff0000 !important;
    }

    /* صندوق الحل */
    .answer-box {
        background-color: #0a0000;
        border: 2px solid #ff0000;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 18px;
        line-height: 1.6;
        box-shadow: inset 0 0 15px #ff0000;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. وظيفة قراءة الشيت (PDF)
def get_pdf_content():
    text = ""
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:15]: # يقرأ أول 15 صفحة لضمان السرعة
                text += page.extract_text()
        except: continue
    return text

# 3. وظيفة الحصول على الحل (AI + Search)
def get_ai_solution(user_query):
    sheet_content = get_pdf_content()
    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # هنا السر: نطلب منه يحل من الشيت، وإذا ما لقاش يحل من قوقل
    prompt = f"""
    أنت مساعد ذكي لمعهد رسل الحضارة.
    استخدم هذا النص من الشيت للإجابة: {sheet_content[:4000]}
    السؤال: {user_query}
    إذا لم تجد الإجابة في الشيت، ابحث في قوقل وأعطني حلاً كاملاً ومضموناً.
    """
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search_retrieval": {}}]
    }

    for _ in range(3): # محاولات تكرار لضمان 0% خطأ
        try:
            res = requests.post(url, json=payload, timeout=15)
            if res.status_code == 200:
                return res.json()['candidates'][0]['content']['parts'][0]['text']
        except:
            time.sleep(1)
    return "💀 النظام المظلم تعثر.. حاول مرة أخرى."

# 4. واجهة المستخدم
st.markdown("<p class='glow-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

query = st.text_input("💀 اطلب الحل (سأبحث في الشيت وقوقل):")

if query:
    with st.spinner("⏳ جاري استخراج الحل من الأعماق..."):
        solution = get_ai_solution(query)
        st.markdown("<h2 style='color:red;'>✅ الحل النهائي المضمون:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{solution}</div>", unsafe_allow_html=True)

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
