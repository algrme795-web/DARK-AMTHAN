import streamlit as st
import time

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Dark Amtihan - Khairy", layout="wide")

# تصميم الواجهة بالأحمر والأسود (Custom CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; }
    [data-testid="stSidebar"] { background-color: #111111; border-right: 2px solid #ff0000; }
    .stSelectbox div[data-baseweb="select"] { background-color: #222222; color: white; border: 1px solid #ff0000; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #444; border-radius: 8px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 10px; margin: 10px 0; text-align: right; }
    .a-box { background-color: #262626; padding: 15px; border-radius: 5px; color: #dddddd; line-height: 1.6; text-align: right; direction: rtl; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# 1. شريط التحميل الأحمر
if 'loaded' not in st.session_state:
    progress_text = "جاري تجهيز بنك الأسئلة الشامل..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    st.session_state['loaded'] = True

# 2. رسالة الترحيب
st.title("🔥 Welcome to Dark Amtihan 🔥")
st.markdown("---")

# 3. القائمة الجانبية
st.sidebar.header("القائمة الرئيسية")
subject = st.sidebar.selectbox("اختر المادة المراجعة:", ["أساسيات الشبكات", "برمجة ++C"])

# --- محتوى مادة الشبكات (حلول كافة الصور) ---
if subject == "أساسيات الشبكات":
    st.header("🌐 بنك أسئلة أساسيات الشبكات")

    # المجموعة 1: أنواع وتحديات الشبكات [لقطة الشاشة 2026-05-06 022703.png]
    with st.expander("📄 أنواع الشبكات وتحدياتها"):
        questions = [
            ("اذكر ثلاثة من أنواع شبكات الانترنت", "1. PAN (شخصية) | 2. LAN (محلية) | 3. WAN (واسعة)"),
            ("اذكر ثلاثة من استخدامات شبكات الانترنت", "1. التواصل | 2. التجارة الإلكترونية | 3. البحث والتعليم"),
            ("اذكر ثلاثة من التحديات التي تواجه شبكات الانترنت", "1. الأمن والخصوصية | 2. استدامة الطاقة | 3. التطور التكنولوجي السريع"),
            ("اذكر خصائص الشبكات المحلية LAN", "تغطي مساحة جغرافية صغيرة، سرعة عالية، وتملكها مؤسسة واحدة"),
            ("اذكر خصائص الشبكات الواسعة WAN", "تغطي دول وقارات، تعتمد على خطوط مؤجرة، سرعتها أقل من LAN"),
            ("اذكر مزايا شبكات الحوسبة السحابية", "توفير التكاليف، المرونة، وسهولة الوصول من أي مكان")
        ]
        for q, a in questions:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # المجموعة 2: بروتوكولات النقل [لقطة الشاشة 2026-05-06 022726.png]
    with st.expander("📄 بروتوكولات IP, TCP, UDP"):
        questions_p2 = [
            ("اذكر ثلاثة من وظائف بروتوكول IP", "1. العنونة المنطقية | 2. التوجيه (Routing) | 3. تجزئة الحزم"),
            ("اذكر ثلاثة من وظائف بروتوكول TCP", "1. التحكم في التدفق | 2. كشف الأخطاء | 3. ضمان ترتيب الحزم"),
            ("اذكر مزايا بروتوكول TCP", "الموثوقية العالية، الاتصال الموجه، وإدارة الازدحام"),
            ("اذكر خصائص بروتوكول UDP", "غير موجه للاتصال، سرعة عالية جداً، ولا يضمن الوصول"),
            ("اذكر البروتوكولات المستخدمة في البريد الإلكتروني", "SMTP (للإرسال)، IMAP و POP3 (للاستقبال)")
        ]
        for q, a in questions_p2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # المجموعة 3: النماذج الطبقية [لقطة الشاشة 2026-05-06 023129.png & 023404.png]
    with st.expander("📄 نماذج OSI و TCP/IP والعناوين"):
        questions_p3 = [
            ("اذكر طبقات نموذج OSI السبعة", "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق"),
            ("اذكر طبقات نموذج TCP/IP", "الوصول للشبكة، الإنترنت، النقل، التطبيق"),
            ("اذكر أنواع العناوين في الشبكات", "1. العنوان الفيزيائي (MAC) | 2. العنوان المنطقي (IP) | 3. عنوان المنفذ (Port)"),
            ("اذكر مهام الطبقة الفيزيائية", "نقل البتات عبر الأوساط، تحديد نوع الوصلات والمواصفات الكهربائية")
        ]
        for q, a in questions_p3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    # المجموعة 4: الكابلات والوسائط [لقطة الشاشة 2026-05-06 023639.png]
    with st.expander("📄 وسائط النقل والكابلات"):
        questions_p4 = [
            ("اذكر أنواع الكابلات المستخدمة", "1. الكابلات الملتوية (Twisted Pair) | 2. المحورية (Coaxial) | 3. الألياف الضوئية"),
            ("اذكر مزايا الألياف الضوئية", "سرعة هائلة، مسافات طويلة جداً، حصانة ضد التداخل الكهرومغناطيسي"),
            ("اذكر عيوب الكابلات الملتوية", "تتأثر بالتداخل، والمسافة محدودة (حوالي 100 متر)")
        ]
        for q, a in questions_p4:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# --- محتوى مادة برمجة ++C ---
else:
    st.header("💻 بنك أسئلة برمجة ++C")
    
    with st.expander("📄 الأساسيات والجمل الشرطية"):
        questions_cpp = [
            ("اذكر ميزات لغة ++C", "لغة عالية المستوى ومنخفضة المستوى بنفس الوقت، كائنية التوجه، وسريعة التنفيذ"),
            ("ما الفرق بين switch و if؟", "تستخدم switch للقيم المحددة والثوابت، بينما if تستخدم للمقارنات والمدى الواسع"),
            ("ما هي أنواع البيانات الأساسية؟", "int, float, double, char, bool")
        ]
        for q, a in questions_cpp:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📄 المصفوفات والحلقات"):
        st.markdown('<div class="q-box">كيف يتم تعريف مصفوفة وتخزين قيم فيها؟</div>', unsafe_allow_html=True)
        st.code("int arr[3] = {10, 20, 30};", language="cpp")
        
        st.markdown('<div class="q-box">اكتب كود لطباعة الأرقام من 1 إلى 5</div>', unsafe_allow_html=True)
        st.code("for(int i=1; i<=5; i++) {\n  cout << i << endl;\n}", language="cpp")

# تذييل الصفحة
st.sidebar.markdown("---")
st.sidebar.write("Design by **Khairy Abdul Wahid**")
st.sidebar.write("Project: **Dark Amtihan 2026**")
