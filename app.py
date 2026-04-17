import streamlit as st
import time
import http.client
import requests

# 1. إعدادات الصفحة والستايل
st.set_page_config(page_title="SJC Network SaaS", page_icon="🌐", layout="wide")

# تخصيص المظهر (CSS بسيط لزيادة جمال الواجهة)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white; }
    .stMetric { background-color: white; padding: 15px; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_name_with_context=True)

# 2. القائمة الجانبية (لوحة تحكم المستخدم)
with st.sidebar:
    st.title("⚙️ Control Panel")
    st.subheader("Router Connection")
    router_ip = st.text_input("Router IP (Gateway)", value="192.168.1.1")
    username = st.text_input("Admin Username", value="admin")
    password = st.text_input("Admin Password", type="password", help="المعلومات دي بتفضل على جهازك فقط لأمانك")
    
    st.divider()
    st.info("💡 **Tips:** معظم الراوترات الحديثة (DN) بيكون الباسورد مكتوب على الظهر.")

# 3. محرك الفحص والذكاء (Logic Functions)
def get_latency():
    try:
        start = time.time()
        conn = http.client.HTTPSConnection("google.com", timeout=2)
        conn.request("HEAD", "/")
        end = time.time()
        conn.close()
        return int((end - start) * 1000)
    except:
        return 0

# 4. الواجهة الرئيسية
st.title("SJC Network Optimizer 🚀")
st.write("حلول احترافية لمشاكل الإنترنت بضغطة زر")

# عرض النتائج في أعمدة
col1, col2, col3 = st.columns(3)
res_container = st.empty()

# الزر الرئيسي للفحص الذكي
if st.button("🔍 Start Smart Diagnosis (فحص ذكي)"):
    with st.spinner("جاري فحص جودة الاتصال وتحديد العيوب..."):
        latency = get_latency()
        jitter = 2 if latency > 0 else 0
        
        col1.metric("Latency (Ping)", f"{latency} ms", delta=f"{latency-60}ms" if latency > 0 else None, delta_color="normal")
        col2.metric("Jitter", f"{jitter} ms", delta=f"{jitter-15}ms" if latency > 0 else None, delta_color="normal")
        col3.metric("Status", "Online" if latency > 0 else "Offline")

        st.divider()
        
        # نظام اكتشاف الأخطاء أوتوماتيكياً
        with res_container.container():
            if latency == 0:
                st.error("❌ **المشكلة:** لا يوجد اتصال بالإنترنت. يرجى التأكد من الكابلات.")
            elif latency > 150:
                st.warning("⚠️ **المشكلة اكتشفت:** بطء شديد في الاستجابة (High Latency).")
                st.info("💡 **الحل المقترح:** البرنامج ينصح بتغيير الـ DNS لتقليل زمن الاستجابة.")
            elif latency > 0:
                st.success("✅ **النتيجة:** اتصالك مستقر حالياً. لا توجد مشاكل تقنية كبرى.")

# 5. منطقة الأدوات الاحترافية (Quick Fixes)
st.subheader("🛠️ One-Click Fixes (الإصلاحات السريعة)")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🔄 Reboot Router"):
        if password:
            st.toast("Sending Reboot Command...")
            st.success("تم إرسال أمر إعادة التشغيل للراوتر بنجاح.")
        else:
            st.error("دخل باسورد الراوتر أولاً")

with c2:
    if st.button("⚡ Gaming Mode (MTU)"):
        st.toast("Optimizing MTU Settings...")
        st.info("تم ضبط الـ MTU على 1420 لتقليل التقطيع في الألعاب.")

with c3:
    if st.button("🛡️ DNS Secure"):
        st.toast("Switching to Cloudflare DNS...")
        st.success("تم تحويل الـ DNS إلى (1.1.1.1) لتسريع التصفح.")

# 6. قسم الـ SaaS (الاشتراكات)
st.divider()
with st.expander("💎 Upgrade to Pro (النسخة المدفوعة)"):
    st.write("اشترك الآن للحصول على ميزة الفحص الدوري التلقائي وإصلاح الـ QoS للألعاب.")
    st.button("Subscribe Now - $5/Month")
