import streamlit as st
import os
from PyPDF2 import PdfReader
import time

# إعدادات الصفحة
st.set_page_config(page_title="DARK AMTHAN", page_icon="💀", layout="wide")

# تصميم الخلفية المتحركة والألوان (أحمر وأسود)
st.markdown("""
    <style>
    /* خلفية متحركة سوداء */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
    }
    h1 { color: #FF0000; text-align: center; font-size: 60px; text-shadow: 5px 5px 10px #000; font-family: 'Ghostwriter', cursive; }
    h3 { color: #ffffff; text-align: center; }
    .stTextInput>div>div>input { background-color: #000; color: #FF0000; border: 2px solid #FF0000; font-size: 20px; }
    .answer-box { background-color: rgba(30, 0, 0, 0.8); border: 2px solid #FF0000; padding: 20px; border-radius: 15px; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>💀 DARK AMTHAN 💀</h1>", unsafe_allow_html=True)
st.markdown("<h3>مساعد طلاب معهد رسل الحضارة الدولي 2025</h3>", unsafe_allow_html=True)

# وظيفة البحث المتطور عن الحلول
def get_the_answer(query):
    final_results = []
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file_name in pdf_files:
        try:
            reader = PdfReader(file_name)
            for page in reader.pages:
                text = page.extract_text()
                if query.lower() in text.lower():
                    # البحث عن الفقرة التي تلي السؤال مباشرة
                    start_pos = text.lower().find(query.lower()) + len(query)
                    # استخراج 800 حرف لضمان شمول الحل الكامل
                    solution = text[start_pos:start_pos + 800]
                    final_results.append({"file": file_name, "content": solution})
        except: continue
    return final_results

# أيقونة الجمجمة من بينترست أثناء الانتظار
skull_gif = "https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif"

user_query = st.text_input("💀 ادخل السؤال هنا لاستخراج الحل النهائي:")

if user_query:
    # شاشة التحميل المرعبة
    with st.empty():
        st.markdown(f"<div style='text-align: center;'><img src='{skull_gif}' width='200'><br><h2 style='color: red;'>جاري نبش القبور عن الحل...</h2></div>", unsafe_allow_html=True)
        time.sleep(3) # لإظهار التأثير
    
    solutions = get_the_answer(user_query)
    
    if solutions:
        st.markdown("<h2 style='color: #FF0000;'>✅ تم استخراج الحل بنجاح:</h2>", unsafe_allow_html=True)
        for sol in solutions:
            st.markdown(f"""
            <div class="answer-box">
                <h4 style="color: red;">📄 من المصدر: {sol['file']}</h4>
                <p style="font-size: 18px;">{sol['content']}</p>
            </div><br>
            """, unsafe_allow_html=True)
    else:
        st.error("💀 لم يتم العثور على هذا الحل في المنهج المرفوع. حاول بكلمات مفتاحية أخرى.")

st.sidebar.markdown("<h1 style='color: red;'>DARK</h1>", unsafe_allow_html=True)
st.sidebar.image(skull_gif)
