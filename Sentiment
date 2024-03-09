import streamlit as st
from transformers import pipeline
from mtranslate import translate

# عنوان صفحه در Streamlit
st.title('Sentiment Analysis - Created by Razie :)')

# ایجاد یک فیلد ورودی برای دریافت متن‌ها از کاربر
user_comments = st.text_area("لطفاً کامنت‌های خود را بنویسید، هر کامنت را در یک خط بنویسید.")

# تبدیل متن‌های وارد شده به یک لیست از کامنت‌ها
texts = [comment.strip() for comment in user_comments.split('\n') if comment.strip()]

# ترجمه متن‌ها به انگلیسی
translated_texts = [translate(text, 'en') for text in texts]

# ایجاد یک دکمه برای شروع تحلیل همزمان چندین متن
if st.button("تحلیل همزمان چندین متن"):
    # بررسی اینکه کاربر حداقل یک کامنت وارد کرده باشد
    if texts:
        # ایجاد یک pipeline برای تحلیل احساسات
        classifier = pipeline("sentiment-analysis")

        # اجرای تحلیل احساسات روی هر کامنت
        results = []
        for i, (text, translated_text) in enumerate(zip(texts, translated_texts), start=1):
            # تحلیل احساسات بر روی متن ترجمه شده
            preds = classifier(translated_text)
            preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
            results.append({"text": text, "predictions": preds})

        # نمایش نتایج به صورت جدول
        for i, result in enumerate(results, start=1):
            st.write(f"**کامنت {i}**: {result['text']}")
            st.table(result['predictions'])
    else:
        st.warning("لطفاً حداقل یک کامنت وارد کنید.")
##### همی
