import streamlit as st
import time
import http.client

# 1. إعدادات الصفحة (بتظهر في التاب بتاع المتصفح)
st.set_page_config(page_title="Network Optimizer", page_icon="🚀")

st.title("Network Optimizer 🚀")

with st.sidebar:
    st.header("🔑 Router Access")
    router_ip = st.text_input("Router IP", value="192.168.1.1")
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password")
    
    st.divider()
    st.write("Current Device: **Huawei/DN Router**")# 2. وظيفة قياس البنج الحقيقي (طريقة الـ HTTP عشان تشتغل على GitHub)
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
def login_to_router(ip, user, pwd):
    url = f"http://{ip}/asp/login.asp"
    try:
        # دي محاكاة للدخول، في الحقيقة بنحتاج نبعت الـ Session
        session = requests.Session()
        return session
    except:
        return None

def reboot_router(session, ip):
    # مسار الريبوت لراوترات هواوي/DN
    url = f"http://{ip}/api/system/reboot"
    return True # تجريبي حالياً
# 3. بناء الواجهة (الأعمدة)
col1, col2 = st.columns(2)
message_container = st.empty() # ده عشان يمسح الرسايل القديمة وميكررهاش

# 4. زر التشغيل والمنطق
if st.button("Run Auto Fix & Live Monitor 🤖", key="fix_button"):
    # تنظيف الشاشة من أي رسائل قديمة أول ما ندوس
    message_container.empty()
    
    with st.spinner("🔄 Checking Connection..."):
        latency = get_real_ping()
        jitter = 2 if latency > 0 else 0 
        
        # عرض الأرقام في الأعمدة
        # لاحظ استخدام delta_color="normal" عشان السهم السالب يبقى أخضر
        col1.metric(
            label="Latency", 
            value=f"{latency} ms", 
            delta=f"{latency-60}ms" if latency > 0 else None, 
            delta_color="normal"
      # انزل لآخر الملف خالص
st.divider() 

st.subheader("🛠️ Quick Fixes")
c1, c2, c3 = st.columns(3)

if c1.button("Restart Router 🔄"):
    # هنا الكود بيسحب الـ password اللي أنت كتبته في الـ Sidebar فوق
    if password: 
        st.success(f"Attempting to reboot router at {router_ip}...")
        # هنا بننادي الدالة اللي عرفناها فوق
    else:
        st.error("Please enter router password in sidebar!")

if c2.button("Optimize MTU ⚡"):
    st.info("MTU optimization starting...")

if c3.button("Apply QoS 🎮"):
    st.warning("QoS feature is being configured for your DN router.")  )
        col2.metric(
            label="Jitter", 
            value=f"{jitter} ms", 
            delta=f"{jitter-15}ms" if latency > 0 else None, 
            delta_color="normal"
        )

        # تحديد الحالة بناءً على الرقم اللي طلع
        if latency == 0:
            status = "Disconnected"
            info_text = "❌ Connection Failed."
        elif latency < 60:
            status = "Excellent"
            info_text = f"✅ Connection Optimized (Ping: {latency}ms)"
        elif latency < 100:
            status = "Good"
            info_text = f"✅ Stable Connection (Ping: {latency}ms)"
        else:
            status = "Poor"
            info_text = "⚠️ High Latency detected."

        # 5. عرض النتائج النهائية جوه الـ container عشان تظهر مرة واحدة
        with message_container.container():
            st.info(f"📶 Network Quality: {status}")
            if latency > 0:
                st.success(info_text)
            else:
                st.error(info_text)
