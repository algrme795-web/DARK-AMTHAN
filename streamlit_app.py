import streamlit as st
import os
from PyPDF2 import PdfReader
import time

# إعدادات الصفحة والألوان (أحمر وأسود)
st.set_page_config(page_title="DARK AMTHAN", page_icon="💀")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #FF0000; text-align: center; font-family: 'Courier New', Courier, monospace; text-shadow: 2px 2px #555; }
    h3 { color: #FFFFFF; text-align: center; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #FF0000; border: 1px solid #FF0000; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #FF0000; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>💀 DARK AMTHAN 💀</h1>", unsafe_allow_html=True)
st.markdown("<h3>مساعد معهد رسل الحضارة - تحليل المناهج</h3>", unsafe_allow_html=True)

def search_expert(query):
    results = []
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file_name in pdf_files:
        try:
            reader = PdfReader(file_name)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if query.lower() in text.lower():
                    # محاولة استخراج الفقرة التي تلي السؤال مباشرة (الحل)
                    start_pos = text.lower().find(query.lower())
                    content = text[start_pos:start_pos + 600] # استخراج 600 حرف لضمان شمول الحل
                    results.append({"file": file_name, "page": i + 1, "text": content})
        except: continue
    return results

query = st.text_input("🔍 ادخل سؤالك هنا للبحث عن الحل:")

if query:
    # تأثير الجمجمة والتحميل
    with st.empty():
        for _ in range(3):
            st.markdown("<h1 style='color: #FF0000;'>💀</h1>", unsafe_allow_html=True)
            time.sleep(0.3)
            st.markdown("<h1 style='color: #000000;'>💀</h1>", unsafe_allow_html=True)
            time.sleep(0.3)
        st.write("✔️ جاري استخراج الحل من المنهج...")

    answers = search_expert(query)
    
    if answers:
        st.markdown("<p style='color: #FF0000;'>تم العثور على الحلول التالية:</p>", unsafe_allow_html=True)
        for ans in answers:
            with st.expander(f"📄 الحل من ملف: {ans['file']} - صفحة {ans['page']}"):
                st.write(ans['text'])
    else:
        st.error("لم أجد حلاً مباشراً لهذا السؤال في الملفات المرفوعة.")

st.sidebar.markdown("<h2 style='color: #FF0000;'>DARK AMTHAN</h2>", unsafe_allow_html=True)
st.sidebar.info("تم التطوير لخدمة طلاب 2025")
