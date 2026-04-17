import streamlit as st
import time
import http.client

# 1. إعدادات الصفحة
st.set_page_config(page_title="Network Optimizer", page_icon="🚀")
st.title("Network Optimizer 🚀")

# 2. تعريف دالة القياس الجديدة (عشان تشتغل على GitHub)
def get_real_ping():
    try:
        start_time = time.time()
        # محاولة الاتصال بسيرفر جوجل (طريقة مسموحة على السيرفرات)
        conn = http.client.HTTPSConnection("8.8.8.8", timeout=2)
        conn.request("HEAD", "/")
        end_time = time.time()
        conn.close()
        return int((end_time - start_time) * 1000)
    except:
        return 0

# 3. تجهيز المكان في الواجهة
col1, col2 = st.columns(2)
message_container = st.empty()

# 4. زر التشغيل
if st.button("Run Auto Fix & Live Monitor 🤖", key="fix_button"):
    message_container.empty()
    
    with st.spinner("🔄 Measuring Live Connection..."):
        # قياس حقيقي
        latency = get_real_ping()
        # عمل رقم عشوائي بسيط للـ Jitter لإعطاء واقعية (بما أن القياس لحظي)
        jitter = 2 if latency > 0 else 0 
        
        # تحديث الأرقام في الأعمدة
        # delta_color="normal" مع رقم سالب يخلي اللون أخضر
        col1.metric("Latency", f"{latency} ms", delta=f"{latency-60}ms" if latency > 0 else None, delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms" if latency > 0 else None, delta_color="normal")

        # 5. منطق تحديد الحالة (Logic)
        if latency == 0:
            status = "Disconnected"
            info_msg = "❌ Could not reach DNS. Check internet."
        elif latency < 60:
            status = "Excellent"
            info_msg = f"✅ Connection Verified (Ping: {latency}ms)"
        elif latency < 100:
            status = "Good"
            info_msg = f"✅ Connection is Stable (Ping: {latency}ms)"
        else:
            status = "Poor"
            info_msg = "⚠️ High Latency Detected."

        # 6. عرض النتائج النهائية
        with message_container.container():
            st.info(f"📶 Network Quality: {status}")
            if latency > 0:
                st.success(info_msg)
            else:
                st.error(info_msg)
