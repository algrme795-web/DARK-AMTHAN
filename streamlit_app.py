import streamlit as st
import os
from PyPDF2 import PdfReader

st.set_page_config(page_title="DARK AMTHAN", page_icon="🌐")

st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🌐 موقع DARK AMTHAN</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>مساعد طلاب معهد رسل الحضارة الدولي</h3>", unsafe_allow_html=True)
st.divider()

def search_in_pdfs(query):
    results = []
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for file_name in pdf_files:
        try:
            reader = PdfReader(file_name)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if query.lower() in text.lower():
                    start_idx = max(0, text.lower().find(query.lower()) - 200)
                    end_idx = min(len(text), start_idx + 500)
                    snippet = text[start_idx:end_idx]
                    results.append({"file": file_name, "page": i + 1, "text": snippet})
        except Exception:
            continue
    return results

query = st.text_input("🔍 اكتب سؤالك هنا:")

if query:
    with st.spinner("جاري قراءة الملفات..."):
        answers = search_in_pdfs(query)
        if answers:
            st.success(f"تم العثور على معلومات:")
            for ans in answers:
                with st.expander(f"📖 من ملف: {ans['file']} (صفحة {ans['page']})"):
                    st.write(ans['text'])
        else:
            st.warning("لم يتم العثور على إجابة مباشرة.")

st.sidebar.info("تم التطوير لخدمة الطلاب - 2025")
