import streamlit as st
import os
from PyPDF2 import PdfReader
import requests
import time

# 1. إعدادات الصفحة والجمالية (تأثير الاسم الملون)
st.set_page_config(page_title="DARK SYSTEM AI", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* اسم يتغير لونه (Neon Animation) */
    .changing-color-name {
        font-size: 70px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: color-change 3s infinite;
    }
    @keyframes color-change {
        0% { color: #FF0000; text-shadow: 0 0 20px #FF0000; }
        33% { color: #7b0000; text-shadow: 0 0 20px #7b0000; }
        66% { color: #ffffff; text-shadow: 0 0 20px #ffffff; }
        100% { color: #FF0000; text-shadow: 0 0 20px #FF0000; }
    }

    /* الزر الدائري الكبير */
    .stButton>button {
        border-radius: 50%; width: 200px; height: 200px;
        background-color: #000; border: 5px solid #FF0000;
        color: #FF0000; font-size: 30px; font-weight: bold;
        box-shadow: 0 0 50px #FF0000; transition: 0.3s;
        margin: 0 auto; display: block;
    }
    .stButton>button:hover { transform: scale(1.1); background-color: #FF0000; color: #000; }

    .answer-box { background-color: rgba(10, 0, 0, 0.9); border: 2px solid #FF0000; padding: 25px; border-radius: 15px; color: white; }
    .stProgress > div > div > div > div { background-color: #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. وظيفة الصوت (رعد وضحكة)
def play_horror():
    sound_js = """
    <audio id="thunder" autoplay><source src="https://www.soundjay.com/nature/sounds/thunder-rain-1.mp3"></audio>
    <audio id="laugh" autoplay><source src="https://www.soundbox.com/storage/samples/evil-laugh.mp3"></audio>
    """
    st.components.v1.html(sound_js, height=0)

# 3. شريط التحميل والزر الدائري
if 'access' not in st.session_state:
    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        p_bar.progress(i + 1)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:red;'>SYSTEM LOCKED</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("💀 ENTER"):
            play_horror()
            st.session_state['access'] = True
            st.rerun()
    st.stop()

st.markdown("<p class='changing-color-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 4. محرك البحث الهجين (PDF + Google)
def search_hybrid(query):
    # أولاً: جلب نصوص من الـ PDF
    pdf_text = ""
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:10]: pdf_text += page.extract_text()
        except: continue
    
    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # الطلب الذكي: ابحث في النص المرفق، وإذا لم تجد، استخدم بحث قوقل
    prompt = f"""
    لديك النص التالي من المنهج التعليمي: {pdf_text[:4000]}
    السؤال هو: {query}
    تعليمات: 
    1. ابحث عن الإجابة في النص المرفق أولاً.
    2. إذا لم تجد الإجابة في النص، استخدم أداة بحث قوقل المدمجة لديك وأعطني إجابة مضمونة من الإنترنت.
    3. ابدأ إجابتك بذكر مصدر المعلومة (من المنهج أو من الإنترنت).
    """
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search_retrieval": {}}]
    }
    
    try:
        response = requests.post(url, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "💀 حدث خطأ في الاتصال بالنظام المظلم."

# 5. واجهة البحث
user_query = st.text_input("💀 اطلب العلم من المنهج أو من قوقل:")

if user_query:
    with st.spinner("⏳ جاري نبش الملفات والإنترنت..."):
        result = search_hybrid(user_query)
        st.markdown("<h2 style='color: #FF0000;'>✅ الحل النهائي:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{result}</div>", unsafe_allow_html=True)

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
