import streamlit as st
import time
import pandas as pd
from datetime import datetime

# --- 1. PRE-CORE CONFIGURATION ---
st.set_page_config(
    page_title="KHAIRY IMPERIAL CORE 2026",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE IMPERIAL CSS (أعنف وأجمل تنسيق بصري ممكن) ---
st.markdown("""
    <style>
    /* تصميم الخلفية الكونية */
    .stApp {
        background: radial-gradient(circle at top, #1a1a1a 0%, #000000 100%);
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* بطاقات النيون المتوهجة */
    .imperial-card {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid #ff0000;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        transition: 0.4s ease;
        direction: rtl;
    }
    .imperial-card:hover {
        border: 1px solid #ffffff;
        box-shadow: 0 0 40px rgba(255, 0, 0, 0.5);
        transform: scale(1.01);
    }
    
    /* العناوين الإمبراطورية */
    .title-text {
        font-size: 5rem !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, #ff0000, #ffffff, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px #ff0000);
        margin-bottom: 10px;
    }

    /* شريط الحالة والتقدم */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #440000, #ff0000);
    }

    /* الدردشة الاحترافية */
    .chat-bubble-user { background: #330000; border-radius: 15px; padding: 12px; margin: 8px 0; border-right: 4px solid #ff0000; }
    .chat-bubble-sys { background: #111111; border-radius: 15px; padding: 12px; margin: 8px 0; border-left: 4px solid #ffffff; font-style: italic; }
    
    /* تعديل السايدبار */
    [data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ENGINE ---
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []
if 'progress_val' not in st.session_state:
    st.session_state.progress_val = 0

# --- 4. DATA ARCHIVE (جرد الـ 20 صورة بالكامل) ---
# بيانات الشبكات المستخلصة من 10 صور
networking_archive = [
    {"سؤال": "ما هي أنواع الشبكات حسب التغطية؟", "جواب": "PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."},
    {"سؤال": "اذكر فوائد شبكات الحاسوب؟", "جواب": "مشاركة الأجهزة والملفات، البريد الإلكتروني، التواصل، والعمل عن بعد."},
    {"سؤال": "ما هي تحديات الشبكات؟", "جواب": "الأمن والخصوصية، استهلاك الطاقة، التوسع المستمر."},
    {"سؤال": "خصائص الشبكة المحلية LAN؟", "جواب": "سرعة عالية، مساحة صغيرة، ملكية خاصة للجهة المشغلة."},
    {"سؤال": "طبقات OSI السبعة؟", "جواب": "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق."},
    {"سؤال": "ما هي وظيفة بروتوكول IP؟", "جواب": "العنونة، التوجيه، وتجزئة حزم البيانات في طبقة الشبكة."},
    {"سؤال": "الفرق بين TCP و UDP؟", "جواب": "TCP موثوق ويضمن التوصيل. UDP سريع جداً ويستخدم للبث المباشر."},
    {"سؤال": "أنواع كابلات الشبكة؟", "جواب": "الملتوية (Twisted Pair)، المحورية (Coaxial)، الألياف البصرية (Fiber)."},
    {"سؤال": "أهم المنافذ (Ports)؟", "جواب": "HTTP: 80, HTTPS: 443, DNS: 53, SMTP: 25, FTP: 21."},
    {"سؤال": "مزايا الحوسبة السحابية؟", "جواب": "توفير التكلفة، المرونة، سهولة الوصول من أي مكان."}
]

# بيانات البرمجة المستخلصة من 10 صور
cpp_archive = [
    {"سؤال": "ما هي ميزات لغة ++C؟", "جواب": "كائنية التوجه (OOP)، سريعة، وتحكم مباشر في عتاد الحاسوب."},
    {"سؤال": "أنواع البيانات في ++C؟", "جواب": "int, float, char, bool, double, string."},
    {"سؤال": "الفرق بين if و switch؟", "جواب": "if للظروف المعقدة والمدى، switch للقيم الثابتة والمحددة."},
    {"سؤال": "وظيفة cin و cout؟", "جواب": "cout للطباعة والإخراج، cin لاستقبال مدخلات المستخدم."},
    {"سؤال": "أنواع التكرار (Loops)؟", "جواب": "for (عدد محدد)، while (بشرط)، do-while (مرة على الأقل)."},
    {"سؤال": "تعريف المصفوفة (Array)؟", "جواب": "مجموعة عناصر من نفس النوع تُخزن بشكل متسلسل في الذاكرة."},
    {"سؤال": "أهمية الدوال (Functions)؟", "جواب": "تقسيم البرنامج، منع التكرار، وسهولة تتبع الأخطاء."},
    {"سؤال": "ما هي break و continue؟", "جواب": "break تنهي الحلقة فوراً، continue تتخطى الدورة الحالية."},
    {"سؤال": "المتغير العالمي والمحلي؟", "جواب": "العالمي (Global) متاح للكل، المحلي (Local) داخل دالته فقط."},
    {"سؤال": "وظيفة endl؟", "جواب": "إنهاء السطر وتفريغ ذاكرة المخرجات المؤقتة."}
]

# --- 5. APP NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff0000; text-align:center;'>IMPERIAL MENU</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1160/1160358.png", width=120)
    page = st.selectbox("🎯 اختر الوجهة:", ["💎 اللوحة الرئيسية", "📡 رادار الشبكات", "💻 مختبر البرمجة", "🗨️ غرفة العمليات"])
    st.markdown("---")
    st.write("🛠️ النظام: **النسخة السادسة**")
    st.write("👤 القائد: **خيري عبد الواحد**")
    if st.button("تصفير الذاكرة 🧹"):
        st.session_state.chat_log = []
        st.rerun()

# --- 6. CORE LOGIC ---

# --- الوجهة 1: اللوحة الرئيسية ---
if page == "💎 اللوحة الرئيسية":
    st.markdown("<h1 class='title-text'>IMPERIAL CORE</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("البيانات المفرغة", "20 صورة")
    col2.metric("دقة الاستخراج", "100%")
    col3.metric("تحديث النظام", "2026")
    
    st.markdown("""
    <div class='imperial-card'>
    <h3>📜 بيان المهمة</h3>
    هذا النظام هو أقوى نسخة برمجية تم تطويرها لخدمة <b>خيري عبد الواحد</b>. تم دمج كافة الأسئلة الاسترشادية 
    للمنهج الدراسي في قاعدة بيانات ذكية تضمن لك الوصول للمعلومة بلمحة بصر.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 📈 تقدم المراجعة")
    progress = st.slider("حدد مقدار ما ذاكرته اليوم:", 0, 100, 50)
    st.progress(progress)

# --- الوجهة 2: رادار الشبكات ---
elif page == "📡 رادار الشبكات":
    st.header("📡 قاعدة بيانات الشبكات (الـ 10 صور كاملة)")
    search_net = st.text_input("🔍 ابحث عن سؤال في الشبكات...")
    
    for item in networking_archive:
        if search_net.lower() in item['سؤال'].lower():
            st.markdown(f"""
            <div class='imperial-card'>
                <div style='color:#ff0000; font-weight:bold; font-size:1.3rem;'>Q: {item['سؤال']}</div>
                <div style='margin-top:10px; color:#cccccc;'>A: {item['جواب']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- الوجهة 3: مختبر البرمجة ---
elif page == "💻 مختبر البرمجة":
    st.header("💻 مرجع البرمجة ++C (الـ 10 صور كاملة)")
    
    search_cpp = st.text_input("🔍 ابحث عن أمر برمجبي...")
    
    for item in cpp_archive:
        if search_cpp.lower() in item['سؤال'].lower():
            st.markdown(f"""
            <div class='imperial-card'>
                <div style='color:#ff0000; font-weight:bold; font-size:1.3rem;'>Q: {item['سؤال']}</div>
                <div style='margin-top:10px; color:#cccccc;'>A: {item['جواب']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    with st.expander("📝 مساحة تجربة الكود"):
        st.code("""#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Khairy is the Best!";\n    return 0;\n}""", language="cpp")

# --- الوجهة 4: غرفة العمليات (الدردشة) ---
elif page == "🗨️ غرفة العمليات":
    st.header("🗨️ التواصل المباشر")
    
    # عرض الشات
    for chat in st.session_state.chat_log:
        st.markdown(f"<div class='chat-bubble-{chat['role']}'>{chat['content']}</div>", unsafe_allow_html=True)
    
    with st.form("imperial_chat", clear_on_submit=True):
        u_input = st.text_input("أرسل أمراً للنظام:")
        btn = st.form_submit_button("إرسال 🚀")
        
        if btn and u_input:
            st.session_state.chat_log.append({"role": "user", "content": u_input})
            st.session_state.chat_log.append({"role": "sys", "content": f"تم استلام أمرك يا خيري وجاري تنفيذه في السيرفر الرئيسي..."})
            st.rerun()

# --- 7. IMPERIAL FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ff0000; font-weight:bold; letter-spacing:3px;'>BUILT FOR THE CHOSEN ONE: KHAIRY ABDUL WAHID © {datetime.now().year}</p>", unsafe_allow_html=True)
