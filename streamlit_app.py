import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

# 1. إعداد الذكاء الاصطناعي (استخدام مفتاحك)
genai.configure(api_key="AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk")
model = genai.GenerativeModel('gemini-pro')

# 2. تصميم الواجهة والخلفية المتحركة
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    /* خلفية متحركة واحترافية */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* اسم يقطر دماً */
    .dripping-blood {
        color: #FF0000;
        font-size: 65px;
        font-weight: bold;
        text-align: center;
        font-family: 'Creepster', cursive;
        text-shadow: 5px 5px 15px #000;
        margin-top: -20px;
    }

    /* رسالة الترحيب الحمراء */
    .welcome-text {
        color: #FF0000;
        text-align: center;
        font-size: 30px;
        font-family: 'Courier New';
        font-weight: bold;
        border-right: 3px solid #FF0000;
        white-space: nowrap;
        overflow: hidden;
        margin: 0 auto;
        animation: typing 3.5s steps(30, end), blink-caret .75s step-end infinite;
    }

    @keyframes typing { from { width: 0 } to { width: 100% } }
    @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #FF0000; } }

    .answer-box { 
        background-color: rgba(15, 0, 0, 0.95); 
        border: 2px solid #FF0000; 
        padding: 20px; 
        border-radius: 15px; 
        color: #ffffff; 
        box-shadow: 0 0 15px #FF0000;
    }
    
    .stProgress > div > div > div > div { background-color: #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. شريط التحميل ورسالة الترحيب عند الفتح
if 'first_load' not in st.session_state:
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.markdown("<p class='welcome-text'>Welcome to DARK...</p>", unsafe_allow_html=True)
    time.sleep(1)
    progress_bar.empty()
    st.session_state['first_load'] = True

st.markdown("<p class='dripping-blood'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 4. دالة جلب النصوص من الـ PDF
def fetch_curriculum():
    text = ""
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:10]: # قراءة أول 10 صفحات للسرعة
                text += page.extract_text()
        except: continue
    return text

# 5. البحث والحل الذكي (بدون أخطاء Traceback)
query = st.text_input("💀 ادخل سؤالك هنا:")

if query:
    with st.spinner("⏳ جاري تحليل المنهج..."):
        context = fetch_curriculum()
        try:
            # إرسال السؤال مع سياق المنهج
            full_prompt = f"منهج الدراسة: {context[:5000]}. السؤال: {query}. أجب بوضوح."
            response = model.generate_content(full_prompt)
            st.markdown(f"<div class='answer-box'><strong>✅ الحل:</strong><br>{response.text}</div>", unsafe_allow_html=True)
        except Exception:
            # حل بديل لمنع انهيار الموقع
            try:
                response = model.generate_content(query)
                st.markdown(f"<div class='answer-box'><strong>✅ الحل (ذكاء عام):</strong><br>{response.text}</div>", unsafe_allow_html=True)
            except:
                st.error("💀 خطأ في الاتصال بالذكاء الاصطناعي. حاول مرة أخرى.")

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
