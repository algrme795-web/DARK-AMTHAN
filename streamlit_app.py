import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="منصة مراجعة معهد رسل الحضارة", layout="wide")

# تنسيق المظهر (CSS) ليكون مريحاً للطالب
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stExpander { background-color: white; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .question { color: #2c3e50; font-weight: bold; font-size: 1.1em; border-right: 4px solid #3498db; padding-right: 10px; margin-bottom: 10px; }
    .answer { color: #27ae60; background-color: #f0fff4; padding: 10px; border-radius: 5px; margin-bottom: 20px; font-weight: 500; }
    div.stMarkdown { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 بنك الأسئلة المحلولة - معهد رسل الحضارة")
st.write("إعداد الطالب: خيري عبد الواحد")

# القائمة الجانبية للتنقل
with st.sidebar:
    st.header("إدارة المواد")
    choice = st.radio("اختر القسم:", ["شبكات الحاسوب (Network)", "لغة البرمجة (++C)"])
    st.success("جميع الأسئلة مستخرجة من المنهج الرسمي.")

if choice == "شبكات الحاسوب (Network)":
    st.header("🌐 مراجعة شاملة لمادة الشبكات (CCNA-1)")

    # القسم الأول: المحاضرات 1، 2، 3
    with st.expander("📖 المحاضرة 1 إلى 3: التعريفات والأنواع", expanded=True):
        st.markdown('<div class="question">س1: ما هي شبكة الحاسب؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: مجموعة من الأجهزة المرتبطة ببعضها لمشاركة الموارد (بيانات، طابعات، برمجيات).</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="question">س2: ما الفرق بين الـ LAN والـ WAN والـ MAN؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: LAN (محلية لمبنى)، MAN (متوسطة لمدينة)، WAN (واسعة لدول وقارات).</div>', unsafe_allow_html=True)

        st.markdown('<div class="question">س3: اذكر مكونات الشبكة (Components).</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: الأجهزة (Devices)، الوسائط (Media)، الخدمات (Services).</div>', unsafe_allow_html=True)

    # القسم الثاني: المحاضرة 4
    with st.expander("📐 المحاضرة 4: أشكال ربط الشبكات (Topology)"):
        st.markdown('<div class="question">س4: ما هو الـ Star Topology؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: ربط كل الأجهزة بنقطة مركزية (Hub/Switch)[cite: 1].</div>', unsafe_allow_html=True)

        st.markdown('<div class="question">س5: ما هي ميزة الـ Mesh Topology؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: الموثوقية العالية (Redundancy)؛ حيث يتصل كل جهاز بكل الأجهزة الأخرى مباشرة[cite: 1].</div>', unsafe_allow_html=True)

    # القسم الثالث: المحاضرة 5 و 6
    with st.expander("⚙️ المحاضرة 5 & 6: نموذج OSI والبروتوكولات"):
        st.markdown('<div class="question">س6: اذكر طبقات الـ OSI السبعة بالترتيب من الأسفل.</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: 1-Physical, 2-Data Link, 3-Network, 4-Transport, 5-Session, 6-Presentation, 7-Application[cite: 1].</div>', unsafe_allow_html=True)

        st.markdown('<div class="question">س7: ما هي وظيفة طبقة الـ Network؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: العنونة المنطقية (IP Addressing) واختيار أفضل مسار (Routing)[cite: 1].</div>', unsafe_allow_html=True)

    # القسم الرابع: المحاضرة 7
    with st.expander("🔌 المحاضرة 7: وسائط النقل والكيبلات"):
        st.markdown('<div class="question">س8: ما الفرق بين كيبل Straight-through و Cross-over؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: Straight لربط أجهزة مختلفة (PC إلى Switch)، و Cross لربط أجهزة متشابهة (PC إلى PC)[cite: 1].</div>', unsafe_allow_html=True)

else:
    st.header("💻 مراجعة شاملة لأسئلة لغة ++C")

    with st.expander("基础 الأساسيات والمدخلات", expanded=True):
        st.markdown('<div class="question">س1: كيف يتم تعريف متغير لتخزين نص (كلمة)؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: باستخدام نوع البيانات string (مثال: string name;).</div>', unsafe_allow_html=True)

        st.markdown('<div class="question">س2: ما هو الفرق بين "=" و "==" في البرمجة؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: "=" تستخدم لإعطاء قيمة للمتغير، بينما "==" تستخدم للمقارنة بين قيمتين.</div>', unsafe_allow_html=True)

    with st.expander("🔄 الحلقات التكرارية (Loops) والشروط"):
        st.markdown('<div class="question">س3: متى نستخدم الحلقة (for loop)؟</div>', unsafe_allow_html=True)
        st.markdown('<div class="answer">ج: عندما نعرف عدد التكرارات مسبقاً.</div>', unsafe_allow_html=True)

        st.code("""
// مثال لكود يطبع الأرقام من 1 إلى 5
for(int i=1; i<=5; i++) {
    cout << i << endl;
}
        """, language="cpp")

st.sidebar.markdown("---")
st.sidebar.info("هذا الموقع يخدم طلاب معهد رسل الحضارة الدولي.")
