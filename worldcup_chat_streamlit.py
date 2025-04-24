
import streamlit as st
import json

# تحميل قاعدة البيانات
with open("worldcup_chat_data_full.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

# عنوان التطبيق
st.title("مساعد كأس العالم 2034")

# اختيار الفئة
user_category = st.selectbox("اختر فئتك:", ["زائر عام", "عائلة", "طفل", "شاب", "ذوي احتياجات خاصة"])

# إدخال السؤال
user_question = st.text_input("ما هو سؤالك اليوم؟")

# البحث في قاعدة البيانات
def find_answer(question):
    for item in qa_data:
        if item["question"].strip() in question.strip():
            return item["answer"].get("general") or item["answer"].get("special_needs") or list(item["answer"].values())[0]
    return "عذرًا، لم أتمكن من العثور على إجابة لهذا السؤال حالياً."

# عرض الإجابة
if st.button("أرسل"):
    if user_question:
        response = find_answer(user_question)
        st.success(response)
    else:
        st.warning("يرجى كتابة سؤال للمتابعة.")
