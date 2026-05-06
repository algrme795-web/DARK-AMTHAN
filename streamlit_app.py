import streamlit as st
import time
import random
from datetime import datetime

# --- 1. THE SOVEREIGN ENGINE CONFIG ---
st.set_page_config(
    page_title="KHAIRY SOVEREIGN CORE | 2026",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE ULTIMATE NEURAL-RED CSS (أقوى تنسيق بصري على الإطلاق) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .stApp {
        background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                    url('https://www.transparenttextures.com/patterns/carbon-fibre.png'),
                    radial-gradient(circle, #2b0000 0%, #000000 100%);
        color: #ffffff;
    }

    /* العناوين الخارقة */
    .sovereign-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 5.5rem !important;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        background: linear-gradient(to bottom, #ff0000 20%, #ffffff 50%, #ff0000 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 30px rgba(255, 0, 0, 0.8));
        margin-bottom: 0px;
    }

    /* البطاقات التفاعلية (The Sovereign Cards) */
    .sov-card {
        background: rgba(15, 15, 15, 0.9);
        border: 2px solid #ff0000;
        border-radius: 25px;
        padding: 40px;
        margin: 25px 0;
        position: relative;
        overflow: hidden;
        transition: 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        direction: rtl;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .sov-card::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,0,0,0.2), transparent);
        transition: 0.5s;
    }
    .sov-card:hover::before { left: 100%; }
    .sov-card:hover {
        transform: scale(1.03);
        border-color: #ffffff;
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.4);
    }

    .q-text { font-family: 'Orbitron', sans-serif; color: #ff0000; font-size: 1.7rem; font-weight: bold; margin-bottom: 20px; }
    .a-text { color: #e0e0e0; font-size: 1.3rem; line-height: 2.1; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; border-right: 5px solid #ff0000; }

    /* أزرار مخصصة */
    .stButton>button {
        background: linear-gradient(45deg, #ff0000, #440000);
        color: white; border: none; border-radius: 50px;
        padding: 15px 30px; font-weight: bold; text-transform: uppercase;
        transition: 0.3s; width: 100%;
    }
    .stButton>button:hover { background: #ffffff; color: #ff0000; box-shadow: 0 0 20px #ff0000; }

    /* السايدبار */
    [data-testid="stSidebar"] { background: #050505; border-right: 3px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE: THE COMPLETE ARCHIVE (تفريغ 100% لـ 20 صورة) ---
# حصر شامل للشبكات (10 صور)
NET_DB = [
    {"q": "ما هي أنواع الشبكات حسب المساحة؟", "a": "PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."},
    {"q": "ما هي استخدامات الشبكات؟", "a": "مشاركة الموارد، الملفات، الطابعات، الاتصال الصوتي والمرئي، والبريد الإلكتروني."},
    {"q": "ما هي تحديات الشبكات الحديثة؟", "a": "الأمن والخصوصية، استهلاك الطاقة، القابلية للتوسع، وإدارة البيانات الضخمة."},
    {"q": "اذكر مميزات الشبكة المحلية LAN؟", "a": "تغطية جغرافية محدودة، سرعات نقل بيانات هائلة، ملكية خاصة تدار داخلياً."},
    {"q": "ما هي خصائص شبكة WAN؟", "a": "تغطي مسافات جغرافية كبيرة (مدن/دول)، تعتمد على مزودي خدمة، وسرعتها أقل من LAN."},
    {"q": "عدد طبقات نموذج OSI السبعة بالترتيب؟", "a": "1. الفيزيائية، 2. ربط البيانات، 3. الشبكة، 4. النقل، 5. الجلسة، 6. التقديم، 7. التطبيق."},
    {"q": "ما هي وظيفة طبقة النقل (Transport Layer)؟", "a": "تقسيم البيانات (Segmentation)، التحكم في التدفق، وضمان موثوقية الوصول عبر TCP."},
    {"q": "ما هو دور بروتوكول IP في طبقة الشبكة؟", "a": "توفير العنونة المنطقية (Addressing)، التوجيه (Routing)، وتجزئة الحزم."},
    {"q": "قارن بين TCP و UDP؟", "a": "TCP: موثوق، بطيء، يضمن الترتيب. UDP: سريع جداً، غير موثوق، للبث والألعاب."},
    {"q": "اذكر أهم البروتوكولات والمنافذ (Ports)؟", "a": "HTTP(80), HTTPS(443), DNS(53), SMTP(25), FTP(21), SSH(22)."},
    {"q": "ما هي أنواع كابلات الشبكة المستخدمة؟", "a": "الكابلات الملتوية (UTP/STP)، كابلات الألياف البصرية (Fiber)، والكابلات المحورية (Coaxial)."},
    {"q": "بماذا تتميز الحوسبة السحابية (Cloud Computing)؟", "a": "المرونة، توفير التكلفة، الوصول الشامل، والأمان المتقدم."},
    {"q": "ما هو الـ IP Address والفرق بين IPv4 و IPv6؟", "a": "IPv4 يتكون من 32 بت، IPv6 يتكون من 128 بت لتوفير عدد أكبر من العناوين."},
    {"q": "ما وظيفة الـ Default Gateway؟", "a": "هو المنفذ الذي تمر عبره البيانات للخروج من الشبكة المحلية إلى الشبكات الأخرى."}
]

# حصر شامل لبرمجة C++ (10 صور)
CPP_DB = [
    {"q": "ما هي ميزات لغة ++C؟", "a": "لغة كائنية التوجه (OOP)، سريعة الأداء، قريبة من الهاردوير، ومتعددة المنصات."},
    {"q": "اذكر أنواع البيانات الأساسية (Data Types)؟", "a": "int (صحيح)، float (عشري)، char (حرف)، bool (منطقي)، double (عشري دقيق)."},
    {"q": "متى نستخدم جملة switch؟", "a": "عند المفاضلة بين عدة قيم ثابتة لمتغير واحد، وهي أكثر كفاءة من if المتكررة."},
    {"q": "ما الفرق بين cin و cout؟", "a": "cout تستخدم لطباعة المخرجات على الشاشة، و cin تستخدم لاستقبال المدخلات من المستخدم."},
    {"q": "ما هي أنواع الـ Loops في ++C؟", "a": "for (تكرار محدد)، while (تكرار مشروط)، do-while (ينفذ مرة على الأقل قبل فحص الشرط)."},
    {"q": "تعريف المصفوفة (Array) وطريقة الوصول لعناصرها؟", "a": "مجموعة عناصر من نفس النوع في ذاكرة متتابعة، نصل إليها عبر الـ Index الذي يبدأ من 0."},
    {"q": "لماذا نستخدم الدوال (Functions)؟", "a": "لتنظيم الكود، تقليل التكرار، سهولة التعديل، وتقسيم البرنامج لمهام صغيرة."},
    {"q": "ما هو المتغير المحلي (Local) والعالمي (Global)؟", "a": "المحلي يُعرف داخل دالة ولا يُرى خارجها، العالمي يُعرف في بداية البرنامج ويراه الجميع."},
    {"q": "ما وظيفة الأوامر break و continue؟", "a": "break تكسر الحلقة وتخرج منها، continue تتخطى الخطوات المتبقية وتبدأ الدورة التالية."},
    {"q": "كيف نستخدم المكتبة iostream؟", "a": "يتم تضمينها في بداية البرنامج عبر #include للسماح بعمليات الإدخال والإخراج."},
    {"q": "ما معنى التوريث (Inheritance) في ++C؟", "a": "عملية تسمح لكلاس جديد بوراثة خصائص ودوال من كلاس موجود مسبقاً."},
    {"q": "ما هي الـ Pointers؟", "a": "متغيرات تخزن عناوين الذاكرة لمتغيرات أخرى بدلاً من تخزين القيم مباشرة."}
]

# --- 4. SESSION MANAGEMENT ---
if 'chat' not in st.session_state:
    st.session_state.chat = [{"user": "CORE", "msg": "النظام السيادي مفعل.. جاهز لخدمتك يا خيري.", "time": "SECURE"}]

# --- 5. THE SOVEREIGN SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color:#ff0000; text-align:center;'>SOVEREIGN PANEL</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2621/2621113.png", width=120)
    mode = st.radio("العمليات الحيوية:", ["👑 لوحة السيادة", "📡 بنك الشبكات (100%)", "💻 معمل البرمجة (100%)", "🔥 اختبار القوة (Quiz)", "💬 قناة الاتصال"])
    st.markdown("---")
    st.write("🔧 المعالج: **Core i5 4th Gen**")
    st.write("🎮 الجرافيك: **RX 560**")
    st.progress(100)

# --- 6. CORE CONTENT ---

# -- 1. الرئيسية --
if mode == "👑 لوحة السيادة":
    st.markdown("<h1 class='sovereign-header'>SOVEREIGN</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>THE ABSOLUTE KNOWLEDGE CENTER</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class='sov-card'><h2>🛡️ التقرير التقني</h2>
        <ul><li>الحالة: مستقر</li><li>البيانات: 20 صورة كاملة</li><li>الدقة: 100%</li></ul></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='sov-card'><h2>🧠 رؤية النظام</h2>
        تجميعة <b>خيري عبد الواحد</b> التقنية قوية بما يكفي لتشغيل هذا المحرك. تم دمج كل الأسئلة لضمان النجاح الساحق.</div>""", unsafe_allow_html=True)

# -- 2. الشبكات --
elif mode == "📡 بنك الشبكات (100%)":
    st.header("📡 الأرشيف الكلي للشبكات")
    search_net = st.text_input("🔍 ابحث في قاعدة بيانات الشبكات...")
    for item in NET_DB:
        if search_net.lower() in item['q'].lower() or search_net.lower() in item['a'].lower():
            st.markdown(f"<div class='sov-card'><div class='q-text'>{item['q']}</div><div class='a-text'>{item['a']}</div></div>", unsafe_allow_html=True)

# -- 3. البرمجة --
elif mode == "💻 معمل البرمجة (100%)":
    st.header("💻 الأرشيف الكلي لبرمجة ++C")
    search_cpp = st.text_input("🔍 ابحث في قاعدة بيانات البرمجة...")
    for item in CPP_DB:
        if search_cpp.lower() in item['q'].lower() or search_cpp.lower() in item['a'].lower():
            st.markdown(f"<div class='sov-card'><div class='q-text'>{item['q']}</div><div class='a-text'>{item['a']}</div></div>", unsafe_allow_html=True)
    st.code("#include <iostream>\nusing namespace std;\nint main() { cout << 'Success is Choice'; return 0; }", language="cpp")

# -- 4. الكويز --
elif mode == "🔥 اختبار القوة (Quiz)":
    st.header("🔥 هل أنت جاهز للاختبار؟")
    all_qs = NET_DB + CPP_DB
    q_sample = random.choice(all_qs)
    st.markdown(f"<div class='sov-card'><div class='q-text'>{q_sample['q']}</div></div>", unsafe_allow_html=True)
    if st.button("كشف الإجابة"):
        st.success(q_sample['a'])

# -- 5. الشات --
elif mode == "💬 قناة الاتصال":
    st.header("💬 غرفة عمليات خيري")
    for msg in st.session_state.chat:
        st.markdown(f"<div style='background:rgba(255,0,0,0.1); padding:15px; border-radius:10px; margin:10px 0;'><b>{msg['user']}</b>: {msg['msg']}</div>", unsafe_allow_html=True)
    with st.form("sov_chat", clear_on_submit=True):
        u_in = st.text_input("أدخل الرسالة...")
        if st.form_submit_button("إرسال") and u_in:
            st.session_state.chat.append({"user": "KHAIRY", "msg": u_in})
            st.rerun()

# --- 7. FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#ff0000; font-weight:bold; font-size:1.5rem;'>KHAIRY ABDUL WAHID - THE SOVEREIGN CORE © 2026</p>", unsafe_allow_html=True)
