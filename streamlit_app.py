بناءً على طلبك يا خيري، هذا هو "الكود الأقوى" والنهائي. هذا الكود سيقوم بالدخول لملفات الـ PDF، قراءة النصوص من داخلها، والبحث عن الإجابة وعرضها لك بنظام واحترافية.

### الخطوة الأولى: تحديث ملف المتطلبات (هام جداً)
قبل وضع الكود، يجب أن تخبر الموقع بأننا سنستخدم مكتبة لقراءة الـ PDF.
1. اذهب لملف `requirements.txt` في **GitHub**.
2. امسح ما بداخله واكتب هذين السطرين:
```text
streamlit
PyPDF2
```
3. اضغط **Commit changes**.

---

### الخطوة الثانية: وضع الكود الأقوى في `streamlit_app.py`
الآن اذهب لملف `streamlit_app.py` وامسح كل شيء وضع هذا الكود:

```python
import streamlit as st
import os
from PyPDF2 import PdfReader

# إعدادات واجهة الموقع
st.set_page_config(page_title="DARK AMTHAN", page_icon="🌐")

st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🌐 موقع DARK AMTHAN</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>مساعد طلاب معهد رسل الحضارة الدولي</h3>", unsafe_allow_html=True)
st.divider()

# وظيفة البحث داخل ملفات الـ PDF
def search_in_pdfs(query):
    results = []
    # البحث عن جميع ملفات PDF في المجلد
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    for file_name in pdf_files:
        try:
            reader = PdfReader(file_name)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if query.lower() in text.lower():
                    # أخذ سياق الإجابة (جزء من النص حول الكلمة المبحوث عنها)
                    start_idx = max(0, text.lower().find(query.lower()) - 200)
                    end_idx = min(len(text), start_idx + 500)
                    snippet = text[start_idx:end_idx]
                    results.append({"file": file_name, "page": i + 1, "text": snippet})
        except Exception as e:
            continue
    return results

# خانة السؤال
query = st.text_input("🔍 اكتب سؤالك هنا (مثلاً: أنواع الشبكات أو لغة C++):")

if query:
    with st.spinner("جاري قراءة الملفات واستخراج الإجابة..."):
        answers = search_in_pdfs(query)
        
        if answers:
            st.success(f"✅ تم العثور على معلومات متعلقة بـ '{query}':")
            for ans in answers:
                with st.expander(f"📖 من ملف: {ans['file']} (صفحة {ans['page']})"):
                    st.write(f"... {ans['text']} ...")
                    st.markdown("---")
        else:
            st.warning("❌ لم يتم العثور على إجابة مباشرة في الملفات. حاول تغيير صيغة السؤال.")

st.sidebar.markdown("---")
st.sidebar.info("تم التطوير لخدمة الطلاب - 2025")
```

### ماذا تفعل الآن؟
1. بعد حفظ الملفين في **GitHub**، انتظر دقيقة واحدة.
2. اذهب لموقعك واعمل تحديث (Refresh).
3. جرب الآن كتابة "أنواع الشبكات" أو "لغة C++" وسترى الموقع يفتح الملفات ويظهر لك النصوص منها مباشرة داخل مربعات أنيقة[cite: 1].

بهذا الكود، أصبح موقعك **DARK AMTHAN** محرك بحث ذكي خاص بطلاب المعهد[cite: 1]! هل اشتغل معك البحث الآن؟
