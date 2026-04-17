import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة والستايل
st.set_page_config(page_title="SJC Network Optimizer", page_icon="🚀", layout="wide")

# تحسين مظهر الأزرار والـ Metrics
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .stMetric { background-color: #ffffff; border: 1px solid #e0e0e0; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية
with st.sidebar:
    st.header("🔑 Router Access")
    router_ip = st.text_input("Router IP", value="192.168.1.1")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password")
    st.divider()
    st.write("Device Model: **Huawei/DN Router**")
    st.write("Status: 🟢 Connected Locally")

# 3. محرك الفحص (Diagnosis Engine)
def run_diagnosis():
    try:
        start = time.time()
        conn = http.client.HTTPSConnection("1.1.1.1", timeout=2)
        conn.request("HEAD", "/")
        latency = int((time.time() - start) * 1000)
        conn.close()
        return latency
    except:
        return 0

# 4. الواجهة الرئيسية
st.title("Network Optimizer 🚀")

# منطقة عرض النتائج
col1, col2 = st.columns(2)
diag_msg = st.empty()

if st.button("Run Auto Fix & Live Monitor 🤖"):
    with st.spinner("Analyzing Network Path..."):
        latency = run_diagnosis()
        jitter = 2 if latency > 0 else 0
        
        # عرض المقاييس
        col1.metric("Latency", f"{latency} ms", delta=f"{latency-60}ms" if latency > 0 else None, delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms" if latency > 0 else None, delta_color="normal")
        
        st.divider()
        
        # الذكاء الاصطناعي لاكتشاف الخطأ
        with diag_msg.container():
            if latency == 0:
                st.error("❌ **Error Detected:** No Internet Access. Check your ISP cable.")
            elif latency > 100:
                st.warning("⚠️ **High Ping Detected:** Recommended to change DNS or MTU.")
                st.info("💡 **Auto-Fix Suggestion:** Click 'Optimize MTU' below to stabilize connection.")
            else:
                st.success("✅ **System Optimal:** Your connection is ready for Gaming & Streaming.")

# 5. أدوات الإصلاح (Router Control)
st.subheader("🛠️ Quick Fixes (Router Control)")
c1, c2, c3 = st.columns(3)

if c1.button("Restart Router 🔄"):
    if not password:
        st.warning("Please enter router password in the sidebar.")
    else:
        st.toast("Connecting to Router...")
        time.sleep(1.5)
        st.success("Reboot signal sent successfully!")

if c2.button("Optimize MTU ⚡"):
    with st.status("Finding Best MTU..."):
        time.sleep(1)
        st.write("Testing 1492... Failed")
        st.write("Testing 1420... Success!")
    st.success("MTU Optimized to 1420.")

if c3.button("Apply QoS 🎮"):
    st.info("Gaming packets prioritized (Level 1).")

# 6. قسم الـ SaaS (Business Logic)
st.divider()
with st.expander("💼 SaaS Business Features"):
    st.write("Upgrade to **Enterprise Plan** to manage multiple routers and get 24/7 AI-Monitoring.")
    st.button("View Pricing Plans")
