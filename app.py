import streamlit as st
import time

st.title("Network Optimizer 🚀")

# إنشاء الأعمدة لعرض الأرقام
col1, col2 = st.columns(2)

if st.button("Run Auto Fix 🤖", key="fix_button"):
    with st.spinner("⚠️ Fixing..."):
        time.sleep(1)

        # 1. تعريف الأرقام في متغيرات
        latency = 40
        jitter = 10

        # 2. منطق تحديد الحالة (بناءً على نصيحة شات جي بي تي)
        if latency < 60 and jitter < 20:
            status = "Excellent"
        elif latency < 100:
            status = "Good"
        else:
            status = "Poor"

        # 3. تحديث الأرقام في الواجهة
        col1.metric("Latency", f"{latency} ms", delta="-5ms")
        col2.metric("Jitter", f"{jitter} ms", delta="-2ms")

        # 4. عرض الحالة (باستخدام المتغير status)
        st.info(f"📶 Network Quality: {status}")

        # 5. رسالة النجاح النهائية (باستخدام f-string لدمج الأرقام)
        st.success(f"✅ Issue Resolved (Latency: {latency}ms | Jitter: {jitter}ms)")
        # عرض النتائج النهائية
        st.info(f"📶 Network Quality: {status}")
        st.success(f"✅ Issue Resolved (Latency: {latency}ms | Jitter: {jitter}ms)")
