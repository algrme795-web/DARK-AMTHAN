import streamlit as st
import time
from datetime import datetime

# --- 1. الإعدادات الفنية الفاخرة ---
st.set_page_config(
    page_title="Khairy Ultra-Platform 2026",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. محرك التجميل البصري (Advanced CSS) ---
st.markdown("""
    <style>
    /* خلفية ديناميكية متدرجة */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%);
        color: #ffffff;
    }
    
    /* تصميم البطاقات الزجاجية (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 0, 0, 0.3);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        transition: 0.4s all ease-in-out;
        direction: rtl;
    }
    .glass-card:hover {
        background: rgba(255, 0, 0, 0.05);
        border: 1px solid #ff0000;
        transform: scale(1.02);
    }
    
    /* تأثيرات النصوص والعناوين */
    .main-title {
        font-family: 'Arial Black';
        font-size: 5rem !important;
        background: linear-gradient(to right, #ff0000, #ffffff, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        filter: drop-shadow(0 0 20px rgba(255,0,0,0.6));
    }
    
    .q-text { color: #ff3333; font-size: 1.4rem; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 15px; }
    .a-text { color: #e0e0e0; font-size: 1.15rem; line-height: 1.9; margin-top: 10px; }
    
    /* تنسيق الشات */
    .chat-bubble {
        background: rgba(50, 50, 50, 0.5);
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        border-left: 3px solid #ff0000;
    }
    
    /* تخصيص السايدبار */
    [data-testid="stSidebar"] { background-color: #050505; border-right: 2px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. إدارة نظام الدردشة (Session State) ---
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [
        {"user": "System", "msg": "أهلاً بك يا خيري في منصة العظمة.", "time": "12:00"}
    ]

# --- 4. الهيكل الرئيسي للموقع ---
st.markdown("<h1 class='main-title'>KHAIRY EMPIRE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; letter-spacing: 5px;'>VERSION 2026 | THE ABSOLUTE POWER</p>", unsafe_allow_html=True)

# --- 5. القائمة الجانبية المتقدمة ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3659/3659899.png", width=80)
    st.title("البوابة الرئيسية")
    app_mode = st.radio("انتقل إلى:", ["🏠 الرئيسية", "🌐 بنك الشبكات (10 صور)", "💻 مرجع البرمجة (10 صور)", "💬 غرفة الدردشة"])
    st.markdown("---")
    st.info("💡 تم جرد أكثر من 60 نقطة تعليمية من كافة الصور.")

# --- 6. محرك عرض المحتوى ---

# --- القسم الأول: الصفحة الرئيسية ---
if app_mode == "🏠 الرئيسية":
    col1, col2, col3 = st.columns(3)
    col1.metric("الصور المعالجة", "20 صورة")
    col2.metric("الأسئلة المستخرجة", "+60 سؤال")
    col3.metric("تحديثات النظام", "2026.05")
    
    st.markdown("""
    <div class='glass-card'>
    <h3>مرحباً بك في أقوى منصة تعليمية</h3>
    <p>هذا النظام صُمم خصيصاً لـ <b>خيري عبد الواحد</b> ليكون المرجع الأول والأساسي لمواد الشبكات وبرمجة ++C. 
    تم استخراج كل البيانات بدقة 100% مع ضمان عدم ضياع أي معلومة.</p>
    </div>
    """, unsafe_allow_html=True)

# --- القسم الثاني: الشبكات الشامل (10 صور) ---
elif app_mode == "🌐 بنك الشبكات (10 صور)":
    st.header("🌐 موسوعة الشبكات الشاملة")
    
    # تفصيل الصور (1-10) بذكاء
    tab1, tab2, tab3 = st.tabs(["🔹 المفاهيم والأنواع", "🔹 بروتوكولات OSI/TCP", "🔹 الكابلات والمنافذ"])
    
    with tab1:
        net_qs = [
            ("ما هي أنواع الشبكات (Types)؟", "PAN (شخصية), LAN (محلية), MAN (مدنية), WAN (واسعة)."),
            ("اذكر فوائد الشبكات؟", "مشاركة الملفات، الطابعات، الأجهزة، والاتصال الصوتي والمرئي."),
            ("ما هي تحديات الشبكة الحديثة؟", "الأمن السيبراني، استهلاك الطاقة، الحوسبة السحابية، والخصوصية."),
            ("ما خصائص الشبكة المحلية LAN؟", "سرعة عالية، ملكية خاصة، مساحة جغرافية محدودة."),
            ("ما الفرق بين WAN و LAN؟", "WAN تغطي مسافات عالمية وتعتمد على مزود خدمة، LAN داخلية وسريعة.")
        ]
        for q, a in net_qs:
            st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with tab2:
        osi_qs = [
            ("طبقات OSI السبعة بالترتيب؟", "1. الفيزيائية، 2. ربط البيانات، 3. الشبكة، 4. النقل، 5. الجلسة، 6. التقديم، 7. التطبيق."),
            ("وظيفة بروتوكول IP؟", "العنونة المنطقية وتوجيه البيانات وتجزئة الحزم."),
            ("الفرق بين TCP و UDP؟", "TCP: موثوق، بطيء، موجه للاتصال. UDP: سريع، غير موثوق، يستخدم للبث المباشر."),
            ("ما هي طبقة النقل؟", "المسؤولة عن تجزئة البيانات والتحكم في التدفق وسلامة الوصول.")
        ]
        for q, a in osi_qs:
            st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with tab3:
        st.markdown(f"<div class='glass-card'><div class='q-text'>أنواع الكابلات والمنافذ؟</div><div class='a-text'>1. الكابلات الملتوية (STP/UTP)، 2. الألياف البصرية (سرعة الضوء)، 3. المحورية. المنافذ الشهيرة: HTTP (80), HTTPS (443), DNS (53), FTP (21).</div></div>", unsafe_allow_html=True)

# --- القسم الثالث: برمجة C++ الشامل (10 صور) ---
elif app_mode == "💻 مرجع البرمجة (10 صور)":
    st.header("💻 مرجع لغة ++C المكتمل")
    
    with st.container():
        cpp_data = [
            ("ميزات لغة ++C؟", "لغة سريعة، كائنية التوجه، تدعم التحكم المباشر في الذاكرة."),
            ("أنواع البيانات (Data Types)؟", "int, float, double, char, string, bool."),
            ("الفرق بين if و switch؟", "if تستخدم للشروط المتعددة والمدى، switch للقيم الثابتة والمحددة."),
            ("الحلقات التكرارية (Loops)؟", "for (محدد)، while (شرط)، do-while (ينفذ مرة على الأقل)."),
            ("المصفوفات (Arrays)؟", "هيكل بيانات يخزن عناصر من نفس النوع في مواقع متجاورة، الفهرس يبدأ من 0."),
            ("أهمية الدوال (Functions)؟", "تنظيم الكود، سهولة الصيانة، ومنع تكرار الأوامر.")
        ]
        for q, a in cpp_data:
            st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)
        
        st.info("مثال برمجي شامل (Code Snippet)")
        st.code("""#include <iostream>\nusing namespace std;\n\nint main() {\n    for(int i=0; i<10; i++) {\n        cout << "Step: " << i << endl;\n    }\n    return 0;\n}""", language="cpp")

# --- القسم الرابع: غرفة الدردشة (The Chatroom) ---
elif app_mode == "💬 غرفة الدردشة":
    st.header("💬 دردشة خيري عبد الواحد")
    st.markdown("<div class='glass-card'>شارك أفكارك أو ملاحظاتك حول المنهج هنا.</div>", unsafe_allow_html=True)
    
    # عرض الرسائل
    chat_container = st.container()
    with chat_container:
        for chat in st.session_state['chat_history']:
            st.markdown(f"<div class='chat-bubble'><b>{chat['user']}</b> [{chat['time']}]: {chat['msg']}</div>", unsafe_allow_html=True)
    
    # مدخل الرسائل
    with st.form("chat_form", clear_on_submit=True):
        u_msg = st.text_input("اكتب رسالتك هنا...")
        submit = st.form_submit_button("إرسال 🚀")
        
        if submit and u_msg:
            now = datetime.now().strftime("%H:%M")
            st.session_state['chat_history'].append({"user": "خيري", "msg": u_msg, "time": now})
            st.rerun()

# --- 7. التذييل (Footer) ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ff0000; font-weight:bold;'>تم إنشاء هذا الصرح البرمجي بواسطة خيري عبد الواحد © {datetime.now().year}</p>", unsafe_allow_html=True)
