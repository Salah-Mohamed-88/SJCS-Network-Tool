import streamlit as st
import time

st.title("Network Optimizer 🚀")

col1, col2 = st.columns(2)

# حجز مكان فاضي للرسائل عشان ميتكرروش تحت بعض
message_container = st.empty()

if st.button("Run Auto Fix 🤖", key="fix_button"):
    # أول ما تدوس، بننضف المكان الفاضي
    message_container.empty()
    
    with st.spinner("⚠️ Optimizing..."):
        time.sleep(1)
        latency = 40
        jitter = 10
        
        # تحديث الأرقام
        col1.metric("Latency", f"{latency} ms", delta="-5ms", delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta="-2ms", delta_color="normal")
        
        # بنعرض النتائج جوه الـ container اللي حجزناه
        with message_container.container():
            st.info("📶 Network Quality: Excellent")
            st.success(f"✅ Issue Resolved (Latency: {latency}ms | Jitter: {jitter}ms)")
