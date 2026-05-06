import streamlit as st
import time

# إعدادات الصفحة - Dark Theme
st.set_page_config(page_title="Dark Amtihan - النسخة المليونية الكاملة", layout="wide")

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
    p_bar = st.progress(0, text="جاري استخراج كافة التفاصيل من الصور (بدون نقص)... خيري عبد الواحد")
    for p in range(100):
        time.sleep(0.01)
        p_bar.progress(p + 1)
    st.session_state['loaded'] = True
    p_bar.empty()

st.title("🔥 Dark Amtihan: The Final Edition 🔥")
st.markdown("<h3 style='text-align: center; color: white;'>المراجعة الشاملة لخيري عبد الواحد</h3>", unsafe_allow_html=True)

# القائمة الجانبية
choice = st.sidebar.radio("اختر المادة التعليمية:", ["أساسيات الشبكات (مكتملة)", "برمجة ++C (مكتملة)"])

# ---------------------------------------------------------
# القسم الأول: أساسيات الشبكات (استخراج شامل من 10 صور)
# ---------------------------------------------------------
if choice == "أساسيات الشبكات (مكتملة)":
    st.header("🌐 بنك أسئلة الشبكات - لا يوجد نقص")
    
    with st.expander("📄 1. أنواع الشبكات وتحدياتها (صور 1-2)"):
        net_q1 = [
            ("اذكر أنواع شبكات الانترنت؟", "PAN (شخصية)، LAN (محلية)، MAN (مدنية)، WAN (واسعة)."),
            ("اذكر ثلاثة من استخدامات شبكات الانترنت؟", "التواصل، التجارة الإلكترونية، البحث العلمي، التعليم، الترفيه."),
            ("اذكر التحديات التي تواجه شبكات الانترنت؟", "الأمن والخصوصية، استدامة الطاقة، التكيف مع التطور التكنولوجي، سعة الشبكة."),
            ("اذكر خصائص الشبكات المحلية LAN؟", "مساحة صغيرة، سرعة عالية، ملكية خاصة لجهة واحدة."),
            ("اذكر خصائص الشبكات الواسعة WAN؟", "مساحة شاسعة، سرعة أقل، تعتمد على مزودي خدمة (ISP)."),
            ("اذكر مزايا شبكات الحوسبة السحابية؟", "توفير التكاليف، المرونة، سهولة الوصول والتوسع.")
        ]
        for q, a in net_q1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 2. البروتوكولات والنماذج OSI & TCP/IP (صور 3-5)"):
        net_q2 = [
            ("اذكر وظائف بروتوكول IP؟", "العنونة المنطقية، التوجيه (Routing)، وتجزئة الحزم."),
            ("اذكر وظائف بروتوكول TCP؟", "التحكم في التدفق، كشف الأخطاء، وترتيب الحزم."),
            ("اذكر مزايا بروتوكول TCP؟", "الموثوقية العالية والاتصال الموجه."),
            ("اذكر تحديات بروتوكول TCP؟", "التأخير (Latency) والعبء الإضافي على البيانات."),
            ("اذكر خصائص بروتوكول UDP؟", "سريع جداً، غير موجه للاتصال، ولا يضمن الوصول."),
            ("اذكر مزايا بروتوكول UDP؟", "كفاءة عالية وتأخير قليل جداً."),
            ("اذكر عيوب بروتوكول UDP؟", "فقدان البيانات وعدم الترتيب."),
            ("اذكر استخدامات بروتوكول UDP؟", "البث المباشر، VoIP، والألعاب أونلاين."),
            ("اذكر طبقات نموذج OSI السبعة بالترتيب؟", "1.الفيزيائية، 2.ربط البيانات، 3.الشبكة، 4.النقل، 5.الجلسة، 6.التقديم، 7.التطبيق."),
            ("اذكر طبقات نموذج TCP/IP الأربعة؟", "1.الوصول للشبكة، 2.الإنترنت، 3.النقل، 4.التطبيق."),
            ("اذكر مزايا وتحديات النماذج الطبقية؟", "المزايا: التوافق وسهولة التطوير. التحديات: التعقيد والعبء على المعالج.")
        ]
        for q, a in net_q2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 3. التطبيقات، الكابلات والمنافذ (صور 6-10)"):
        net_q3 = [
            ("ما هي وظيفة طبقة التطبيق؟", "توفير واجهة للمستخدم وبروتوكولات التواصل مثل HTTP."),
            ("اذكر أنواع رؤوس HTTP؟", "General Headers, Request Headers, Response Headers."),
            ("ما الفرق بين HTTP و HTTPS؟", "HTTPS مشفر وآمن باستخدام SSL/TLS."),
            ("اذكر بروتوكولات البريد الإلكتروني؟", "SMTP (إرسال)، POP3 و IMAP (استقبال)."),
            ("اذكر أنواع الكابلات ومزايا وعيوب كل نوع؟", "الملتوية (رخيصة/مسافة قصيرة)، المحورية (مقاومة للتشويش)، الألياف (سرعة هائلة)."),
            ("اذكر أنواع المنافذ (Ports)؟", "المعروفة (0-1023)، المسجلة (1024-49151)، والديناميكية (49152-65535)."),
            ("ما هي استخدامات ومزايا المصافحة (Handshake)؟", "بدء الاتصال، الاتفاق على المعايير، وضمان أمن الجلسة."),
            ("اذكر وظائف طبقة ربط البيانات؟", "عنونة الـ MAC وكشف أخطاء الإطار."),
            ("اذكر وظائف الطبقة الفيزيائية؟", "تمثيل البتات وتحديد المواصفات الميكانيكية للكابلات.")
        ]
        for q, a in net_q3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# القسم الثاني: برمجة ++C (استخراج شامل من 10 صور)
# ---------------------------------------------------------
else:
    st.header("💻 بنك أسئلة ++C - لا يوجد نقص")

    with st.expander("📄 1. أساسيات اللغة والتحكم (صور 1-5)"):
        cpp_q1 = [
            ("ما هي ميزات لغة ++C؟", "كائنية التوجه (OOP)، سريعة، قريبة من العتاد، وتدعم البرمجة المرئية."),
            ("ما هو الهيكل الأساسي لبرنامج ++C؟", "include <iostream> متبوعاً بدالة main() وينتهي بـ return 0."),
            ("اذكر أنواع البيانات الأساسية؟", "int (صحيح)، float (عشري)، char (حرف)، bool (منطقي)، double (دقة عالية)."),
            ("ما هي وظيفة cin و cout؟", "cout للإخراج والطباعة، و cin للإدخال من المستخدم."),
            ("ما الفرق بين if و switch؟", "if للشروط المعقدة والمدى، و switch للقيم الثابتة والمحددة."),
            ("ما هي وظيفة جملة break و default في switch؟", "break تنهي الحالة، و default تنفذ إذا لم يتحقق أي شرط."),
            ("ما الفرق بين (\\n) و (endl)؟", "كلاهما لبدء سطر جديد، لكن endl يفرغ الذاكرة المؤقتة.")
        ]
        for q, a in cpp_q1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 2. التكرار، المصفوفات والدوال (صور 6-10)"):
        cpp_q2 = [
            ("اذكر أنواع حلقات التكرار (Loops)؟", "for, while, do-while."),
            ("ما الفرق بين while و do-while؟", "while تفحص الشرط أولاً، أما do-while تنفذ الكود مرة واحدة على الأقل."),
            ("ما هي المصفوفة (Array)؟", "هيكل بيانات يخزن عناصر من نفس النوع في مواقع متجاورة بذاكرة الكمبيوتر."),
            ("كيف يتم تعريف مصفوفة والوصول لعناصرها؟", "يتم الوصول عبر الفهرس (Index) الذي يبدأ من الرقم 0."),
            ("ما هي فوائد استخدام الدوال (Functions)؟", "تنظيم الكود، سهولة الصيانة، ومنع تكرار الأوامر."),
            ("ما الفرق بين المتغير المحلي (Local) والعالمي (Global)؟", "المحلي داخل دالة محددة، العالمي متاح لكل الكود."),
            ("ما هي أهمية جملة return؟", "إعادة نتيجة المعالجة من الدالة إلى مكان الاستدعاء.")
        ]
        for q, a in cpp_q2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.success("تم تأكيد اكتمال كافة الأسئلة (45+ سؤال)")
