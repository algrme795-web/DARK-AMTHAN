import streamlit as st

st.set_page_config(page_title="مراجعة خيري - الأسئلة الاسترشادية", layout="wide")

# تنسيق الواجهة
st.markdown("""
    <style>
    .stExpander { background-color: white; border-radius: 10px; border: 1px solid #3498db; }
    .q-box { color: #2c3e50; font-weight: bold; font-size: 1.1em; border-right: 5px solid #e67e22; padding-right: 15px; margin-bottom: 10px; }
    .a-box { color: #155724; background-color: #d4edda; padding: 15px; border-radius: 8px; margin-bottom: 25px; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 حل الأسئلة الاسترشادية (منهج ++C)")
st.subheader("معهد رسل الحضارة الدولي - الطالب خيري عبد الواحد")

# عرض الأسئلة من الصورة مباشرة
with st.expander("📝 حل أسئلة الصفحة 6 (الأسئلة الاسترشادية العامة)", expanded=True):
    
    st.markdown('<div class="q-box">س1: اذكر ثلاثة أمثلة على لغات البرمجة من المستوى العالي.</div>', unsafe_allow_html=True)
    st.markdown('<div class="a-box">ج: 1. ++C | 2. Java | 3. Python</div>', unsafe_allow_html=True)

    st.markdown('<div class="q-box">س2: اذكر ثلاثة من ميزات لغات ++C.</div>', unsafe_allow_html=True)
    st.markdown('<div class="a-box">ج: 1. لغة كائنية التوجه (OOP). <br> 2. السرعة والكفاءة في التنفيذ. <br> 3. القوة في التعامل مع موارد النظام والذاكرة.</div>', unsafe_allow_html=True)

    st.markdown('<div class="q-box">س3: اذكر ثلاثة من استخدامات لغة ++C.</div>', unsafe_allow_html=True)
    st.markdown('<div class="a-box">ج: 1. برمجة الألعاب الضخمة. <br> 2. تطوير المتصفحات وأنظمة التشغيل. <br> 3. برمجة الأنظمة المدمجة (Embedded Systems).</div>', unsafe_allow_html=True)

    st.markdown('<div class="q-box">س4: اذكر الغرض من استخدام جملة using namespace std في بداية الكود.</div>', unsafe_allow_html=True)
    st.markdown('<div class="a-box">ج: الغرض هو السماح باستخدام الكلمات المحجوزة في مكتبة iostream (مثل cout و cin) مباشرة دون الحاجة لكتابة std:: قبل كل أمر.</div>', unsafe_allow_html=True)

    st.markdown('<div class="q-box">س5: إلى ماذا تشير كلمة void في الدالة الرئيسية ()void main؟</div>', unsafe_allow_html=True)
    st.markdown('<div class="a-box">ج: تشير إلى أن نوع البيانات المرتجع من الدالة هو "فراغ"، أي أن الدالة لا تعيد أي قيمة لنظام التشغيل عند انتهاء البرنامج.</div>', unsafe_allow_html=True)

st.sidebar.info("تم تحديث الأسئلة بناءً على صورة المنهج المرفقة.")
