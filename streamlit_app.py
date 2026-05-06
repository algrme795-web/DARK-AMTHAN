import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="مراجعة معهد رسل الحضارة", layout="wide")

# إضافة تنسيق CSS لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #3498db; color: white; }
    .question-box { background: white; padding: 20px; border-radius: 10px; border-right: 5px solid #3498db; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .answer-text { color: #2ecc71; font-weight: bold; }
    div.stMarkdown { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 منصة مراجعة خيري عبد الواحد")
st.subheader("معهد رسل الحضارة الدولي")

# نظام القائمة الجانبية للاختيار
with st.sidebar:
    st.header("قائمة المواد")
    choice = st.radio("اختر المادة للمراجعة:", ["شبكات الحاسوب (Network)", "لغة البرمجة (++C)"])
    st.info("تم إعداد هذه الأسئلة بناءً على المنهج الدراسي المعتمد.")

if choice == "شبكات الحاسوب (Network)":
    st.header("🌐 مراجعة مادة الشبكات (CCNA-1)")
    
    # قسم المحاضرة 1 & 2
    with st.expander("المحاضرة 1 & 2: أساسيات ومكونات الشبكة", expanded=True):
        st.markdown('<div class="question-box"><b>س: ما هو تعريف شبكة الحاسب؟</b><br><span class="answer-text">ج: هي مجموعة من أجهزة الحاسب وبعض الأجهزة الأخرى المترابطة معاً، بغرض مشاركة الموارد.</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="question-box"><b>س: اذكر مكونات الشبكة الأساسية.</b><br><span class="answer-text">ج: الأجهزة (Devices)، الوسائط (Media)، والخدمات (Services).</span></div>', unsafe_allow_html=True)

    # قسم المحاضرة 3
    with st.expander("المحاضرة 3: أنواع الشبكات"):
        st.markdown('<div class="question-box"><b>س: قارن بين LAN و WAN؟</b><br><span class="answer-text">ج: LAN للمساحات الصغيرة (مكتب)، و WAN للمساحات الواسعة (مدن).</span></div>', unsafe_allow_html=True)

    # قسم المحاضرة 4
    with st.expander("المحاضرة 4: أشكال الربط (Topology)"):
        st.markdown('<div class="question-box"><b>س: ما فائدة الـ Terminator في شبكة Bus؟</b><br><span class="answer-text">ج: يمنع ارتداد الإشارات عند نهايات الكيبل.</span></div>', unsafe_allow_html=True)

else:
    st.header("💻 مراجعة لغة البرمجة (++C)")
    
    with st.expander("الأساسيات والعمليات", expanded=True):
        st.code("""
#include <iostream>
using namespace std;

int main() {
    // كود طباعة ترحيب
    cout << "Welcome to C++";
    return 0;
}
        """, language="cpp")
        st.markdown('<div class="question-box"><b>س: ما وظيفة #include <iostream>؟</b><br><span class="answer-text">ج: استدعاء مكتبة الإدخال والإخراج الأساسية في اللغة.</span></div>', unsafe_allow_html=True)

    with st.expander("الشروط والدوال"):
        st.code("""
if (grade >= 50) {
    cout << "Pass";
} else {
    cout << "Fail";
}
        """, language="cpp")
        st.markdown('<div class="question-box"><b>س: كيف نعرّف متغير رقمي صحيح؟</b><br><span class="answer-text">ج: باستخدام الكلمة المحجوزة int (مثال: int x;).</span></div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("تم التطوير بواسطة خيري عبد الواحد")
