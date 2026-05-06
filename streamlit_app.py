import streamlit as st
import os
from PyPDF2 import PdfReader

# 1. تصميم الواجهة (الألوان اللي طلبتها بالضبط)
st.set_page_config(page_title="DARK SYSTEM AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    /* الاسم المتوهج ملون */
    .glow-name {
        font-size: 60px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: colorShift 3s infinite alternate;
    }
    @keyframes colorShift {
        0% { color: #ff0000; text-shadow: 0 0 20px #ff0000; }
        100% { color: #ffffff; text-shadow: 0 0 10px #ffffff; }
    }

    /* سجل البحث: أسود داكن بحدود حمراء */
    .stTextInput > div > div > input {
        background-color: #050505 !important;
        color: #ff0000 !important;
        border: 2px solid #222 !important;
        border-radius: 10px;
        font-size: 20px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff0000 !important;
        box-shadow: 0 0 15px #ff0000 !important;
    }

    /* صندوق الحل المستخرج */
    .answer-box {
        background-color: #0a0000; border: 2px solid #ff0000;
        padding: 20px; border-radius: 15px; color: white;
        font-size: 18px; line-height: 1.6;
    }
    
    /* زر قوقل الأحمر */
    .google-btn {
        display: inline-block; padding: 15px 30px;
        background-color: #ff0000; color: white !important;
        text-decoration: none; border-radius: 10px;
        font-weight: bold; font-size: 20px;
        box-shadow: 0 0 20px #ff0000;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. وظيفة البحث الذكي في ملفاتك (الشيت)
def search_in_sheets(query):
    hits = []
    # يبحث في كل ملفات الـ PDF اللي رفعتها في المشروع
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if query.lower() in text.lower():
                    # استخراج النص المحيط بالكلمة (الحل)
                    pos = text.lower().find(query.lower())
                    start = max(0, pos - 100)
                    end = min(len(text), pos + 900)
                    hits.append({
                        "file": f,
                        "page": i + 1,
                        "content": text[start:end].replace('\n', ' ')
                    })
        except: continue
    return hits

# 3. واجهة البرنامج
st.markdown("<p class='glow-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# سجل البحث
user_query = st.text_input("💀 اطلب الحل (سأبحث في الشيت أو أوجهك لقوقل):")

if user_query:
    st.markdown("<br>", unsafe_allow_html=True)
    results = search_in_sheets(user_query)
    
    if results:
        st.markdown("<h2 style='color:red;'>✅ الحلول المتوفرة في الشيت:</h2>", unsafe_allow_html=True)
        for res in results:
            with st.container():
                st.markdown(f"""
                <div class='answer-box'>
                    <b style='color:red;'>📄 المصدر: {res['file']} (صفحة {res['page']})</b><br><br>
                    {res['content']}...
                </div><br>
                """, unsafe_allow_html=True)
    else:
        # إذا لم يجد حل في الشيت، يظهر زر قوقل فوراً
        st.error("💀 لم أجد هذا السؤال في الشيت الخاص بك.")
        st.markdown(f"""
            <div style="text-align:center; padding:20px;">
                <p style="font-size:20px; color:white;">اضغط الزر بالأسفل للبحث في قوقل كروم مباشرة:</p>
                <a href="https://www.google.com/search?q={user_query}" target="_blank" class="google-btn">
                   🔍 ابحث عن الحل في قوقل 
                </a>
            </div>
        """, unsafe_allow_html=True)

st.sidebar.markdown("<h3 style='color:red;'>SYSTEM STATUS</h3>", unsafe_allow_html=True)
st.sidebar.write("✅ البحث المحلي: مفعل")
st.sidebar.write("✅ وضع قوقل: جاهز")
st.sidebar.write("❌ نظام API: معطل (بناءً على طلبك)")
