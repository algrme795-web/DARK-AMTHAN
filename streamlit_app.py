import streamlit as st
import time

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Dark Amtihan - Khairy", layout="wide")

# تصميم الواجهة بالأحمر والأسود (Custom CSS)
st.markdown("""
    <style>
    /* الخلفية العامة */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* العناوين والقوائم */
    h1, h2, h3 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; }
    
    /* شريط التمرير الجانبي */
    [data-testid="stSidebar"] { background-color: #111111; border-right: 2px solid #ff0000; }
    
    /* الأزرار وصناديق الخيارات */
    .stSelectbox div[data-baseweb="select"] { background-color: #222222; color: white; border: 1px solid #ff0000; }
    
    /* تصميم الـ Expanders (الأسئلة) */
    .stExpander { background-color: #1a1a1a; border: 1px solid #444; border-radius: 8px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 10px; margin: 10px 0; }
    .a-box { background-color: #262626; padding: 15px; border-radius: 5px; color: #dddddd; line-height: 1.6; }
    
    /* شريط التحميل */
    .stProgress > div > div > div > div { background-color: #ff0000; }
    
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# 1. شريط التحميل الأحمر (يظهر مرة واحدة عند التشغيل)
if 'loaded' not in st.session_state:
    progress_text = "جاري تحضير أسئلة Dark Amtihan..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    st.toast("Welcome to Dark Amtihan", icon="🔥")
    st.session_state['loaded'] = True

# 2. رسالة الترحيب
st.title("🔥 Welcome to Dark Amtihan 🔥")
st.markdown("---")

# 3. القائمة الجانبية لاختيار المادة
st.sidebar.header("لوحة التحكم")
subject = st.sidebar.selectbox("اختر المادة التي تريد مراجعتها:", ["أساسيات الشبكات", "برمجة ++C"])

# --- محتوى مادة الشبكات (الصور الجديدة) ---
if subject == "أساسيات الشبكات":
    st.header("🌐 مراجعة أساسيات الشبكات")
    
    with st.expander("📄 المجموعة 1: أنواع وتحديات الشبكات"):
        st.markdown('<div class="q-box">1- اذكر ثلاثة من أنواع شبكات الانترنت.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. LAN (شبكة محلية) | 2. WAN (شبكة واسعة) | 3. MAN (شبكة مدنية).</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="q-box">3- اذكر ثلاثة من التحديات التي تواجه شبكات الانترنت.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. الأمن والخصوصية | 2. استدامة الطاقة | 3. التكيف مع التقنيات الحديثة (مثل 5G والذكاء الاصطناعي).</div>', unsafe_allow_html=True)

    with st.expander("📄 المجموعة 2: البروتوكولات (IP, TCP, UDP)"):
        st.markdown('<div class="q-box">1- اذكر ثلاثة من وظائف بروتوكول IP.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. العنونة (Addressing) | 2. التوجيه (Routing) | 3. تجزئة البيانات.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="q-box">2- اذكر ثلاثة من وظائف بروتوكول TCP.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. ضمان وصول البيانات | 2. التحكم في التدفق | 3. إعادة ترتيب الحزم.</div>', unsafe_allow_html=True)

    with st.expander("📄 المجموعة 3: النماذج الطبقية (OSI & TCP/IP)"):
        st.markdown('<div class="q-box">4- اذكر ثلاثة من طبقات نموذج OSI.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. الطبقة الفيزيائية | 2. طبقة ربط البيانات | 3. طبقة الشبكة.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="q-box">6- اذكر ثلاثة من أنواع العناوين في الشبكات.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. عنوان الفيزيائي (MAC Address) | 2. عنوان المنطقي (IP Address) | 3. عنوان المنفذ (Port Number).</div>', unsafe_allow_html=True)

    with st.expander("📄 المجموعة 4: الكابلات والوسائط"):
        st.markdown('<div class="q-box">1- اذكر ثلاثة من أنواع الكابلات المستخدمة في الشبكات.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. الكابلات الملتوية (Twisted Pair) | 2. الكابلات المحورية (Coaxial) | 3. الألياف الضوئية (Fiber Optics).</div>', unsafe_allow_html=True)

# --- محتوى مادة ++C ---
else:
    st.header("💻 مراجعة لغة ++C")
    
    with st.expander("📄 المجموعة 1: أساسيات اللغة"):
        st.markdown('<div class="q-box">1- اذكر ثلاثة من ميزات لغات ++C.</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-box">ج: 1. كائنية التوجه | 2. سريعة الأداء | 3. قريبة من العتاد.</div>', unsafe_allow_html=True)

    with st.expander("📄 المجموعة 2: جمل التحكم والحلقات"):
        st.markdown('<div class="q-box">1- ما هو الفرق بين while و do-while؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: حلقة do-while تنفذ الكود مرة واحدة على الأقل قبل فحص الشرط.</div>', unsafe_allow_html=True)

    with st.expander("📄 المجموعة 3: المصفوفات والدوال"):
        st.markdown('<div class="q-box">2- قم بتعريف مصفوفة ثنائية 4 صفوف و 3 أعمدة.</div>', unsafe_allow_html=True)
        st.code("int matrix[4][3];", language="cpp")

# تذييل الصفحة
st.sidebar.markdown("---")
st.sidebar.write("Developed by **Khairy Abdul Wahid**")
