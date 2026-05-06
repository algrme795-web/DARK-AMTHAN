import streamlit as st

st.set_page_config(page_title="الموسوعة الشاملة لحلول أسئلة ++C", layout="wide")

st.markdown("""
    <style>
    .stExpander { background-color: #ffffff; border-radius: 10px; border-right: 10px solid #2980b9; margin-bottom: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .q-text { color: #d35400; font-weight: bold; font-size: 1.1em; margin-bottom: 8px; display: block; }
    .a-text { color: #2c3e50; background-color: #ecf0f1; padding: 12px; border-radius: 6px; margin-bottom: 20px; border-right: 3px solid #27ae60; }
    .code-snippet { background-color: #2d3436; color: #fab1a0; padding: 10px; border-radius: 5px; font-family: 'Courier New', monospace; }
    div.stMarkdown { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 الحل الكامل لجميع الأسئلة الاسترشادية (منهج ++C)")
st.info("هذا القسم يحتوي على حلول كافة الأسئلة الواردة في الصور العشر دون استثناء.")

# --- الأسئلة الاسترشادية صفحة 6 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 6 (مقدمة البرمجة)", expanded=True):
    st.markdown('<span class="q-text">1- اذكر ثلاثة أمثلة على لغات البرمجة من المستوى العالي.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. لغة ++C | 2. لغة Java | 3. لغة Python[cite: 1]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر ثلاثة من ميزات لغات ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. لغة كائنية التوجه (OOP). 2. السرعة العالية في الأداء. 3. القدرة على التحكم المباشر في الذاكرة[cite: 1]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر ثلاثة من استخدامات لغة ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. برمجة الألعاب. 2. تطوير أنظمة التشغيل. 3. بناء المتصفحات والأنظمة المدمجة[cite: 1]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر الغرض من استخدام جملة using namespace std في بداية الكود البرمجي.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تستخدم لتسهيل كتابة الأوامر القياسية (مثل cout و cin) مباشرة دون الحاجة لكتابة البادئة std:: قبل كل أمر[cite: 1]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- إلى ماذا تشير كلمة void في الدالة الرئيسة ()void main؟</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تشير إلى أن الدالة لا تعيد (No Return) أي قيمة لنظام التشغيل عند انتهائها[cite: 1]</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 16 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 16 (أنواع البيانات)"):
    st.markdown('<span class="q-text">1- اذكر ثلاثة أمثلة للأنواع الأساسية للبيانات في لغة ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. int (للأعداد الصحيحة). 2. double (للأعداد العشرية). 3. char (للحروف)[cite: 2]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر الغرض من استخدام نوع البيانات int.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يستخدم لتعريف المتغيرات التي تخزن قيماً عددية صحيحة (بدون فاصلة عشرية)[cite: 2]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر الغرض من استخدام نوع البيانات short.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يستخدم لتخزين أعداد صحيحة صغيرة المدى لتوفير مساحة في الذاكرة[cite: 2]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر الغرض من استخدام نوع البيانات bool.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يستخدم لتخزين القيم المنطقية فقط (true/false)[cite: 2]</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اذكر ثلاثة أنواع من عوامل التشغيل في ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. العوامل الحسابية (+, -). 2. عوامل المقارنة (==, !=). 3. العوامل المنطقية (&&, ||)[cite: 2]</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 36 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 36 (الكلاسات)"):
    st.markdown('<span class="q-text">1- اذكر الفرق الأساسي بين class و struct.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: في الـ class تكون الأعضاء خاصة (private) افتراضياً، أما في الـ struct فتكون عامة (public) افتراضياً.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر مفهوم الخصائص (Attributes) في ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: هي المتغيرات التي تصف حالة الكائن ويتم تعريفها داخل الكلاس.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر الغرض من استخدام Public في الـ Class.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يسمح بالوصول للأعضاء من خارج الكلاس.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر الغرض من استخدام Private في الـ Class.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يمنع الوصول للأعضاء إلا من داخل الكلاس نفسه لحماية البيانات.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اذكر الغرض من استخدام Protected في الـ Class.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: يسمح للكلاس والوراثة بالوصول للأعضاء ويمنع العالم الخارجي.</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 61 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 61 (الجمل الشرطية)"):
    st.markdown('<span class="q-text">1- اذكر الحالات التي تستخدم فيها جملة if statement.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تستخدم لاتخاذ قرار بناءً على شرط منطقي (نعم/لا).</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر ثلاثة من الأخطاء التي تحدث عند استخدام جملة if statement.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. وضع (;) بعد الشرط. 2. استخدام (=) بدلاً من (==). 3. نسيان الأقواس {}.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر أحد الفروق بين if و else if.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: if هي الشرط الأول، و else if تفحص شرطاً آخر فقط إذا فشل الأول.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اكتب الغرض من استخدام الجملة الشرطية switch.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تستخدم للاختيار بين خيارات متعددة ثابتة بشكل أكثر تنظيماً.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اكتب ثلاثة أمثلة على الحالات التي تستخدم فيها الجملة الشرطية switch.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. قائمة أيام الأسبوع. 2. درجات الطلاب. 3. قوائم الطعام.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">6- اذكر ثلاثة من الأخطاء التي يمكن ان تحدث عند استخدام switch.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. نسيان break. 2. تكرار قيمة الحالة (case). 3. عدم وضع حالة default.</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 73 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 73 (الحلقات التكرارية)"):
    st.markdown('<span class="q-text">1- اذكر الغرض استخدام جملة while.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تكرار كود معين طالما أن الشرط صحيح.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر ثلاثة من الحالات التي يتم فيها استخدام جملة while.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. قراءة بيانات حتى يتوقف المستخدم. 2. عداد غير معلوم النهاية. 3. التحقق من صحة المدخلات.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- ماذا يعني استخدام return 0 في الدالة الرئيسة؟</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تعني أن البرنامج انتهى بنجاح بدون أخطاء.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر أمثلة على الأقواس في ++C واستخدام كل منها.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. () للشرط. 2. {} للجسم البرمجي. 3. [] للمصفوفات.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اذكر ثلاثة من الأخطاء التي يمكن أن تحدث عند استخدام الجملة while.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. حلقة لا نهائية. 2. وضع (;) بعد الشرط. 3. عدم تحديث متغير العد.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">6- ماهو الفرق الأساسي بين while و do-while؟</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: do-while تنفذ الكود مرة واحدة على الأقل قبل فحص الشرط.</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 84 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 84 (التحكم في التكرار)"):
    st.markdown('<span class="q-text">1- اذكر ثلاثة من أنواع الحلقات المستخدمة في ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: for, while, do-while.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر الغرض من استخدام الجملة continue.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: تخطي الدورة الحالية والذهاب للتي تليها فوراً.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- ثلاثة من الحالات التي تستخدم فيها الجملة continue.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. تخطي الأرقام الزوجية. 2. استبعاد قيمة محددة من معالجة. 3. تسريع الحلقات الطويلة.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر الغرض من استخدام الجملة break.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: إيقاف الحلقة تماماً والخروج منها.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- ماذا تعني الجملة المتداخلة nested for؟</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: هي حلقة for تقع بداخل جسم حلقة for أخرى.</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 96 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 96 (المصفوفات)"):
    st.markdown('<span class="q-text">1- اذكر استخدام المصفوفات في ++C.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: لتخزين بيانات كثيرة من نفس النوع في متغير واحد.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- قم بتعريف مصفوفة ثنائية بها ثلاثة أعمدة وأربعة صفوف من الأعداد الصحيحة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">int arr[4][3];</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- قم بتعريف مصفوفة ثنائية بها أربعة أعمدة وخمسة صفوف لتخزين أسماء الطلبة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">string students[5][4];</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اكتب الغرض من استخدام الحلقة Foreach Loop.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: للمرور على عناصر المصفوفة بسهولة دون الحاجة لعداد.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اكتب امر الوصول للعنصر الثاني في المصفوفة {10, 20, 30, 40, 50} = int arr[].</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">arr[1]</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 107 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 107 (الدوال الجاهزة)"):
    st.markdown('<span class="q-text">1- اذكر ثلاثة أمثلة على الدوال الجاهزة في ++C والغرض من كل منها.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. abs(): للقيمة المطلقة. 2. pow(): للأس. 3. sqrt(): للجذر التربيعي.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر احد الطرق المستخدمة في حل مشكلة عدم التعرف على الدالة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: استدعاء المكتبة الخاصة بالدالة في بداية الكود (مثال: #include &lt;cmath&gt;).</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر ثلاثة من الدوال المكتبية مع ذكر مثال لكل منها.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. cmath (مثل sqrt). 2. iostream (مثل cout). 3. string (مثل length).</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اكتب دالة حساب حجم المصفوفة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">sizeof(arr) / sizeof(arr[0])</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اكتب دالة حساب طول السلسلة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">str.length()</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">6- اكتب دالة حساب جذر تربيحي.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">sqrt(x)</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">7- اكتب دالة الادخال.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">cin >> var;</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">8- اكتب دالة الاخراج.</span>', unsafe_allow_html=True)
    st.markdown('<div class="code-snippet">cout << var;</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 117 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 117 (بناء الدوال)"):
    st.markdown('<span class="q-text">1- اذكر ثلاثة أمثلة على دوال المستخدم في ++C والغرض من استخدام كل منها.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. دالة لجمع رقمين. 2. دالة لحساب المعدل. 3. دالة لطباعة رسالة ترحيبية. الغرض هو تنظيم الكود.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر ثلاثة من شروط اختيار اسم الدالة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. ألا تبدأ برقم. 2. ألا تكون كلمة محجوزة. 3. ألا تحتوي على مسافات.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر نوعي المعلمات المستخدمة في ++C والغرض من كل استخدام منهما.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. تمرير بالقيمة (Value). 2. تمرير بالمرجع (Reference).</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر ثلاثة من مكونات جسم الدالة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. نوع الإرجاع. 2. اسم الدالة. 3. الأقواس والمعاملات.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اكتب ثلاثة من المكونات الاختيارية في جسم الدالة.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. المعاملات. 2. جملة return (في حال void). 3. التعليقات التوضيحية.</div>', unsafe_allow_html=True)

# --- الأسئلة الاسترشادية صفحة 127 ---
with st.expander("📄 الأسئلة الاسترشادية - صفحة 127 (التحكم في الدوال)"):
    st.markdown('<span class="q-text">1- اذكر ثلاثة أمثلة على دوال التحكم في ++C والغرض من استخدام كل منها.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. return (لإرجاع قيمة). 2. exit() (لإغلاق البرنامج). 3. break (للخروج من حلقة).</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">2- اذكر ثلاثة من الأخطاء التي يمكن ان تحدث عند استخدام جملة return.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. إرجاع قيمة في دالة void. 2. نسيان return في دالة لها نوع. 3. إرجاع نوع بيانات خاطئ.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">3- اذكر ثلاثة من حالات استخدام الجملة void.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. دوال الطباعة. 2. دوال معالجة البيانات التي لا تحتاج لنتيجة. 3. الدالة الرئيسية إذا لم ترجع قيمة.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">4- اذكر ثلاثة من الأخطاء التي يمكن ان تحدث عند استخدام الجملة void.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. محاولة كتابة return قيمة. 2. محاولة تخزين نتيجتها في متغير. 3. استخدامها في العمليات الحسابية.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">5- اكتب الغرض من استخدام الجملة exit.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: إيقاف البرنامج تماماً وتحرير الذاكرة فوراً.</div>', unsafe_allow_html=True)

    st.markdown('<span class="q-text">6- اذكر ثلاثة من الأخطاء التي يمكن ان تحدث عند استخدام الجملة exit.</span>', unsafe_allow_html=True)
    st.markdown('<div class="a-text">ج: 1. وضعها قبل تنفيذ كود هام. 2. عدم إغلاق الملفات المفتوحة. 3. نسيان المكتبة &lt;cstdlib&gt;.</div>', unsafe_allow_html=True)

st.sidebar.success("تم حصر وحل كافة أسئلة الصور الـ 10")
