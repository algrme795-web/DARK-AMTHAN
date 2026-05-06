import streamlit as st
import os
from PyPDF2 import PdfReader
import webbrowser
import time

# 1. الواجهة السوداء والاسم الملون (بدون تغيير)
st.set_page_config(page_title="DARK SYSTEM - NO API", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .glow-name {
        font-size: 70px; font-weight: bold; text-align: center;
        font-family: 'Creepster', cursive;
        animation: colorShift 3s infinite alternate;
    }
    @keyframes colorShift {
        0% { color: #ff0000; text-shadow: 0 0 20px #ff0000; }
        100% { color: #ffffff; text-shadow: 0 0 10px #ffffff; }
    }
    /* جعل سجل البحث أسود داكن */
    .stTextInput > div > div > input {
        background-color: #050505 !important;
        color: #ff0000 !important;
        border: 2px solid #333 !important;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

st.markdown("<p class='glow-name'>DARK AMTHAN AI</p>", unsafe_allow_html=True)

# 2. وظيفة البحث في الشيت (PDF)
def search_in_sheets(query):
    results = []
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for f in files:
        try:
            reader = PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if query.lower() in text.lower():
                    results.append(f"وجدنا شيئاً في ملف {f} - صفحة {i+1}")
        except: continue
    return results

# 3. واجهة المستخدم
q = st.text_input("💀 اكتب سؤالك هنا (سأبحث في ملفاتك أو أفتح لك قوقل):")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 ابحث في الشيت (PDF)"):
        with st.spinner("جاري فحص الملفات..."):
            hits = search_in_sheets(q)
            if hits:
                for hit in hits: st.success(hit)
            else:
                st.error("لم أجد شيئاً في ملفاتك.. اذهب لقوقل.")

with col2:
    if st.button("🌐 ابحث في قوقل كروم"):
        # هذا السطر يفتح المتصفح فوراً ببحث قوقل
        search_url = f"https://www.google.com/search?q={q}"
        webbrowser.open(search_url)
        st.info("تم فتح البحث في قوقل كروم الآن.")

# إضافة ملاحظة في الأسفل
st.sidebar.markdown("### نظام بدون API")
st.sidebar.info("هذا النظام يعتمد على ملفاتك المحلية ومتصفحك الشخصي فقط.")
