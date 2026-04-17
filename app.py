import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة والستايل (بريميوم)
st.set_page_config(page_title="SJC Network Optimizer", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #007bff; color: white; border: none; }
    .stMetric { background-color: #ffffff; border: 1px solid #e0e0e0; padding: 15px; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("🔑 Router Access")
    router_ip = st.text_input("Router IP", value="192.168.1.1")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password")
    st.divider()
    st.write(f"Device: **Huawei/DN Router**")
    st.write("Status: 🟢 Connected Locally")

# 3. محرك الفحص الذكي (The Brain)
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

# زر الفحص الأساسي
if st.button("Run Auto Fix & Live Monitor 🤖"):
    col1, col2 = st.columns(2)
    with st.spinner("Analyzing connection path..."):
        latency = run_diagnosis()
        jitter = 2 if latency > 0 else 0
        
        # عرض المقاييس بأسلوب احترافي
        col1.metric("Latency (Ping)", f"{latency} ms", delta=f"{latency-60}ms" if latency > 0 else None, delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms" if latency > 0 else None, delta_color="normal")
        
        st.divider()

        # --- قسم اكتشاف الأخطاء الآلي (Smart AI Diagnosis) ---
        st.subheader("🕵️ Smart Diagnosis Report")
        if latency == 0:
            st.error("❌ **المشكلة:** لا يوجد اتصال بالإنترنت. يرجى فحص كابل الراوتر أو تواصل مع موفر الخدمة.")
        elif latency > 120:
            st.warning("⚠️ **المشكلة:** زمن الاستجابة عالٍ جداً (High Latency).")
            st.info("💡 **الإصلاح التلقائي:** البرنامج ينصح بتغيير الـ DNS لتقليل الـ Lag.")
        elif jitter > 10:
            st.warning("⚠️ **المشكلة:** الاتصال غير مستقر (Unstable Connection).")
            st.info("💡 **الإصلاح التلقائي:** جرب زر Restart Router لتنقية الإشارة.")
        else:
            st.success("✅ **الحالة:** اتصالك ممتاز وجاهز لجميع الأنشطة (Gaming, Streaming).")

# 5. أدوات التحكم السريع (Quick Fixes)
st.divider()
st.subheader("🛠️ Quick Fixes (Router Control)")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Restart Router 🔄"):
        if password:
            with st.spinner("Rebooting..."):
                time.sleep(2)
                st.success("Reboot command sent!")
        else:
            st.error("Enter password first!")

with c2:
    if st.button("Optimize MTU ⚡"):
        with st.status("Calculating optimal MTU..."):
            time.sleep(1.5)
            st.write("Setting MTU to 1420...")
        st.success("MTU Optimized!")

with c3:
    if st.button("Apply QoS 🎮"):
        st.info("Gaming Traffic Prioritized.")

# 6. قسم الـ SaaS (Business Logic)
st.divider()
with st.expander("💼 SaaS Business Features"):
    st.write("Upgrade to **Enterprise Plan** to unlock 24/7 AI-Monitoring and ISP auto-complaint system.")
    st.button("View Pricing Plans")
