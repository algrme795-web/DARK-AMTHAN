import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Dark Amtihan - النسخة المليونية", layout="wide")

# تصميم الواجهة الاحترافي (أحمر وأسود)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; }
    [data-testid="stSidebar"] { background-color: #0b0b0b; border-right: 2px solid #ff0000; }
    .stExpander { background-color: #151515; border: 1px solid #333; border-radius: 10px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 15px; margin: 15px 0; text-align: right; direction: rtl; }
    .a-box { background-color: #1f1f1f; padding: 15px; border-radius: 5px; color: #e0e0e0; text-align: right; direction: rtl; border: 1px dashed #444; line-height: 1.6; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    code { color: #00ff00 !important; }
    </style>
    """, unsafe_allow_html=True)

# شريط التحميل
if 'loaded' not in st.session_state:
    p_bar = st.progress(0, text="جاري جرد وحقن كافة الأسئلة التفصيلية (لا يوجد نقص)...")
    for p in range(100):
        time.sleep(0.01)
        p_bar.progress(p + 1)
    st.session_state['loaded'] = True
    p_bar.empty()

st.title("🔥 Dark Amtihan: Zero Omission 🔥")

# القائمة الجانبية
st.sidebar.title("الفهرس الشامل")
choice = st.sidebar.radio("اختر المادة:", ["الشبكات (كل الصور)", "برمجة ++C (كل الصور)"])

# --- قسم الشبكات الشامل جداً ---
if choice == "الشبكات (كل الصور)":
    st.header("🌐 بنك أسئلة الشبكات (مستخرج من 10 صور)")
    
    with st.expander("📁 الوحدة الأولى: مقدمة الشبكات والأنواع"):
        net_data = [
            ("1. اذكر ثلاثة من أنواع شبكات الانترنت؟", "PAN, LAN, MAN, WAN"),
            ("2. اذكر ثلاثة من استخدامات شبكات الانترنت؟", "التواصل، التجارة الإلكترونية، البحث والتعليم، الترفيه"),
            ("3. اذكر ثلاثة من التحديات التي تواجه شبكات الانترنت؟", "الأمن السيبراني، استدامة الطاقة، التكيف مع التطور"),
            ("4. اذكر خصائص الشبكات المحلية LAN؟", "مساحة صغيرة، سرعة عالية، ملكية خاصة"),
            ("5. اذكر خصائص الشبكات الواسعة WAN؟", "مساحة شاسعة، سرعة أقل، تعتمد على خطوط مؤجرة"),
            ("6. اذكر مزايا شبكات الحوسبة السحابية؟", "توفير التكاليف، المرونة، سهولة الوصول")
        ]
        for q, a in net_data:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 الوحدة الثانية: البروتوكولات والنماذج (TCP, UDP, OSI)"):
        net_data2 = [
            ("1. اذكر وظائف بروتوكول IP؟", "العنونة، التوجيه، التجزئة"),
            ("2. اذكر وظائف بروتوكول TCP؟", "التحكم في التدفق، كشف الأخطاء، ترتيب الحزم"),
            ("3. اذكر مزايا بروتوكول TCP؟", "الموثوقية، الاتصال الموجه"),
            ("4. اذكر تحديات بروتوكول TCP؟", "التأخير، حجم البيانات الإضافية"),
            ("5. اذكر خصائص بروتوكول UDP؟", "سرعة عالية، غير موجه للاتصال"),
            ("6. اذكر طبقات نموذج OSI؟", "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق"),
            ("7. اذكر طبقات نموذج TCP/IP؟", "الوصول للشبكة، الإنترنت، النقل، التطبيق"),
            ("8. اذكر البروتوكولات المستخدمة في البريد؟", "SMTP, IMAP, POP3")
        ]
        for q, a in net_data2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 الوحدة الثالثة: الوسائط، المنافذ، والتطبيقات"):
        net_data3 = [
            ("1. اذكر أنواع الكابلات ومزاياها؟", "الملتوية (رخيصة)، المحورية (متوسطة)، الألياف (سرعة هائلة)"),
            ("2. اذكر أنواع المنافذ (Ports)؟", "المعروفة (0-1023)، المسجلة، والديناميكية"),
            ("3. ما الفرق بين HTTP و HTTPS؟", "HTTPS يوفر التشفير والأمن عبر SSL/TLS"),
            ("4. اذكر مهام طبقة النقل؟", "تقسيم البيانات وإدارة الجلسات وسلامة الوصول"),
            ("5. اذكر استخدامات المصافحة (Handshake)؟", "بدء الاتصال والتأكد من جاهزية الطرفين")
        ]
        for q, a in net_data3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# --- قسم برمجة C++ الشامل جداً ---
else:
    st.header("💻 بنك أسئلة برمجة ++C (مستخرج من 10 صور)")
    
    with st.expander("📁 أساسيات اللغة والمتغيرات"):
        cpp_data = [
            ("1. ما هي ميزات لغة ++C؟", "كائنية التوجه، سريعة، تحكم مباشر في الذاكرة"),
            ("2. اذكر أنواع البيانات الأساسية؟", "int, float, double, char, bool"),
            ("3. ما هي وظيفة المكتبة <iostream>؟", "تسمح بعمليات الإدخال (cin) والإخراج (cout)"),
            ("4. كيف نكتب تعليقاً (Comment) في الكود؟", "نستخدم // للسطر الواحد أو /* */ للفقرة")
        ]
        for q, a in cpp_data:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 الجمل الشرطية والحلقات التكرارية"):
        cpp_data2 = [
            ("1. ما الفرق بين if البسيطة و else if؟", "if تفحص شرطاً واحداً، و else if تضيف شروطاً بديلة"),
            ("2. متى نستخدم جملة switch؟", "عند وجود خيارات ثابتة ومحددة بدلاً من الشروط المعقدة"),
            ("3. اذكر أنواع حلقات التكرار؟", "for (عدد محدد)، while (بناءً على شرط)، do-while (تنفذ مرة على الأقل)"),
            ("4. ما هي وظيفة break في الحلقات؟", "تستخدم للخروج من الحلقة فوراً قبل اكتمالها")
        ]
        for q, a in cpp_data2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المصفوفات والدوال"):
        cpp_data3 = [
            ("1. ما هي المصفوفة (Array)؟", "هيكل بيانات يخزن عناصر من نفس النوع في مواقع متجاورة"),
            ("2. كيف يتم الوصول لعنصر في المصفوفة؟", "عن طريق الفهرس (Index) الذي يبدأ من الصفر (0)"),
            ("3. ما هي أهمية الدوال (Functions)؟", "تقسيم الكود، سهولة القراءة، ومنع التكرار"),
            ("4. ما هو الفرق بين القيمة المرجعة (Return) والطباعة؟", "الـ Return تعيد قيمة لتستخدم في الكود، والطباعة تعرضها للمستخدم")
        ]
        for q, a in cpp_data3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.warning("ملاحظة: هذا البنك يحتوي على كافة تفاصيل الصور الـ 20.")
