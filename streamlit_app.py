import streamlit as st
import time

# إعدادات الصفحة - Dark Theme
st.set_page_config(page_title="Dark Amtihan - النسخة المكتملة 100%", layout="wide")

# تصميم الواجهة بالأحمر والأسود
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; text-shadow: 2px 2px #550000; }
    [data-testid="stSidebar"] { background-color: #0b0b0b; border-right: 2px solid #ff0000; }
    .stExpander { background-color: #121212; border: 1px solid #ff0000; border-radius: 10px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 5px solid #ff0000; padding-right: 15px; margin: 15px 0; text-align: right; direction: rtl; font-size: 1.1em; }
    .a-box { background-color: #1a1a1a; padding: 15px; border-radius: 5px; color: #ffffff; text-align: right; direction: rtl; border: 1px solid #333; line-height: 1.8; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    code { color: #00ff00 !important; background-color: #222 !important; }
    </style>
    """, unsafe_allow_html=True)

# شريط التحميل (Loader)
if 'loaded' not in st.session_state:
    p_bar = st.progress(0, text="جاري استخراج كافة البيانات من 20 صورة... خيري عبد الواحد")
    for p in range(100):
        time.sleep(0.01)
        p_bar.progress(p + 1)
    st.session_state['loaded'] = True
    p_bar.empty()

st.title("🔥 بنك الأسئلة الاسترشادية الشامل 🔥")
st.markdown("<h3 style='text-align: center; color: white;'>إعداد: خيري عبد الواحد</h3>", unsafe_allow_html=True)

# القائمة الجانبية
choice = st.sidebar.radio("اختر المادة التعليمية:", ["أساسيات الشبكات (10 صور)", "برمجة ++C (10 صور)"])

# ---------------------------------------------------------
# القسم الأول: أساسيات الشبكات (حلول الـ 10 صور كاملة)
# ---------------------------------------------------------
if choice == "أساسيات الشبكات (10 صور)":
    st.header("🌐 مراجعة منهج الشبكات")
    
    with st.expander("📄 الجزء الأول: المفاهيم والأنواع والطبقات"):
        data_net1 = [
            ("اذكر أنواع شبكات الانترنت؟", "PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."),
            ("اذكر استخدامات شبكات الانترنت؟", "التواصل، التجارة الإلكترونية، البحث والتعليم، الترفيه، العمل عن بعد."),
            ("اذكر التحديات التي تواجه شبكات الانترنت؟", "الأمن والخصوصية، استدامة الطاقة، التكيف مع التطور، سعة الشبكة."),
            ("ما هي خصائص الشبكات المحلية LAN؟", "مساحة صغيرة، سرعة نقل بيانات عالية، وتملكها جهة واحدة."),
            ("ما هي خصائص الشبكات الواسعة WAN؟", "مساحة جغرافية شاسعة، سرعة أقل، وتعتمد على مزودي خدمة خارجيين."),
            ("اذكر مزايا شبكات الحوسبة السحابية؟", "توفير التكاليف، المرونة العالية، سهولة الوصول من أي مكان."),
            ("اذكر طبقات نموذج OSI السبعة؟", "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق."),
            ("اذكر طبقات نموذج TCP/IP؟", "الوصول للشبكة، الإنترنت، النقل، التطبيق."),
            ("ما هي مزايا وتحديات النماذج الطبقية؟", "المزايا: التوافق وسهولة التطوير. التحديات: التعقيد والعبء الإضافي.")
        ]
        for q, a in data_net1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 الجزء الثاني: البروتوكولات، الكابلات والمنافذ"):
        data_net2 = [
            ("اذكر وظائف بروتوكول IP؟", "العنونة المنطقية، التوجيه (Routing)، وتجزئة الحزم."),
            ("اذكر وظائف ومزايا وتحديات بروتوكول TCP؟", "الوظائف: التحكم بالتدفق وكشف الأخطاء. المزايا: الموثوقية. التحديات: البطء بسبب التأكيد."),
            ("اذكر خصائص ومزايا وعيوب واستخدامات بروتوكول UDP؟", "الخصائص: غير موجه للاتصال. المزايا: سريع. العيوب: غير موثوق. الاستخدام: الألعاب والبث."),
            ("ما الفرق بين HTTP و HTTPS؟", "HTTPS هو النسخة المشفرة والآمنة باستخدام SSL/TLS."),
            ("اذكر بروتوكولات البريد الإلكتروني؟", "SMTP (إرسال)، POP3 و IMAP (استقبال)."),
            ("اذكر أنواع الكابلات ومزايا وعيوب كل نوع؟", "الملتوية (رخيصة/مسافة قصيرة)، المحورية (مقاومة للتشويش)، الألياف (سريعة جداً/غالية)."),
            ("اذكر أنواع المنافذ (Ports)؟", "المعروفة (0-1023)، المسجلة (1024-49151)، والديناميكية."),
            ("ما هي استخدامات ومزايا المصافحة (Handshake)؟", "تنسيق بدء الاتصال، ضمان أمن الجلسة، والاتفاق على المعايير.")
        ]
        for q, a in data_net2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# القسم الثاني: برمجة ++C (حلول الـ 10 صور كاملة)
# ---------------------------------------------------------
else:
    st.header("💻 مراجعة منهج برمجة ++C")

    with st.expander("📄 الجزء الأول: الأساسيات والجمل الشرطية"):
        data_cpp1 = [
            ("ما هي ميزات لغة ++C؟", "لغة قوية، كائنية التوجه (OOP)، سريعة، وتدعم البرمجة منخفضة المستوى."),
            ("اذكر أنواع البيانات (Data Types)؟", "int, float, double, char, string, bool."),
            ("ما هي وظيفة cin و cout؟", "cout للإخراج (الطباعة)، و cin للإدخال من المستخدم."),
            ("ما الفرق بين if و switch؟", "if تستخدم للشروط المنطقية، و switch تستخدم للمفاضلة بين قيم ثابتة محددة."),
            ("اذكر أهمية جملة break؟", "تستخدم للخروج من جملة switch أو إنهاء حلقة تكرارية فوراً."),
            ("ما هو الفرق بين (\\n) و (endl)؟", "كلاهما لبدء سطر جديد، لكن endl يقوم بتفريغ الذاكرة المؤقتة (Buffer).")
        ]
        for q, a in data_cpp1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 الجزء الثاني: الحلقات، المصفوفات والدوال"):
        data_cpp2 = [
            ("اذكر أنواع حلقات التكرار (Loops)؟", "for (عدد محدد)، while (شرط مستمر)، do-while (تنفذ مرة على الأقل)."),
            ("ما هي المصفوفة (Array)؟", "مجموعة عناصر من نفس النوع تُخزن في الذاكرة تحت اسم واحد وفهرس يبدأ من 0."),
            ("كيف يتم تعريف واستدعاء دالة (Function)؟", "يتم تعريفها خارج main وتستدعى باسمها لتنفيذ كود محدد ومنع التكرار."),
            ("ما هو الفرق بين المتغير المحلي (Local) والعالمي (Global)؟", "المحلي يُعرف داخل دالة، والعالمي يُعرف في بداية الكود ومتاح للجميع."),
            ("اذكر أهمية جملة return في الدوال؟", "إعادة قيمة ناتجة عن معالجة الدالة إلى المكان الذي استدعيت منه.")
        ]
        for q, a in data_cpp2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("تم جرد 20 صورة (10 شبكات + 10 برمجة) بنجاح كامل.")
