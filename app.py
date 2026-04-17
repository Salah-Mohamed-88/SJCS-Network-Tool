import streamlit as st
import time
import subprocess
import re

# إعدادات الصفحة
st.set_page_config(page_title="Network Optimizer Pro", page_icon="🚀")

st.title("Network Optimizer 🚀")

# إنشاء الأعمدة في الأعلى عشان تكون ثابتة
col1, col2 = st.columns(2)
# مكان مخصص للرسائل عشان ميتكرروش
message_container = st.empty()

# دالة (Function) عشان تجيب البنج الحقيقي من جهازك
def get_real_ping():
    try:
        # بنج على جوجل عشان نشوف سرعة النت الحقيقية
        # لو عايز بنج الراوتر غير 8.8.8.8 لـ 192.168.1.1
        command = ["ping", "-n", "1", "8.8.8.8"]
        result = subprocess.run(command, capture_output=True, text=True, timeout=2)
        
        # بنطلع الرقم من وسط الكلام اللي بيظهر في الـ CMD
        match = re.search(r"time=(\d+)ms", result.stdout)
        if match:
            return int(match.group(1))
        return 0
    except:
        return 0

# الزرار اللي بيعمل الـ Fix والـ Monitoring
if st.button("Run Auto Fix & Live Monitor 🤖", key="fix_button"):
    message_container.empty()
    
    with st.spinner("🔄 Checking Live Connection..."):
        # هنجرب نقيس 3 مرات ورا بعض عشان نحسب الـ Jitter (التذبذب)
        pings = []
        for i in range(3):
            pings.append(get_real_ping())
            time.sleep(0.5)
        
        latency = pings[-1] # آخر قراءة
        jitter = abs(pings[-1] - pings[0]) # الفرق بين القراءات هو الـ Jitter
        
        # تحديث الأرقام في الأعمدة (الأرقام دي حقيقية دلوقتي!)
        col1.metric("Latency", f"{latency} ms", delta=f"{latency-60}ms", delta_color="inverse")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms", delta_color="inverse")

        # منطق تحديد الحالة اللي قاله Chat GPT
        if latency < 60 and latency > 0:
            status = "Excellent"
        elif latency < 100:
            status = "Good"
        else:
            status = "Poor / Offline"

        # عرض النتائج النهائية في الـ container
        with message_container.container():
            st.info(f"📶 Network Quality: {status}")
            if latency > 0:
                st.success(f"✅ Connection Verified (Live Ping: {latency}ms)")
            else:
                st.error("❌ Could not reach DNS. Check your internet.")
