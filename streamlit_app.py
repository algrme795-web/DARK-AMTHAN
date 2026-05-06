import streamlit as st

st.set_page_config(page_title="بنك الأسئلة الاسترشادية - ++C", layout="wide")

st.markdown("""
    <style>
    .stExpander { background-color: white; border-radius: 10px; border: 1px solid #2ecc71; margin-bottom: 15px; }
    .q-text { color: #2c3e50; font-weight: bold; border-right: 5px solid #27ae60; padding-right: 10px; }
    .a-text { color: #155724; background-color: #f0fff4; padding: 10px; border-radius: 5px; margin-bottom: 15px; border: 1px dotted #27ae60; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 الحلول الكاملة للأسئلة الاسترشادية (++C)")
st.subheader("معهد رسل الحضارة الدولي - الطالب خيري عبد الواحد")

# حل أسئلة الصورة 1 (ص 6)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 6 (مقدمة البرمجة)"):
    st.markdown('<p class="q-text">1- اذكر ثلاثة أمثلة على لغات البرمجة من المستوى العالي.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: ++Java, Python, C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">2- اذكر ثلاثة من ميزات لغات ++C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: لغة كائنية التوجه (OOP)، سريعة وفعالة، تدعم التعامل المباشر مع الذاكرة.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">4- اذكر الغرض من استخدام جملة using namespace std.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: تتيح استخدام عناصر مكتبة iostream (مثل cout) دون كتابة std:: قبل كل أمر.</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 2 (ص 16)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 16 (أنواع البيانات)"):
    st.markdown('<p class="q-text">1- اذكر ثلاثة أمثلة للأنواع الأساسية للبيانات في ++C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: int (للأرقام الصحيحة)، float (للأرقام العشرية)، char (للحروف).</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">2- اذكر الغرض من استخدام نوع البيانات int.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: تعريف متغيرات تخزن أرقاماً صحيحة فقط (بدون كسور).</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">4- اذكر الغرض من استخدام نوع البيانات bool.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: تخزين القيم المنطقية (True أو False) فقط.</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 3 (ص 36)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 36 (الكائنات Classes)"):
    st.markdown('<p class="q-text">2- اذكر مفهوم الخصائص (Attributes) في ++C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: هي المتغيرات التي تُعرف داخل الكلاس وتحدد صفات الكائن.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">3- اذكر الغرض من استخدام Public في الـ Class.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: جعل الأعضاء (متغيرات/دوال) قابلة للوصول من خارج الكلاس.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">4- اذكر الغرض من استخدام Private في الـ Class.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: حماية البيانات بحيث لا يمكن الوصول إليها إلا من داخل الكلاس نفسه.</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 4 (ص 61)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 61 (الجمل الشرطية Switch/If)"):
    st.markdown('<p class="q-text">4- اكتب الغرض من استخدام الجملة الشرطية switch.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: اختيار تنفيذ كود معين من بين عدة خالات محتملة بناءً على قيمة متغير واحد.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">6- اذكر ثلاثة من الأخطاء التي يمكن أن تحدث عند استخدام switch.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: نسيان أمر break، تكرار قيم الـ cases، عدم وضع حالة default.</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 6 (ص 84)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 84 (الحلقات التكرارية)"):
    st.markdown('<p class="q-text">1- اذكر ثلاثة من أنواع الحلقات المستخدمة في ++C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: for loop, while loop, do-while loop.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">4- اذكر الغرض من استخدام الجملة break.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: الخروج الفوري من الحلقة التكرارية أو جملة switch.</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 7 (ص 96)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 96 (المصفوفات Arrays)"):
    st.markdown('<p class="q-text">1- اذكر استخدام المصفوفات في ++C.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: تخزين مجموعة من القيم من نفس نوع البيانات في متغير واحد وتحت فهرس (Index) معين.</p>', unsafe_allow_html=True)
    st.markdown('<p class="q-text">5- اكتب أمر الوصول للعنصر الثاني في المصفوفة int arr[] = {10, 20, 30}.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: arr[1]</p>', unsafe_allow_html=True)

# حل أسئلة الصورة 10 (ص 127)
with st.expander("📝 الأسئلة الاسترشادية - صفحة 127 (دوال التحكم)"):
    st.markdown('<p class="q-text">5- اكتب الغرض من استخدام الجملة exit.</p>', unsafe_allow_html=True)
    st.markdown('<p class="a-text">ج: إنهاء تنفيذ البرنامج بالكامل فوراً من أي مكان في الكود.</p>', unsafe_allow_html=True)

st.sidebar.success("تم حل كافة أسئلة الصور المرفقة ✅")
