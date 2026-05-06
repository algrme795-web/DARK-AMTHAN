import streamlit as st
import os

st.set_page_config(page_title="DARK AMTHAN", page_icon="🌐")

st.markdown("<h1 style='text-align: center;'>🌐 موقع DARK AMTHAN</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>مساعد طلاب معهد رسل الحضارة الدولي</h3>", unsafe_allow_html=True)

query = st.text_input("اكتب سؤالك هنا عن الشبكات أو C++:")

if query:
    st.write("🔍 جاري البحث في الملفات المرفوعة...")
    
    # البحث عن ملفات PDF في المستودع
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if pdf_files:
        st.success(f"تم العثور على {len(pdf_files)} ملفات منهج. جاري تحليل المحتوى...")
        # هنا الموقع سيقوم بعرض الملفات المرتبطة بسؤالك
        for file in pdf_files:
            st.info(f"يمكنك مراجعة ملف: {file} للحصول على التفاصيل.")
    else:
        st.error("لم يتم العثور على ملفات PDF. تأكد من رفعها للمستودع.")

st.sidebar.markdown("تم التطوير لخدمة الطلاب - 2025")
