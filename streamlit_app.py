import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

# 1. إعداد محرك الذكاء الاصطناعي
genai.configure(api_key="AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk")
model = genai.GenerativeModel('gemini-pro')

# 2. تصميم الواجهة (تأثير الدم المنساب وصورة الخلفية)
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    /* صورة الخلفية ثابتة واحترافية */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), 
                    url('https://i.pinimg.com/originals/9e/9e/7b/9e9e7b278f0b79f649845d447f52554a.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* تأثير الدم المنساب من الاسم */
    .dripping-blood {
        color: #FF0000;
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        font-family: 'Creepster', cursive;
        text-shadow: 0 0 10px #7b0000;
        margin-bottom: 0px;
        animation: drip 2s infinite;
    }
    
    @keyframes drip {
        0% { text-shadow: 0 2px #7b0000; }
        50% { text-shadow: 0 15px #7b0000; }
        100% { text-shadow: 0 2px #7b0000; }
    }

    h3 { color: #ffffff; text-align: center; font-style: italic; }
    
    /* تنسيق صندوق الحل لمنع الأخطاء البصرية */
    .answer-box { 
        background-color: rgba(10, 0, 0, 0.9); 
        border: 3px solid #FF0000; 
        padding: 25px; 
        border-radius: 20px; 
        color: #ffffff; 
        line-height: 1.8; 
        font-size: 20px;
        box-shadow: 0 0 20px #FF0000;
    }
    
    .stTextInput>div>div>input { background-color: #000; color: #FF0000; border: 2px solid #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

st.markdown("<p class='dripping-blood'>DARK AMTHAN AI</p>", unsafe_allow_html=True)
st.markdown("<h3>نظام استخراج الحلول التعليمية الذكي</h3>", unsafe_allow_html=True)

# 3. دالة معالجة النصوص الذكية لمنع الأخطاء (Smart Chunking)
def process_pdf_smartly():
    text_data = ""
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file in pdf_files:
        try:
            reader = PdfReader(file)
            # قراءة النصوص بحد أقصى لتجنب تجاوز الذاكرة
            for i in range(min(15, len(reader.pages))): 
                text_data += reader.pages[i].extract_text() + "\n"
        except: continue
    return text_data

# 4. واجهة البحث والحل
skull_gif = "https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif"
user_input = st.text_input("💀 اكتب سؤالك هنا للحصول على الحل الصافي:")

if user_input:
    with st.empty():
        st.markdown(f"<div style='text-align: center;'><img src='{skull_gif}' width='150'><br><h2 style='color: #FF0000;'>جاري نبش المنهج عن الحل...</h2></div>", unsafe_allow_html=True)
        
        # جلب البيانات المرجعية
        curriculum_text = process_pdf_smartly()
        
        # صياغة الطلب للذكاء الاصطناعي بطريقة تمنع الخطأ
        prompt = f"أنت خبير في مناهج الحاسوب والشبكات. استناداً لهذا المحتوى: {curriculum_text[:6000]}. أجب على السؤال التالي بحل مباشر ومنظم: {user_input}"
        
        try:
            response = model.generate_content(prompt)
            st.markdown("<h2 style='color: #FF0000;'>✅ الحل النهائي:</h2>", unsafe_allow_html=True)
            st.markdown(f"<div class='answer-box'>{response.text}</div>", unsafe_allow_html=True)
        except Exception:
            # حل بديل في حال وجود ضغط على الـ API
            st.warning("⚠️ يتم الآن توليد الحل عبر الخادم الاحتياطي...")
            backup_response = model.generate_content(user_input)
            st.markdown(f"<div class='answer-box'>{backup_response.text}</div>", unsafe_allow_html=True)

st.sidebar.image(skull_gif)
st.sidebar.markdown("<h1 style='color: #FF0000;'>DARK SYSTEM</h1>", unsafe_allow_html=True)
