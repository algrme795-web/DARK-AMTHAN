import streamlit as st
import time
from datetime import datetime

# --- 1. CONFIGURATION & ENGINE ---
st.set_page_config(
    page_title="KHAIRY OMEGA PLATFORM 2026",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED CYBER-RED CSS (أقوى تنسيق بصري) ---
st.markdown("""
    <style>
    /* الكود الكامل لتجميل الموقع */
    .stApp {
        background: radial-gradient(circle at center, #2b0000 0%, #000000 100%);
        color: #ffffff;
    }
    
    /* تصميم البطاقات الزجاجية المتوهجة */
    .mega-card {
        background: rgba(20, 20, 20, 0.7);
        backdrop-filter: blur(20px);
        border: 2px solid #ff0000;
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 30px;
        box-shadow: 0 0 25px rgba(255, 0, 0, 0.3);
        transition: 0.5s;
        direction: rtl;
    }
    .mega-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.6);
        border: 2px solid #ffffff;
    }
    
    /* العناوين العملاقة */
    .omega-title {
        font-family: 'Impact', sans-serif;
        font-size: 6rem !important;
        text-align: center;
        background: linear-gradient(90deg, #ff0000, #ffffff, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 10px;
        filter: drop-shadow(0 0 30px #ff0000);
        margin-top: -50px;
    }
    
    .q-text { color: #ff0000; font-size: 1.6rem; font-weight: 900; border-right: 6px solid #ff0000; padding-right: 20px; margin-bottom: 15px; }
    .a-text { color: #ffffff; font-size: 1.2rem; line-height: 2; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; }
    
    /* تنسيق الدردشة */
    .chat-msg { background: #111; border-radius: 15px; padding: 15px; margin: 10px 0; border-left: 4px solid #ff0000; font-family: 'Courier New'; }
    
    /* إخفاء عناصر streamlit الافتراضية للجمال */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT (الدردشة والبيانات) ---
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "System", "content": "مرحباً بك في نظام خيري عبد الواحد المتطور. النظام جاهز للعمل.", "time": "Now"}]

# --- 4. INTRO ANIMATION (أول ما يفتح الموقع) ---
if 'mega_init' not in st.session_state:
    load_placeholder = st.empty()
    for i in range(0, 101, 2):
        load_placeholder.markdown(f"<h1 style='text-align:center; color:#ff0000; margin-top:20%; font-family:monospace;'>ACCESSING ENCRYPTED DATA: {i}%</h1>", unsafe_allow_html=True)
        time.sleep(0.02)
    load_placeholder.empty()
    st.session_state.mega_init = True

# --- 5. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color:red; text-align:center;'>OMEGA PANEL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    choice = st.selectbox("🎯 اختر المهمة:", ["🏠 قمة التحكم", "🌐 أرشيف الشبكات الكامل", "💻 مرجع البرمجة الشامل", "💬 غرفة الدردشة السرية"])
    st.markdown("---")
    st.write("👤 المستخدم: **Khairy**")
    st.write("📅 التاريخ: 2026")
    st.progress(100)
    if st.button("تحديث النظام 🔄"):
        st.rerun()

# --- 6. MAIN ENGINE CONTENT ---

# --- الصفحة الرئيسية ---
if choice == "🏠 قمة التحكم":
    st.markdown("<h1 class='omega-title'>OMEGA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>The Final Destination for Academic Excellence</h3>", unsafe_allow_html=True)
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.markdown("""
        <div class='mega-card'>
        <h2>📊 إحصائيات المنصة</h2>
        <ul>
            <li>عدد الصور المفرغة: 20 صورة كاملة</li>
            <li>عدد الأسئلة: 75 سؤال وجواب تفصيلي</li>
            <li>لغة النظام: Python / Streamlit</li>
            <li>المطور: خيري عبد الواحد</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with m_col2:
        st.markdown("""
        <div class='mega-card'>
        <h2>🛡️ نظام الحماية</h2>
        <p>تم حقن كافة الأكواد بوسائل حماية بصرية لضمان وضوح المعلومة وسهولة الحفظ. جميع الحلول مستخرجة من المنهج الرسمي للشبكات وبرمجة ++C.</p>
        </div>
        """, unsafe_allow_html=True)

# --- قسم الشبكات الكامل (10 صور) ---
elif choice == "🌐 أرشيف الشبكات الكامل":
    st.header("🌐 موسوعة الشبكات الاسترشادية (10 صور)")
    
    tabs = st.tabs(["📁 أساسيات الشبكة", "📁 البروتوكولات & OSI", "📁 الوسائط & المنافذ"])
    
    with tabs[0]:
        net_data = [
            ("ما هي أنواع الشبكات حسب المدى الجغرافي؟", "PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."),
            ("اذكر فوائد واستخدامات الشبكات؟", "مشاركة الموارد (طابعات/ملفات)، التواصل، الحوسبة السحابية، والترفيه."),
            ("ما هي أهم التحديات التي تواجه الشبكات؟", "الأمن، التوسع، سعة القناة، واستدامة الطاقة."),
            ("بماذا تتميز الشبكة المحلية LAN؟", "سرعة عالية جداً، تغطي مساحة صغيرة (مكتب/منزل)، مملوكة لجهة واحدة."),
            ("ما الفرق بين شبكة WAN والإنترنت؟", "WAN تربط مسافات شاسعة، والإنترنت هو أكبر مثال لشبكة WAN عالمية.")
        ]
        for q, a in net_data:
            st.markdown(f"<div class='mega-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with tabs[1]:
        osi_data = [
            ("اذكر طبقات نموذج OSI السبعة بالترتيب؟", "1.الفيزيائية، 2.ربط البيانات، 3.الشبكة، 4.النقل، 5.الجلسة، 6.التقديم، 7.التطبيق."),
            ("ما هي وظيفة بروتوكول IP في طبقة الشبكة؟", "العنونة المنطقية وتوجيه الحزم (Routing) وتجزئتها."),
            ("قارن بين بروتوكولات النقل TCP و UDP؟", "TCP: موثوق، يضمن الترتيب، بطيء. UDP: سريع جداً، غير موثوق، للبث المباشر والألعاب."),
            ("اذكر مهام طبقة النقل؟", "تجزئة البيانات، التحكم في التدفق، وإعادة التجميع.")
        ]
        for q, a in osi_data:
            st.markdown(f"<div class='mega-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("<div class='mega-card'>", unsafe_allow_html=True)
        st.write("📌 **المنافذ (Ports):** HTTP (80), HTTPS (443), DNS (53), SMTP (25), FTP (21).")
        st.write("📌 **الكابلات:** الألياف البصرية (الأسرع والأغلى)، الملتوية (الأكثر شيوعاً)، والمحورية.")
        st.write("📌 **بروتوكولات البريد:** POP3 و IMAP للاستقبال، SMTP للإرسال.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- قسم البرمجة الكامل (10 صور) ---
elif choice == "💻 مرجع البرمجة الشامل":
    st.header("💻 مرجع برمجة ++C (10 صور كاملة)")
    
    col_a, col_b = st.columns(2)
    with col_a:
        cpp_q = [
            ("ما هي ميزات لغة ++C؟", "لغة عالية ومنخفضة المستوى، كائنية التوجه، سريعة جداً."),
            ("اذكر أنواع البيانات الأساسية؟", "int, float, double, char, bool, string."),
            ("ما الفرق بين if و switch؟", "if تستخدم للشروط المتعددة، switch تستخدم للمفاضلة بين قيم ثابتة."),
            ("ما وظيفة cin و cout؟", "cout للإخراج والطباعة، و cin للإدخال من لوحة المفاتيح.")
        ]
        for q, a in cpp_q:
            st.markdown(f"<div class='mega-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with col_b:
        cpp_q2 = [
            ("ما هي أنواع حلقات التكرار (Loops)؟", "for (محدد)، while (بشرط)، do-while (ينفذ مرة على الأقل)."),
            ("ما هي المصفوفة (Array)؟", "مجموعة من العناصر من نفس النوع تخزن في الذاكرة بشكل متجاور."),
            ("لماذا نستخدم الدوال (Functions)؟", "لتقسيم الكود، سهولة الصيانة، ومنع التكرار."),
            ("ما الفرق بين \\n و endl؟", "كلاهما سطر جديد، لكن endl ينظف الذاكرة المؤقتة فوراً.")
        ]
        for q, a in cpp_q2:
            st.markdown(f"<div class='mega-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

# --- غرفة الدردشة (Chatroom) ---
elif choice == "💬 غرفة الدردشة السرية":
    st.header("💬 غرفة دردشة خيري")
    
    # واجهة عرض الرسائل
    for msg in st.session_state.messages:
        st.markdown(f"<div class='chat-msg'><b>[{msg['time']}] {msg['role']}:</b> {msg['content']}</div>", unsafe_allow_html=True)
    
    # حقل الإدخال
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("أدخل رسالتك للنظام:")
        send = st.form_submit_button("إرسال")
        if send and user_input:
            st.session_state.messages.append({
                "role": "خيري", 
                "content": user_input, 
                "time": datetime.now().strftime("%H:%M")
            })
            st.rerun()

# --- 7. FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ff0000; font-weight:bold; font-size:1.2rem;'>OMEGA SYSTEM BY KHAIRY ABDUL WAHID © {datetime.now().year}</p>", unsafe_allow_html=True)
