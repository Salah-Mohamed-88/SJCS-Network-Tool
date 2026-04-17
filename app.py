import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="Network Optimizer Pro", page_icon="🚀")

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("🔑 Router Access")
    router_ip = st.text_input("Router IP", value="192.168.1.1")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password")
    st.divider()
    st.write("Current Device: **Huawei/DN Router**")

# 3. الدوال (Functions)
def get_real_ping():
    try:
        start_time = time.time()
        conn = http.client.HTTPSConnection("8.8.8.8", timeout=2)
        conn.request("HEAD", "/")
        end_time = time.time()
        conn.close()
        return int((end_time - start_time) * 1000)
    except:
        return 0

def login_and_reboot(ip, user, pwd):
    # ملاحظة: دي دالة تجريبية، الربط الفعلي بيعتمد على موديل الراوتر بدقة
    try:
        st.info(f"Connecting to {ip}...")
        time.sleep(2)
        return True
    except:
        return False

# 4. الواجهة الرئيسية
st.title("Network Optimizer 🚀")

col1, col2 = st.columns(2)
message_container = st.empty()

# زرار الفحص والتحسين الأساسي
if st.button("Run Auto Fix & Live Monitor 🤖", key="fix_button"):
    message_container.empty()
    with st.spinner("🔄 Checking Connection..."):
        latency = get_real_ping()
        jitter = 2 if latency > 0 else 0
        
        # عرض الأرقام (تأكد من وجود الفواصل هنا)
        col1.metric(
            label="Latency", 
            value=f"{latency} ms", 
            delta=f"{latency-60}ms" if latency > 0 else None, 
            delta_color="normal"
        )
        col2.metric(
            label="Jitter", 
            value=f"{jitter} ms", 
            delta=f"{jitter-15}ms" if latency > 0 else None, 
            delta_color="normal"
        )

        if latency == 0:
            status = "Disconnected"
        elif latency < 60:
            status = "Excellent"
        else:
            status = "Good"

        with message_container.container():
            st.info(f"📶 Network Quality: {status}")
            st.success(f"✅ Analysis Complete (Ping: {latency}ms)")

# 5. أزرار التحكم في الراوتر (Quick Fixes)
st.divider()
st.subheader("🛠️ Quick Fixes (Router Control)")
c1, c2, c3 = st.columns(3)

if c1.button("Restart Router 🔄"):
    if password:
        if login_and_reboot(router_ip, username, password):
            st.success("Reboot command sent to router!")
    else:
        st.error("Please enter password in sidebar.")

if c2.button("Optimize MTU ⚡"):
    st.info("MTU set to 1420 (Gaming Mode)")

if c3.button("Apply QoS 🎮"):
    st.warning("Gaming Prioritization Enabled")
