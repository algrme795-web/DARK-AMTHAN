import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Dark Amtihan - النسخة الكاملة", layout="wide")

# التصميم الاحترافي (أحمر وأسود)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; }
    [data-testid="stSidebar"] { background-color: #0b0b0b; border-right: 2px solid #ff0000; }
    .stExpander { background-color: #151515; border: 1px solid #333; border-radius: 10px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 15px; margin: 15px 0; text-align: right; direction: rtl; }
    .a-box { background-color: #1f1f1f; padding: 15px; border-radius: 5px; color: #e0e0e0; text-align: right; direction: rtl; border: 1px dashed #444; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# شريط التحميل
if 'loaded' not in st.session_state:
    p_bar = st.progress(0, text="جاري حقن كافة الأسئلة (20 صورة)...")
    for p in range(100):
        time.sleep(0.01)
        p_bar.progress(p + 1)
    st.session_state['loaded'] = True
    p_bar.empty()

st.title("🔥 Dark Amtihan: Full Edition 🔥")

# القائمة الجانبية
st.sidebar.title("المواد")
choice = st.sidebar.radio("اختر المنهج:", ["الشبكات (10 صور كاملة)", "برمجة ++C (10 صور كاملة)"])

# --- قسم الشبكات الشامل ---
if choice == "الشبكات (10 صور كاملة)":
    st.header("🌐 بنك أسئلة الشبكات الكامل")
    
    with st.expander("📁 الأسئلة من صورة 1 إلى 5 (الأنواع والبروتوكولات)"):
        net_qs = [
            ("س: اذكر أنواع شبكات الانترنت؟", "ج: PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."),
            ("س: ما هي استخدامات الشبكة؟", "ج: مشاركة الموارد، التواصل، نقل الملفات، والتجارة الإلكترونية."),
            ("س: اذكر تحديات الشبكات؟", "ج: الأمن، الخصوصية، استهلاك الطاقة، وتوسع الشبكة."),
            ("س: ما هي وظائف بروتوكول IP؟", "ج: العنونة المنطقية، التوجيه (Routing)، وتجزئة الحزم."),
            ("س: قارن بين TCP و UDP؟", "ج: TCP موثوق وموجه للاتصال، بينما UDP سريع وغير موجه للاتصال."),
            ("س: اذكر طبقات نموذج OSI السبعة؟", "ج: الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق."),
            ("س: ما هي وظيفة DNS؟", "ج: تحويل أسماء النطاقات (Domains) إلى عناوين IP.")
        ]
        for q, a in net_qs:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 الأسئلة من صورة 6 إلى 10 (الكابلات والمنافذ)"):
        net_qs2 = [
            ("س: اذكر أنواع الكابلات ومزاياها؟", "ج: الملتوية (رخيصة)، المحورية (مقاومة للتداخل)، الألياف (سريعة جداً)."),
            ("س: ما هي أنواع المنافذ (Ports)؟", "ج: المعروفة (0-1023)، المسجلة (1024-49151)، والديناميكية."),
            ("س: اذكر بروتوكولات البريد الإلكتروني؟", "ج: SMTP للإرسال، POP3 و IMAP للاستقبال."),
            ("س: ما هو الفرق بين HTTP و HTTPS؟", "ج: HTTPS مشفر وآمن باستخدام SSL/TLS بينما HTTP غير مشفر.")
        ]
        for q, a in net_qs2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# --- قسم برمجة C++ الشامل ---
else:
    st.header("💻 بنك أسئلة ++C الكامل")
    
    with st.expander("📁 الأسئلة من صورة 1 إلى 5 (الأساسيات والشروط)"):
        cpp_qs = [
            ("س: ما هي ميزات لغة ++C؟", "ج: لغة كائنية (OOP)، سريعة، وتستخدم في تطوير الأنظمة والألعاب."),
            ("س: اذكر أنواع المتغيرات الأساسية؟", "ج: int, float, double, char, bool."),
            ("س: ما الفرق بين جملة if وجملة switch؟", "ج: if للقيم المنطقية والمدى، و switch للقيم الثابتة والمحددة."),
            ("س: ما هي وظيفة cin و cout؟", "ج: cout للطباعة (الإخراج) و cin للقراءة (الإدخال).")
        ]
        for q, a in cpp_qs:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 الأسئلة من صورة 6 إلى 10 (الدوال والمصفوفات)"):
        cpp_qs2 = [
            ("س: ما هي أنواع حلقات التكرار (Loops)؟", "ج: for, while, do-while."),
            ("س: كيف نعرف مصفوفة (Array)؟", "ج: نوع البيانات ثم الاسم ثم الحجم، مثال: int numbers[10];"),
            ("س: ما هي فوائد استخدام الدوال (Functions)؟", "ج: تنظيم الكود، منع التكرار، وسهولة الصيانة."),
            ("س: ما معنى الرمز (\\n) والرمز (endl)؟", "ج: كلاهما يستخدم لبدء سطر جديد في المخرجات.")
        ]
        for q, a in cpp_qs2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("تم تضمين كافة الأسئلة من الـ 20 صورة بنجاح.")
