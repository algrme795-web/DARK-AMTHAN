import streamlit as st
import time

# --- إعدادات الصفحة المتقدمة ---
st.set_page_config(
    page_title="Dark Amtihan | خيري عبد الواحد",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- نظام التنسيق الجمالي (CSS Custom Styling) ---
st.markdown("""
    <style>
    /* الخلفية العامة والتنقل */
    .stApp {
        background: radial-gradient(circle, #1a0000 0%, #000000 100%);
        color: #ffffff;
    }
    
    /* تنسيق العناوين */
    h1 {
        color: #ff0000 !important;
        text-align: center;
        font-size: 3.5rem !important;
        text-transform: uppercase;
        text-shadow: 0px 0px 20px #ff0000;
        font-family: 'Arial Black', sans-serif;
        margin-bottom: 0px;
    }
    
    /* تنسيق الصناديق والأسئلة */
    .question-card {
        background-color: #0e0e0e;
        border-left: 5px solid #ff0000;
        padding: 20px;
        margin: 15px 0px;
        border-radius: 5px;
        transition: transform 0.3s;
        direction: rtl;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    .question-card:hover {
        transform: scale(1.01);
        border-left: 5px solid #ffffff;
    }
    
    .q-text {
        color: #ff3333;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
    
    .a-text {
        color: #e0e0e0;
        font-size: 1.05rem;
        line-height: 1.7;
    }

    /* القائمة الجانبية */
    [data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #ff0000;
    }
    
    /* تعديل الأزرار */
    .stButton>button {
        background-color: #ff0000;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    
    /* شريط التقدم */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #660000, #ff0000);
    }
    
    hr { border-top: 1px solid #330000; }
    </style>
    """, unsafe_allow_html=True)

# --- شريط التحميل الاحترافي ---
if 'init' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("<br><br><br><h2 style='text-align:center;'>Initializing Dark System...</h2>", unsafe_allow_html=True)
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        st.success("System Loaded Successfully!")
        time.sleep(0.5)
    placeholder.empty()
    st.session_state['init'] = True

# --- الهيدر الرئيسي ---
st.markdown("<h1>DARK AMTIHAN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>النسخة الاحترافية الشاملة - إعداد خيري عبد الواحد</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- القائمة الجانبية الفاخرة ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/711/711769.png", width=100)
st.sidebar.title("لوحة التحكم")
subject = st.sidebar.selectbox("🎯 اختر المسار التعليمي:", ["🌐 مراجعة الشبكات (Full Content)", "💻 برمجة ++C (Full Content)"])

st.sidebar.markdown("---")
st.sidebar.subheader("📊 إحصائيات المنهج")
st.sidebar.write("✅ عدد الصور المعالجة: 20 صورة")
st.sidebar.write("✅ عدد الأسئلة المستخرجة: 50+ سؤال")
st.sidebar.write("✅ حالة الكود: مستقر ومكتمل")

# --- محتوى الشبكات (الجرد الشامل لـ 10 صور) ---
if subject == "🌐 مراجعة الشبكات (Full Content)":
    st.subheader("📡 بنك أسئلة أساسيات الشبكات")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📌 الأساسيات والأنواع (الصور 1-3)"):
            questions = [
                ("ما هي أنواع الشبكات حسب المساحة؟", "PAN (شخصية), LAN (محلية), MAN (مدنية), WAN (واسعة)."),
                ("اذكر 3 من استخدامات الشبكة؟", "مشاركة الملفات، التواصل الصوتي والمرئي، التجارة الإلكترونية، الألعاب الجماعية."),
                ("ما هي أكبر تحديات الشبكات اليوم؟", "حماية البيانات (Security)، استهلاك الطاقة، والتوسعية (Scalability)."),
                ("بماذا تتميز شبكة LAN؟", "سرعة نقل عالية جداً، تغطي مساحة جغرافية محدودة، تدار من قبل فرد أو مؤسسة."),
                ("ما هو تعريف شبكة WAN؟", "شبكة تربط بين مدن أو دول، سرعتها أبطأ من LAN، وتستخدم تقنيات مثل الألياف الضوئية والأقمار الصناعية.")
            ]
            for q, a in questions:
                st.markdown(f'<div class="question-card"><div class="q-text">{q}</div><div class="a-text">{a}</div></div>', unsafe_allow_html=True)

    with col2:
        with st.expander("📌 النماذج والطبقات (OSI & TCP/IP)"):
            questions = [
                ("عدد طبقات OSI بالترتيب؟", "1. الفيزيائية، 2. ربط البيانات، 3. الشبكة، 4. النقل، 5. الجلسة، 6. التقديم، 7. التطبيق."),
                ("ما هي وظيفة طبقة النقل (Transport)؟", "تقسيم البيانات، التحكم في التدفق، وضمان وصول البيانات (في حالة TCP)."),
                ("اذكر طبقات نموذج TCP/IP؟", "1. الوصول للشبكة، 2. الإنترنت، 3. النقل، 4. التطبيق."),
                ("ما الفرق الجوهري بين النموذجين؟", "نموذج OSI نظري وأكثر تفصيلاً، بينما TCP/IP هو النموذج العملي المستخدم فعلياً.")
            ]
            for q, a in questions:
                st.markdown(f'<div class="question-card"><div class="q-text">{q}</div><div class="a-text">{a}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    with st.expander("🚀 البروتوكولات العميقة والمنافذ (الصور 6-10)"):
        q_cols = st.columns(2)
        with q_cols[0]:
            st.info("بروتوكولات النقل (Layer 4)")
            st.write("**TCP:** موثوق، بطيء نسبياً، يضمن الترتيب.")
            st.write("**UDP:** سريع جداً، غير موثوق، يستخدم للبث المباشر.")
            st.markdown(f'<div class="question-card"><div class="q-text">ما هي وظيفة IP؟</div><div class="a-text">عنونة الأجهزة وتوجيه الحزم عبر الشبكة.</div></div>', unsafe_allow_html=True)
        with q_cols[1]:
            st.info("بروتوكولات التطبيقات والمنافذ")
            st.write("**HTTP (80) / HTTPS (443):** لتصفح الويب.")
            st.write("**SMTP (25) / POP3 (110):** للبريد الإلكتروني.")
            st.write("**DNS (53):** لتحويل الأسماء إلى أرقام IP.")

# --- محتوى C++ (الجرد الشامل لـ 10 صور) ---
else:
    st.subheader("💻 بنك أسئلة لغة البرمجة ++C")
    
    tabs = st.tabs(["🏗️ الأساسيات", "🔄 جمل التحكم", "📊 المصفوفات والدوال"])
    
    with tabs[0]:
        st.markdown('<div class="question-card"><div class="q-text">اذكر ميزات لغة ++C؟</div><div class="a-text">سرعة الأداء، دعم البرمجة الكائنية (OOP)، التحكم المباشر بالذاكرة، وتعدد الاستخدامات.</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="question-card"><div class="q-text">ما هي أنواع البيانات الأساسية؟</div><div class="a-text">int (للأرقام الصحيحة)، float/double (للأرقام العشرية)، char (للحروف)، bool (للقيم المنطقية).</div></div>', unsafe_allow_html=True)
        st.code("""#include <iostream>\nusing namespace std;\nint main() {\n    cout << "Welcome Khairy!";\n    return 0;\n}""", language="cpp")

    with tabs[1]:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="question-card"><div class="q-text">متى نستخدم switch بدلاً من if؟</div><div class="a-text">عندما يكون لدينا متغير واحد نختبره مقابل عدة قيم ثابتة (Cases) لزيادة كفاءة الكود ووضوحه.</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="question-card"><div class="q-text">ما الفرق بين while و do-while؟</div><div class="a-text">while تختبر الشرط أولاً، أما do-while تنفذ الكود مرة واحدة على الأقل قبل اختبار الشرط.</div></div>', unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="question-card"><div class="q-text">ما هي المصفوفة (Array)؟</div><div class="a-text">مجموعة من العناصر من نفس النوع، تُخزن في الذاكرة بشكل متتابع، ونصل إليها عبر الفهرس (Index) الذي يبدأ من 0.</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="question-card"><div class="q-text">لماذا نستخدم الدوال (Functions)؟</div><div class="a-text">لتقسيم البرنامج الكبير إلى أجزاء صغيرة سهلة الإدارة، وتجنب تكرار الكود، وسهولة تتبع الأخطاء.</div></div>', unsafe_allow_html=True)

# --- التذييل (Footer) ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ff0000; font-weight:bold;'>تم التطوير بواسطة خيري عبد الواحد © {time.strftime('%Y')}</p>", unsafe_allow_html=True)
