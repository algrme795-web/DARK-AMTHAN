import streamlit as st
import time

# --- الإعدادات الفنية الفاخرة ---
st.set_page_config(
    page_title="Khairy Abdul Wahid - Ultimate Edition",
    page_icon="💎",
    layout="wide"
)

# --- نظام التجميل البصري المتطور (Ultra-Modern CSS) ---
st.markdown("""
    <style>
    /* خلفية متحركة احترافية */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #330000 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    
    /* تصميم البطاقات الزجاجية */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 0, 0, 0.2);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        transition: all 0.4s ease;
        direction: rtl;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }
    .glass-card:hover {
        border: 1px solid #ff0000;
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.4);
    }
    
    /* العناوين المتوهجة */
    .glow-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 4rem !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #ff0000, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255, 0, 0, 0.5);
        margin-bottom: 0px;
    }

    /* تنسيق الأسئلة والأجوبة */
    .q-text { color: #ff4d4d; font-size: 1.3rem; font-weight: 700; margin-bottom: 15px; border-bottom: 1px solid #333; padding-bottom: 10px; }
    .a-text { color: #dcdcdc; font-size: 1.1rem; line-height: 1.8; }
    
    /* تعديل شريط التمرير والقوائم */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #000; }
    ::-webkit-scrollbar-thumb { background: #ff0000; border-radius: 10px; }
    
    .stSidebar { background-color: rgba(0,0,0,0.9) !important; border-right: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# --- شريط التحميل (Intro Animation) ---
if 'init_done' not in st.session_state:
    with st.empty():
        for i in range(101):
            st.markdown(f"<h1 style='text-align:center; color:#ff0000; margin-top:20%;'>LOADING SYSTEM {i}%</h1>", unsafe_allow_html=True)
            st.progress(i)
            time.sleep(0.01)
        st.session_state['init_done'] = True
    st.rerun()

# --- الهيدر والترحيب ---
st.markdown("<h1 class='glow-title'>DARK EMPIRE V3</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; letter-spacing: 3px;'>THE DEFINITIVE EDITION | KHAIRY ABDUL WAHID</p>", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.markdown("<h2 style='color:#ff0000; text-align:center;'>CONTROL CENTER</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
menu = st.sidebar.radio("📁 المنهج الدراسي الكامل:", ["🌐 موسوعة الشبكات", "💻 مرجع برمجة ++C"])
st.sidebar.markdown("---")
st.sidebar.info("💡 تم دمج جميع الأسئلة الاسترشادية من 20 صورة بدقة متناهية.")

# --- قسم الشبكات (الصور 1-10 كاملة) ---
if menu == "🌐 موسوعة الشبكات":
    st.markdown("## 🌐 بنك أسئلة أساسيات الشبكات الشامل")
    
    # شبكات - الجزء 1
    with st.container():
        st.markdown("### 🧱 الأساسيات، النماذج، والطبقات")
        cols = st.columns(2)
        with cols[0]:
            q_list1 = [
                ("أنواع الشبكات؟", "PAN, LAN, MAN, WAN."),
                ("استخدامات الشبكة؟", "مشاركة البيانات، التواصل، التعليم، التجارة."),
                ("تحديات الشبكات؟", "الأمن، استهلاك الطاقة، التوسع، الخصوصية."),
                ("خصائص LAN؟", "مساحة ضيقة، سرعة هائلة، ملكية خاصة."),
                ("خصائص WAN؟", "مساحة عالمية، سرعة معتدلة، شبكات عامة."),
                ("مزايا السحابة؟", "توفير مادي، مرونة، وصول عالمي."),
            ]
            for q, a in q_list1:
                st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)
        
        with cols[1]:
            q_list2 = [
                ("طبقات OSI؟", "7 طبقات: فيزيائية، ربط بيانات، شبكة، نقل، جلسة، تقديم، تطبيق."),
                ("طبقات TCP/IP؟", "4 طبقات: وصول، إنترنت، نقل، تطبيق."),
                ("وظائف IP؟", "العنونة المنطقية، التوجيه، التجزئة."),
                ("وظائف TCP؟", "التحكم بالتدفق، كشف الخطأ، ترتيب الحزم."),
                ("مزايا النماذج؟", "التوافقية وسهولة التطوير البرمجي."),
            ]
            for q, a in q_list2:
                st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    # شبكات - الجزء 2
    with st.expander("📡 البروتوكولات، الكابلات، والمنافذ (التفاصيل العميقة)"):
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("**البروتوكولات والمنافذ:** HTTP (80), HTTPS (443), DNS (53), SMTP (25), POP3 (110).")
        st.write("**أنواع الكابلات:** Twisted Pair (رخيص)، Coaxial (قوي)، Fiber Optic (سرعة الضوء).")
        st.write("**بروتوكولات النقل:** UDP (سريع للبث)، TCP (آمن للبيانات).")
        st.write("**المصافحة (Handshake):** عملية تأمين وبدء الاتصال بين طرفين.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- قسم ++C (الصور 1-10 كاملة) ---
else:
    st.markdown("## 💻 مرجع برمجة ++C الكامل")
    
    t1, t2 = st.tabs(["🏗️ الهيكل والتحكم", "📦 المصفوفات والدوال"])
    
    with t1:
        cpp_q1 = [
            ("مميزات لغة ++C؟", "كائنية التوجه، سريعة، تحكم مباشر بالهاردوير."),
            ("أنواع البيانات؟", "int, float, double, char, bool."),
            ("الفرق بين if و switch؟", "if للمدى والشروط المعقدة، switch للقيم الثابتة والمحددة."),
            ("الفرق بين cin و cout؟", "cin للإدخال (Input)، cout للإخراج (Output)."),
            ("ما هي break و default؟", "break تخرج من الحالة، default تنفذ عند فشل جميع الشروط."),
            ("الفرق بين \\n و endl؟", "كلاهما سطر جديد، لكن endl ينظف الذاكرة المؤقتة.")
        ]
        for q, a in cpp_q1:
            st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)

    with t2:
        cpp_q2 = [
            ("أنواع التكرار؟", "for (محدد)، while (غير محدد)، do-while (تنفذ مرة على الأقل)."),
            ("تعريف المصفوفة؟", "مجموعة عناصر من نفس النوع في ذاكرة متسلسلة تبدأ من الصفر."),
            ("أهمية الدوال؟", "إعادة استخدام الكود، سهولة الصيانة، تقسيم المهام."),
            ("المتغير المحلي والعالمي؟", "Local داخل الدالة فقط، Global متاح لكل البرنامج."),
            ("وظيفة return؟", "إعادة نتيجة المعالجة من الدالة إلى البرنامج الرئيسي.")
        ]
        for q, a in cpp_q2:
            st.markdown(f"<div class='glass-card'><div class='q-text'>{q}</div><div class='a-text'>{a}</div></div>", unsafe_allow_html=True)
        st.code("""// مثال برمجي شامل\n#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n    if(x > 5) cout << "Khairy Success!";\n    return 0;\n}""", language="cpp")

# --- التذييل (Footer) ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:#ff0000; font-weight:bold;'>Developed by Khairy Abdul Wahid © 2026</p>", unsafe_allow_html=True)
