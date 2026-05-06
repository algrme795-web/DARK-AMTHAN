import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

# 1. إعداد مفتاح الذكاء الاصطناعي الخاص بك
genai.configure(api_key="AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk")
model = genai.GenerativeModel('gemini-pro')

# 2. إعدادات الصفحة والمظهر (أحمر وأسود)
st.set_page_config(page_title="DARK AMTHAN AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    /* خلفية متحركة سوداء مرعبة */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
    }
    h1 { color: #FF0000; text-align: center; font-size: 60px; text-shadow: 4px 4px 10px #000; font-family: 'Courier New'; }
    h3 { color: #ffffff; text-align: center; }
    .stTextInput>div>div>input { background-color: #000; color: #FF0000; border: 2px solid #FF0000; border-radius: 10px; }
    .answer-box { background-color: rgba(20, 0, 0, 0.9); border: 2px solid #FF0000; padding: 25px; border-radius: 15px; color: white; line-height: 1.8; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>💀 DARK AMTHAN AI 💀</h1>", unsafe_allow_html=True)
st.markdown("<h3>مساعد طلاب معهد رسل الحضارة الدولي - نظام الحلول الذكي</h3>", unsafe_allow_html=True)

# 3. وظيفة قراءة ملفات الـ PDF المرفوعة
def get_pdf_content():
    combined_text = ""
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file in pdf_files:
        try:
            reader = PdfReader(file)
            for page in reader.pages:
                combined_text += page.extract_text() + "\n"
        except: continue
    return combined_text

# 4. واجهة المستخدم والبحث
skull_gif = "https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif"
query = st.text_input("💀 ادخل سؤالك هنا لاستخراج الحل النهائي من المنهج:")

if query:
    # تأثير التحميل والجمجمة
    with st.empty():
        st.markdown(f"<div style='text-align: center;'><img src='{skull_gif}' width='150'><br><h2 style='color: red;'>جاري استدعاء الحل من المنهج...</h2></div>", unsafe_allow_html=True)
        time.sleep(2)
    
    # استخراج النص من ملفاتك (الشبكات و C++)
    context = get_pdf_content()
    
    if context:
        try:
            # إرسال المعلومات للذكاء الاصطناعي ليقوم بالحل
            prompt = f"أنت خبير تعليمي. بناءً على هذا المنهج المرفوع: {context[:10000]}. أجب على هذا السؤال بدقة واحترافية: {query}"
            response = model.generate_content(prompt)
            
            st.markdown("<h2 style='color: #FF0000;'>✅ الحل الذكي المستخرج:</h2>", unsafe_allow_html=True)
            st.markdown(f"<div class='answer-box'>{response.text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("💀 حدث خطأ في معالجة الحل. تأكد من رفع ملفات الـ PDF.")
    else:
        st.warning("⚠️ لم يتم العثور على ملفات PDF في المستودع. ارفع ملفات المنهج أولاً.")

# القائمة الجانبية
st.sidebar.image(skull_gif)
st.sidebar.markdown("<h2 style='color: red; text-align: center;'>DARK SYSTEM</h2>", unsafe_allow_html=True)
st.sidebar.info("تم التطوير لخدمة طلاب المعهد - 2025")
