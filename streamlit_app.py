import streamlit as st
import time

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Dark Amtihan - الشامل المحدث", layout="wide")

# تصميم الواجهة الاحترافي (أحمر وأسود)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #ff0000 !important; text-align: center; font-family: 'Arial Black'; }
    [data-testid="stSidebar"] { background-color: #0b0b0b; border-right: 2px solid #ff0000; }
    .stExpander { background-color: #151515; border: 1px solid #333; border-radius: 10px; margin-bottom: 10px; }
    .q-box { color: #ff0000; font-weight: bold; border-right: 4px solid #ff0000; padding-right: 15px; margin: 15px 0; text-align: right; }
    .a-box { background-color: #1f1f1f; padding: 15px; border-radius: 5px; color: #e0e0e0; text-align: right; direction: rtl; border: 1px dashed #444; }
    .stProgress > div > div > div > div { background-color: #ff0000; }
    div.stMarkdown { text-align: right; direction: rtl; }
    code { color: #00ff00 !important; } /* لون الكود البرمجي أخضر لسهولة القراءة */
    </style>
    """, unsafe_allow_html=True)

# شريط التحميل الأحمر عند الدخول
if 'loaded' not in st.session_state:
    progress_text = "جاري تحميل كافة الأسئلة (شبكات + ++C)..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    st.session_state['loaded'] = True

st.title("🔥 Welcome to Dark Amtihan 🔥")
st.markdown("---")

# القائمة الجانبية للتنقل بين المواد
st.sidebar.header("لوحة التحكم")
subject = st.sidebar.selectbox("اختر المادة المراد مراجعتها:", ["منهج أساسيات الشبكات", "منهج لغة ++C"])

# ==========================================
# قسم مادة الشبكات (حلول الـ 10 صور للشبكات)
# ==========================================
if subject == "منهج أساسيات الشبكات":
    st.header("🌐 مراجعة شاملة: أساسيات الشبكات")

    with st.expander("📁 المجموعة 1: أنواع وتحديات الشبكات"):
        net_q1 = [
            ("1- اذكر ثلاثة من أنواع شبكات الانترنت", "1. LAN (محلية) | 2. WAN (واسعة) | 3. MAN (مدنية)"),
            ("2- اذكر ثلاثة من استخدامات شبكات الانترنت", "1. التواصل والبريد | 2. البحث العلمي | 3. التجارة الإلكترونية"),
            ("3- اذكر ثلاثة من التحديات التي تواجه شبكات الانترنت", "1. الأمن والخصوصية | 2. استدامة الطاقة | 3. التكيف مع التطور التكنولوجي"),
            ("4- اذكر خصائص الشبكات المحلية LAN", "تغطي مساحة محدودة، سرعة عالية، وتملكها جهة واحدة"),
            ("5- اذكر خصائص الشبكات الواسعة WAN", "مساحة جغرافية كبيرة، سرعة أقل، وتعتمد على مزودي خدمة"),
            ("6- اذكر مزايا شبكات الحوسبة السحابية", "المرونة، توفير التكلفة، وسهولة التوسع")
        ]
        for q, a in net_q1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المجموعة 2: بروتوكولات النقل والمنافذ"):
        net_q2 = [
            ("1- اذكر ثلاثة من وظائف بروتوكول IP", "1. العنونة المنطقية | 2. التوجيه | 3. تجزئة البيانات"),
            ("2- اذكر ثلاثة من وظائف بروتوكول TCP", "1. التحكم في التدفق | 2. كشف الأخطاء | 3. ترتيب الحزم"),
            ("5- اذكر ثلاثة من خصائص بروتوكول UDP", "1. سريع جداً | 2. غير موجه للاتصال | 3. لا يضمن وصول البيانات"),
            ("9- اذكر البروتوكولات المستخدمة في البريد الالكتروني", "1. SMTP | 2. IMAP | 3. POP3"),
            ("4- اذكر أنواع المنافذ", "المعروفة (0-1023)، المسجلة (1024-49151)، الديناميكية (49152-65535)")
        ]
        for q, a in net_q2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المجموعة 3: الطبقات والكابلات"):
        net_q3 = [
            ("4- اذكر طبقات نموذج OSI", "الفيزيائية، ربط البيانات، الشبكة، النقل، الجلسة، التقديم، التطبيق"),
            ("1- اذكر أنواع الكابلات المستخدمة", "الملتوية (Twisted Pair)، المحورية (Coaxial)، الألياف الضوئية"),
            ("10- اذكر مزايا الألياف الضوئية", "سرعة هائلة جداً، مسافات طويلة، ولا تتأثر بالتداخل الكهرومغناطيسي")
        ]
        for q, a in net_q3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

# ==========================================
# قسم مادة ++C (حلول الـ 10 صور لـ ++C)
# ==========================================
else:
    st.header("💻 مراجعة شاملة: لغة برمجة ++C")

    with st.expander("📁 المجموعة 1: أساسيات اللغة والتعريفات"):
        cpp_q1 = [
            ("1- اذكر ميزات لغة ++C", "لغة عالية ومنخفضة المستوى، كائنية التوجه (OOP)، وسريعة الأداء"),
            ("2- ما هو الهيكل الأساسي لبرنامج ++C؟", "تبدأ بـ include <iostream> ثم main() والدالة return 0"),
            ("3- اذكر أنواع البيانات الأساسية", "int (صحيح)، float (عشري)، char (حرفي)، bool (منطقي)")
        ]
        for q, a in cpp_q1:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المجموعة 2: جمل التحكم (if, switch)"):
        cpp_q2 = [
            ("1- متى نستخدم جملة if؟", "عند التحقق من شرط منطقي معين (صح أو خطأ)"),
            ("2- ما الفرق بين switch و if؟", "switch أفضل عند وجود خيارات ثابتة ومحددة، و if أفضل للشروط المعقدة"),
            ("3- اذكر أهمية جملة default في switch", "تنفذ عندما لا تطابق المدخلات أي من الحالات (cases) الموجودة")
        ]
        for q, a in cpp_q2:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المجموعة 3: التكرار والمصفوفات"):
        cpp_q3 = [
            ("1- اذكر أنواع حلقات التكرار (Loops)", "for, while, do-while"),
            ("2- ما هي المصفوفة (Array)؟", "مجموعة من العناصر من نفس نوع البيانات تُخزن في مواقع ذاكرة متجاورة"),
            ("3- كيف يتم تعريف مصفوفة من 5 أرقام صحيحة؟", "int arr[5];")
        ]
        for q, a in cpp_q3:
            st.markdown(f'<div class="q-box">{q}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="a-box">{a}</div>', unsafe_allow_html=True)

    with st.expander("📁 المجموعة 4: الدوال (Functions)"):
        st.markdown('<div class="q-box">اكتب دالة بسيطة لجمع رقمين</div>', unsafe_allow_html=True)
        st.code("""
int sum(int a, int b) {
    return a + b;
}
        """, language="cpp")

# تذييل الصفحة الجانبي
st.sidebar.markdown("---")
st.sidebar.write("تطوير: **خيري عبد الواحد**")
st.sidebar.write("الحالة: **مكتمل 100%**")
