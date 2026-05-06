import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Dark Amtihan - الشامل", layout="wide")

# التصميم بالأحمر والأسود
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #ff0000 !important; text-align: center; }
    [data-testid="stSidebar"] { background-color: #0b0b0b; border-right: 2px solid #ff0000; }
    .stExpander { background-color: #151515; border: 1px solid #333; border-radius: 10px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 15px; margin: 15px 0; text-align: right; }
    .a-box { background-color: #1f1f1f; padding: 15px; border-radius: 5px; color: #e0e0e0; text-align: right; direction: rtl; border: 1px dashed #444; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# شريط التحميل
if 'loaded' not in st.session_state:
    progress_text = "جاري استخراج كافة الأسئلة من الصور..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    st.session_state['loaded'] = True

st.title("🔥 Welcome to Dark Amtihan 🔥")
st.sidebar.header("الاختيار")
subject = st.sidebar.selectbox("اختر المادة:", ["أساسيات الشبكات (كاملة)", "برمجة ++C"])

if subject == "أساسيات الشبكات (كاملة)":
    st.header("🌐 مراجعة شاملة لأساسيات الشبكات")

    # الصورة 1: أنواع الشبكات [لقطة الشاشة 2026-05-06 022703.png]
    with st.expander("📁 1. أنواع الشبكات وتحدياتها"):
        data = [
            ("1- اذكر ثلاثة من أنواع شبكات الانترنت", "1. LAN (محلية) | 2. WAN (واسعة) | 3. MAN (مدنية)"),
            ("2- اذكر ثلاثة من استخدامات شبكات الانترنت", "1. التواصل والبريد | 2. البحث العلمي | 3. التجارة الإلكترونية"),
            ("3- اذكر ثلاثة من التحديات التي تواجه شبكات الانترنت", "1. الأمن والخصوصية | 2. استدامة الطاقة | 3. التكيف مع التطور التكنولوجي"),
            ("4- اذكر خصائص الشبكات المحلية LAN", "تغطي مساحة محدودة، سرعة عالية، وتملكها جهة واحدة"),
            ("5- اذكر خصائص الشبكات الواسعة WAN", "مساحة جغرافية كبيرة، سرعة أقل، وتعتمد على مزودي خدمة"),
            ("6- اذكر مزايا شبكات الحوسبة السحابية", "المرونة، توفير التكلفة، وسهولة التوسع")
        ]
        for q, a in data:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # الصورة 2: بروتوكولات TCP/UDP [لقطة الشاشة 2026-05-06 022726.png]
    with st.expander("📁 2. بروتوكولات IP, TCP, UDP"):
        data2 = [
            ("1- اذكر ثلاثة من وظائف بروتوكول IP", "1. العنونة المنطقية | 2. التوجيه | 3. تجزئة البيانات"),
            ("2- اذكر ثلاثة من وظائف بروتوكول TCP", "1. التحكم في التدفق | 2. كشف الأخطاء | 3. ترتيب الحزم"),
            ("3- اذكر ثلاثة من مزايا بروتوكول TCP", "1. الموثوقية | 2. الاتصال الموجه | 3. إدارة الازدحام"),
            ("4- اذكر ثلاثة من تحديات بروتوكول TCP", "1. التأخير (Latency) | 2. عبء البيانات (Overhead) | 3. تعقيد الإدارة"),
            ("5- اذكر ثلاثة من خصائص بروتوكول UDP", "1. سريع جداً | 2. غير موجه للاتصال | 3. لا يضمن الوصول"),
            ("6- اذكر ثلاثة من مزايا بروتوكول UDP", "1. كفاءة عالية | 2. تأخير قليل | 3. مناسب للبث المباشر"),
            ("7- اذكر ثلاثة من عيوب بروتوكول UDP", "1. فقدان البيانات | 2. عدم الترتيب | 3. لا يوجد تحكم بالازدحام"),
            ("8- اذكر ثلاثة من استخدامات بروتوكول UDP", "1. VoIP | 2. الألعاب أونلاين | 3. البث المباشر"),
            ("9- اذكر البروتوكولات المستخدمة في البريد الالكتروني", "1. SMTP | 2. IMAP | 3. POP3")
        ]
        for q, a in data2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # الصورة 3 و 4 و 5: النماذج والطبقات [لقطة الشاشة 2026-05-06 023129.png وما بعدها]
    with st.expander("📁 3. نماذج OSI و TCP/IP"):
        data3 = [
            ("1- اذكر تحديات النماذج الطبقية", "التعقيد في الإدارة، العبء على المعالج، وتأخير التغليف"),
            ("2- اذكر مزايا النماذج الطبقية", "سهولة التطوير، توافق الأجهزة، وتبسيط التعلم"),
            ("4- اذكر طبقات نموذج OSI", "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق"),
            ("5- اذكر طبقات نموذج TCP/IP", "الوصول للشبكة، الإنترنت، النقل، التطبيق"),
            ("1- اذكر مهام الطبقة الفيزيائية", "تمثيل البيانات (البتات)، تحديد سرعة النقل، والمواصفات الميكانيكية"),
            ("4- اذكر مهام طبقة ربط البيانات", "عنونة الـ MAC، كشف أخطاء الإطار، والتحكم بالوصول للوسط"),
            ("6- اذكر مهام طبقة الشبكة", "توجيه الحزم (Routing)، العنونة المنطقية IP، واختيار أفضل مسار"),
            ("7- اذكر مهام طبقة النقل", "تقسيم البيانات، التحكم في التدفق، وضمان الموثوقية")
        ]
        for q, a in data3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # الصورة 6 و 7: HTTP و HTTPS و SMTP [لقطة الشاشة 2026-05-06 023404.png وما بعدها]
    with st.expander("📁 4. بروتوكولات التطبيقات (HTTP, HTTPS, FTP, SMTP)"):
        data4 = [
            ("1- اذكر بروتوكولات طبقة التطبيق", "HTTP, HTTPS, FTP, SMTP, DNS"),
            ("2- اذكر أنواع رؤوس HTTP", "General Headers, Request Headers, Response Headers"),
            ("6- اذكر مزايا HTTP", "بسيط، سريع، ويدعم أنواعاً متعددة من الوسائط"),
            ("8- اذكر عيوب HTTP", "غير مشفر (غير آمن)، وانتحال الشخصية ممكن"),
            ("1- اذكر مزايا HTTPS", "التشفير (SSL/TLS)، حماية الخصوصية، وموثوقية الهوية"),
            ("3- اذكر مزايا بروتوكول FTP", "نقل الملفات الضخمة، التحكم بالوصول، ودعم الاستئناف"),
            ("5- اذكر مزايا SMTP", "سهولة الإعداد، الموثوقية في إرسال الرسائل"),
            ("7- اذكر مزايا IMAP", "تزامن الرسائل على عدة أجهزة، وإدارة البريد على الخادم")
        ]
        for q, a in data4:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # الصورة 8 و 9: المنافذ والمصافحة [لقطة الشاشة 2026-05-06 023504.png وما بعدها]
    with st.expander("📁 5. المنافذ والمصافحة (Handshake)"):
        data5 = [
            ("3- اذكر خصائص المنافذ", "رقم فريد (16 بت)، يحدد التطبيق المستهدف، ويميز بين الجلسات"),
            ("4- اذكر أنواع المنافذ", "المعروفة (0-1023)، المسجلة (1024-49151)، الديناميكية (49152-65535)"),
            ("2- اذكر استخدامات المصافحة", "تنسيق بدء الاتصال، الاتفاق على المعايير، وضمان جاهزية الطرفين"),
            ("3- اذكر مزايا المصافحة", "تمنع فقدان البيانات في البداية، وتضمن أمن الاتصال")
        ]
        for q, a in data5:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # الصورة 10: الكابلات [لقطة الشاشة 2026-05-06 023639.png]
    with st.expander("📁 6. الكابلات والوسائط"):
        data6 = [
            ("1- اذكر أنواع الكابلات المستخدمة", "الملتوية (Twisted Pair)، المحورية (Coaxial)، الألياف الضوئية"),
            ("3- اذكر مزايا الكابلات الملتوية", "رخيصة الثمن، سهلة التركيب، ومرنة"),
            ("4- اذكر عيوب الكابلات الملتوية", "تتأثر بالتداخل، ومحدودة المسافة"),
            ("7- اذكر مزايا الكابلات المحورية", "أقل تأثراً بالتداخل من الملتوية، وتغطي مسافات أكبر قليلاً"),
            ("10- اذكر مزايا الألياف الضوئية", "سرعة هائلة جداً، مسافات طويلة، ولا تتأثر بالكهرباء تماماً")
        ]
        for q, a in data6:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

else:
    st.header("💻 برمجة ++C")
    # هنا أضف كل أسئلة C++ التي لديك سابقاً بنفس التنسيق
    with st.expander("أساسيات اللغة"):
        st.markdown('<div class="q-box">س: ما هي ميزات ++C؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: سريعة، تدعم البرمجة الكائنية، وقريبة من العتاد.</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("إعداد: خيري عبد الواحد")
