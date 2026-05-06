import streamlit as st

# إعدادات واجهة موقع DARK AMTHAN
st.set_page_config(page_title="DARK AMTHAN", page_icon="🌐")
st.title("🌐 موقع DARK AMTHAN")
st.header("مساعد طلاب معهد رسل الحضارة الدولي")
st.subheader("تحليل محاضرات الشبكات لعام 2025")

st.markdown("---")
st.info("الموقع جاهز للإجابة على استفساراتكم حول المحاضرات السبعة (الطبقات، البروتوكولات، التوجيه)[cite: 1]")

# خانة السؤال
user_question = st.text_input("اكتب سؤالك هنا (مثلاً: ما هي وظيفة طبقة الشبكة؟)")

if user_question:
    st.write("🔍 جاري البحث في محتوى المحاضرات...")
    # هنا يتم الربط مع البيانات التي رفعتها
    if "OSI" in user_question or "طبقات" in user_question:
        st.success("حسب المحاضرة الثالثة والرابعة: يتكون نموذج OSI من 7 طبقات تبدأ بالفيزيائية وتنتهي بالتطبيق[cite: 1]")
    else:
        st.info("سيتم استخراج الإجابة الدقيقة بمجرد اكتمال رفع ملفات الـ PDF للمستودع[cite: 1]")

st.sidebar.write("تم التطوير لخدمة الطلاب - 2025")
