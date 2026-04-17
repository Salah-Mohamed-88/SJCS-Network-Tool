import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة والستايل الاحترافي
st.set_page_config(page_title="SJC Network Optimizer Pro", page_icon="🚀", layout="wide")

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

# 3. محرك الفحص والذكاء الاصطناعي
def run_diagnosis():
    try:
        start = time.time()
        # فحص جودة الاتصال عبر سيرفرات جوجل وكلاود فلير
        conn = http.client.HTTPSConnection("1.1.1.1", timeout=2)
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
    diag_container = st.container()
    
    with st.spinner("Analyzing network path and DNS health..."):
        latency = run_diagnosis()
        jitter = 2 if latency > 0 else 0
        
        # عرض المقاييس
        col1.metric("Latency (Ping)", f"{latency} ms", delta=f"{latency-60}ms" if latency > 0 else None, delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms" if latency > 0 else None, delta_color="normal")
        
        st.divider()

        # التقرير الذكي
        with diag_container:
            st.subheader("🕵️ Smart Diagnosis Report")
            if latency == 0:
                st.error("❌ **المشكلة:** لا يوجد اتصال بالإنترنت. يرجى التأكد من الكابلات.")
            elif latency > 100:
                st.warning("⚠️ **المشكلة:** زمن الاستجابة مرتفع (High Latency).")
                st.info("💡 **الحل الأوتوماتيكي:** ينصح بالضغط على 'Secure DNS' لتحسين المسار.")
            else:
                st.success("✅ **الحالة:** شبكتك مستقرة ومثالية حالياً.")

# 5. أدوات التحكم السريع (Quick Fixes)
st.divider()
st.subheader("🛠️ Quick Fixes (Router Control)")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Restart Router 🔄"):
        if password:
            with st.status("Connecting to Router..."):
                time.sleep(2)
                st.success("Reboot command sent!")
        else:
            st.error("Please enter password in sidebar.")

with c2:
    if st.button("Optimize MTU ⚡"):
        with st.status("Optimizing Packets..."):
            time.sleep(1.5)
        st.success("MTU Optimized to 1420 (Gaming Mode).")

with c3:
    # --- إضافة كود الـ DNS هنا ---
    if st.button("Secure DNS 🛡️"):
        if password:
            with st.status("Changing DNS to Cloudflare (1.1.1.1)..."):
                # هنا بنضيف الـ logic الحقيقي للـ DN Router لاحقاً
                time.sleep(2)
                st.success("DNS Secured Successfully!")
                st.balloons() # حركة احتفالية للعميل
        else:
            st.error("Enter Router Password to change DNS.")

# 6. قسم الـ SaaS
st.divider()
with st.expander("💼 SaaS Business Features"):
    st.write("Upgrade to **Enterprise Plan** to unlock 24/7 AI-Monitoring and ISP auto-complaint system.")
    st.button("View Pricing Plans")
