import streamlit as st
import os
import requests
import time

# 1. إعدادات الصفحة والجمالية (الدم والرعب)
st.set_page_config(page_title="DARK AMTHAN - EVIL EDITION", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://i.pinimg.com/originals/07/20/38/0720387ca0872223403300609395f190.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    .dripping-blood {
        color: #FF0000; font-size: 70px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive; text-shadow: 0 10px 20px #7b0000;
        animation: drip 2s infinite;
    }
    @keyframes drip { 0% { text-shadow: 0 5px #7b0000; } 50% { text-shadow: 0 25px #7b0000; } 100% { text-shadow: 0 5px #7b0000; } }
    .welcome-text { color: #FF0000; text-align: center; font-size: 30px; font-family: 'Courier New'; font-weight: bold; }
    .stButton>button { 
        background-color: #7b0000; color: white; border: 2px solid #FF0000; 
        width: 100%; font-size: 25px; height: 60px; border-radius: 15px;
    }
    .answer-box { background-color: rgba(15, 0, 0, 0.95); border: 2px solid #FF0000; padding: 25px; border-radius: 20px; color: #fff; box-shadow: 0 0 30px #FF0000; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. نظام الصوت والرعد (JavaScript)
def play_horror_sound():
    sound_html = """
    <audio id="thunder" autoplay>
        <source src="https://www.soundjay.com/nature/sounds/thunder-rain-1.mp3" type="audio/mpeg">
    </audio>
    <audio id="laugh" autoplay>
        <source src="https://www.soundbox.com/storage/samples/evil-laugh.mp3" type="audio/mpeg">
    </audio>
    <script>
        document.getElementById('thunder').volume = 0.5;
        document.getElementById('laugh').volume = 1.0;
        document.getElementById('thunder').play();
        setTimeout(function(){ document.getElementById('laugh').play(); }, 2000);
    </script>
    """
    st.components.v1.html(sound_html, height=0)

# 3. شريط التحميل والترحيب
if 'activated' not in st.session_state:
    st.markdown("<p class='dripping-blood'>DARK AMTHAN AI</p>", unsafe_allow_html=True)
    if st.button("💀 تفعيل نظام DARK (اضغط لسماع الرعد) 💀"):
        play_horror_sound()
        p_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            p_bar.progress(i + 1)
        st.markdown("<p class='welcome-text'>Welcome to DARK... Searching the Web for Blood</p>", unsafe_allow_html=True)
        time.sleep(1)
        st.session_state['activated'] = True
        st.rerun()
    st.stop()

st.markdown("<p class='dripping-blood'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 4. وظيفة البحث في قوقل عبر Gemini (طريقة الـ Requests المستقرة)
def ask_gemini_web(question):
    api_key = "AIzaSyDR_8vJRqiFmXwsscAq1WV88d8MBJbfUsk"
    # استخدام موديل يدعم البحث (Google Search Tools)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    data = {
        "contents": [{"parts": [{"text": f"ابحث في الإنترنت وأعطني إجابة مضمونة وتفصيلية للسؤال التالي: {question}"}]}],
        "tools": [{"google_search_retrieval": {}}] # هذه الإضافة هي التي تجعله يبحث في قوقل
    }
    
    try:
        response = requests.post(url, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "💀 النظام غير قادر على الوصول لقوقل حالياً، حاول مرة أخرى."

# 5. واجهة المستخدم
query = st.text_input("💀 اطلب أي معلومة من قوقل (سيتم نبش الإنترنت لإحضارها):")

if query:
    with st.spinner("⏳ جاري استدعاء الرعد والبحث في قوقل..."):
        # تشغيل صوت رعد خفيف عند البحث أيضاً
        st.components.v1.html('<audio autoplay><source src="https://www.soundjay.com/nature/sounds/lightning-strike-1.mp3" type="audio/mpeg"></audio>', height=0)
        
        answer = ask_gemini_web(query)
        
        st.markdown("<h2 style='color: #FF0000; text-align: center;'>✅ النتيجة المضمونة من الشبكة السوداء:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)

st.sidebar.image("https://i.pinimg.com/originals/4d/9d/21/4d9d21469e71b268f76332766860000e.gif")
st.sidebar.markdown("<h1 style='color: red;'>DARK SYSTEM v6.6.6</h1>", unsafe_allow_html=True)
