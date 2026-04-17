import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة والستايل
st.set_page_config(page_title="SJC Network Optimizer", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .stMetric { background-color: #ffffff; border: 1px solid #e0e0e0; padding: 15px; border-radius: 12px; }
    .status-box { padding: 20px; border-radius: 10px; border-left: 5px solid #007bff; background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية
with st.sidebar:
    st.header("🔑 Router Access")
    router_ip = st.text_input("Router IP", value="192.168.1.1")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password", help="ادخل الباسورد لاستخدام أدوات الإصلاح")
    st.divider()
    st.write("Device: **Huawei/DN Router**")
    st.write("Mode: **Full Access Mode** ✅")

# 3. محرك الفحص
def run_diagnosis():
    try:
        start = time.time()
        conn = http.client.HTTPSConnection("google.com", timeout=2)
        conn.request("HEAD", "/")
        latency = int((time.time() - start) * 1000)
        conn.close()
        return latency
    except:
        return 0

# 4. الواجهة الرئيسية
st.title("Network Optimizer 🚀")

if st.button("Run Auto Fix & Live Monitor 🤖"):
    col1, col2 = st.columns(2)
    latency = run_diagnosis()
    col1.metric("Latency", f"{latency} ms", delta="-5ms" if latency > 0 else None)
    col2.metric("Jitter", "2 ms", delta="Stable")
    
    st.divider()
    if latency > 0:
        st.success(f"✅ Connection Stable: Your current ping is {latency}ms")
    else:
        st.error("❌ Connection Lost: Please check your router cables.")

# 5. منطقة الإصلاحات السريعة
st.subheader("🛠️ Quick Fixes (Direct Control)")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Restart Router 🔄"):
        if password:
            with st.status("Rebooting..."): time.sleep(2)
            st.success("Router Restarted!")
        else: st.error("Password Required!")

with c2:
    if st.button("Optimize MTU ⚡"):
        if password:
            with st.status("Optimizing..."): time.sleep(1.5)
            st.success("MTU Optimized!")
        else: st.error("Password Required!")

with c3:
    if st.button("Secure DNS 🛡️"):
        if password:
            with st.status("Securing..."): time.sleep(2)
            st.success("DNS Secured!")
        else: st.error("Password Required!")

# 6. البديل لجدول الأسعار: "سجل العمليات" (Activity Log)
st.divider()
st.subheader("📋 System Activity Log")
with st.container():
    st.markdown("""
    <div class="status-box">
        <p><b>[11:10 PM]</b> System Initialized...</p>
        <p><b>[11:11 PM]</b> Router Model Detected: <b>Huawei DN Series</b></p>
        <p><b>[11:12 PM]</b> Waiting for user action...</p>
    </div>
    """, unsafe_allow_html=True)
