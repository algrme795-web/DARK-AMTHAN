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
import streamlit as st

# إعدادات الصفحة والتصميم
st.set_page_config(page_title="الأسئلة الاسترشادية - خيري عبد الواحد", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stExpander { background-color: #ffffff; border: 1px solid #d1d8e0; border-radius: 8px; }
    .q-text { color: #2c3e50; font-weight: bold; font-size: 1.15em; margin-bottom: 10px; display: block; border-right: 5px solid #e67e22; padding-right: 10px; }
    .a-text { color: #155724; background-color: #d4edda; padding: 12px; border-radius: 6px; margin-bottom: 25px; border: 1px solid #c3e6cb; }
    .highlight { color: #d35400; font-weight: bold; }
    div.stMarkdown { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("📝 الأسئلة الاسترشادية المحلولة")
st.info("هذا القسم يحتوي على حلول كافة الأسئلة الاسترشادية لطلاب معهد رسل الحضارة الدولي.")

# القائمة الجانبية
with st.sidebar:
    st.header("اختر المادة")
    subject = st.radio("المواد المتاحة:", ["شبكات الحاسوب (CCNA-1)", "لغة البرمجة (++C)"])
    st.write("---")
    st.write("إعداد وتطوير: **خيري عبد الواحد**")

if subject == "شبكات الحاسوب (CCNA-1)":
    st.header("🌐 الأسئلة الاسترشادية لمادة الشبكات")

    with st.expander("📌 الجزء الأول: المفاهيم والأنواع", expanded=True):
        st.markdown('<span class="q-text">س: ما هي فوائد شبكات الحاسب؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: 1. مشاركة الموارد (طابعات، ملفات). 2. تقليل التكلفة. 3. سرعة نقل المعلومات. 4. المركزية في الإدارة.</div>', unsafe_allow_html=True)

        st.markdown('<span class="q-text">س: ما هو الفرق الجوهري بين Client-Server و Peer-to-Peer؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: في Client-Server يوجد جهاز مركزي (خادم) يدير الموارد، أما في Peer-to-Peer فكل الأجهزة متساوية في الصلاحيات.</div>', unsafe_allow_html=True)

    with st.expander("📌 الجزء الثاني: الأجهزة والربط (Topologies)"):
        st.markdown('<span class="q-text">س: اذكر عيوب الـ Bus Topology.</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: إذا انقطع الكيبل الرئيسي تتوقف الشبكة بالكامل، وصعوبة اكتشاف الأعطال[cite: 1].</div>', unsafe_allow_html=True)

        st.markdown('<span class="q-text">س: ما هو الجهاز المستخدم لربط شبكات مختلفة (مثل LAN بـ Internet)؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: الموجه (Router)[cite: 1].</div>', unsafe_allow_html=True)

    with st.expander("📌 الجزء الثالث: نموذج OSI والعنونة"):
        st.markdown('<span class="q-text">س: في أي طبقة يتم تحويل البيانات إلى إشارات كهربائية أو ضوئية؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: الطبقة الأولى (Physical Layer)[cite: 1].</div>', unsafe_allow_html=True)

        st.markdown('<span class="q-text">س: ما هو الـ MAC Address؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: هو العنوان الفيزيائي المحروق على كرت الشبكة ولا يتغير، ويتكون من 48 بت[cite: 1].</div>', unsafe_allow_html=True)

else:
    st.header("💻 الأسئلة الاسترشادية لمادة ++C")

    with st.expander("📍 الجزء الأول: المدخلات والمخرجات", expanded=True):
        st.markdown('<span class="q-text">س: ما هو الفرق بين endl و "\n"؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: كلاهما يستخدم للنزول لسطر جديد، لكن endl تقوم أيضاً بتفريغ الذاكرة المؤقتة (Buffer).</div>', unsafe_allow_html=True)

    with st.expander("📍 الجزء الثاني: الشروط والتكرار"):
        st.markdown('<span class="q-text">س: اكتب كود بلغة ++C يطلب من المستخدم إدخال عمره ويطبع "Adult" إذا كان أكبر من 18.</span>', unsafe_allow_html=True)
        st.code("""
int age;
cout << "Enter your age: ";
cin >> age;
if (age > 18) {
    cout << "Adult";
}
        """, language="cpp")

        st.markdown('<span class="q-text">س: ما هي وظيفة أمر switch؟</span>', unsafe_allow_html=True)
        st.markdown('<div class="a-text">ج: تستخدم للاختيار بين عدة حالات ثابتة (Cases) بدلاً من استخدام if المتعددة لتسهيل الكود.</div>', unsafe_allow_html=True)

st.sidebar.warning("تأكد من مراجعة هذه الأسئلة جيداً قبل الامتحان.")
