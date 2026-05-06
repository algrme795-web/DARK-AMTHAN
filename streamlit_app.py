import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

# 1. إعداد الذكاء الاصطناعي بمفتاحك
genai.configure(api_key="AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk")
model = genai.GenerativeModel('gemini-pro')

# 2. إعدادات المظهر مع صورتك الجديدة في الخلفية
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://i.pinimg.com/originals/9e/9e/7b/9e9e7b278f0b79f649845d447f52554a.jpg');
        background-size: cover;
        background-position: center;
    }
    h1 { color: #FF0000; text-align: center; font-size: 55px; text-shadow: 3px 3px 5px #000; }
    .answer-box { background-color: rgba(0, 0, 0, 0.85); border: 2px solid #FF0000; padding: 20px; border-radius: 10px; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>💀 DARK AMTHAN AI 💀</h1>", unsafe_allow_html=True)

# 3. دالة ذكية لقراءة أجزاء من الملفات لتجنب الخطأ
def get_smart_context(search_query):
    context = ""
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file in pdf_files:
        try:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if search_query.lower() in text.lower():
                    context += text + "\n"
                    if len(context) > 5000: break # حد معين لعدم إثقال المحرك
        except: continue
    return context

# 4. خانة السؤال والحل
query = st.text_input("💀 ادخل سؤالك هنا للحصول على الحل النهائي:")

if query:
    with st.spinner("⏳ جاري استخراج الحل من المنهج..."):
        # الحصول على النص المتعلق بالسؤال فقط
        relevant_text = get_smart_context(query)
        
        if relevant_text:
            prompt = f"بناءً على المنهج: {relevant_text[:8000]}. أجب بوضوح وتفصيل على: {query}"
            try:
                response = model.generate_content(prompt)
                st.markdown("<h2 style='color: #FF0000;'>✅ الحل المستخرج:</h2>", unsafe_allow_html=True)
                st.markdown(f"<div class='answer-box'>{response.text}</div>", unsafe_allow_html=True)
            except:
                st.error("💀 حاول تقليل الكلمات في السؤال.")
        else:
            # إذا لم يجد نصاً في الـ PDF، سيجيب الذكاء الاصطناعي من معلوماته العامة
            response = model.generate_content(query)
            st.markdown(f"<div class='answer-box'>{response.text}</div>", unsafe_allow_html=True)

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
