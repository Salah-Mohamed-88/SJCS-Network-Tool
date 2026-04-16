import streamlit as st
import os
import requests

ROUTER = "http://192.168.1.1"

# ===== Functions (الأوامر) =====
def ping_test():
    result = os.popen("ping -c 4 8.8.8.8").read()
    loss = 0
    if "Lost = 1" in result: loss = 25
    if "Lost = 2" in result: loss = 50
    if "Lost = 3" in result: loss = 75
    if "Lost = 4" in result: loss = 100
    return result, loss

def restart_pppoe():
    try:
        requests.post(ROUTER + "/api/pppoe/reconnect")
        return "PPPoE Restarted Successfully"
    except:
        return "Connection to Router Failed"

def change_dns():
    try:
        requests.post(ROUTER + "/api/network/dns", json={"dns": "8.8.8.8"})
        return "DNS Optimized to 8.8.8.8"
    except: return "DNS Fix Failed"

def fix_mtu():
    try:
        requests.post(ROUTER + "/api/network/mtu", json={"mtu": 1420})
        return "MTU adjusted to 1420"
    except: return "MTU Fix Failed"

def toggle_qos():
    try:
        requests.post(ROUTER + "/api/qos", json={"status": "enable"})
        return "QoS Activated"
    except: return "QoS Fix Failed"

# ===== UI (الواجهة) =====
st.set_page_config(page_title="SJCS Tool", layout="wide")
st.title("📡 Smart Jitter Control System (SJCS)")

# تشغيل الفحص
result, loss = ping_test()

# عرض النتائج
col1, col2, col3 = st.columns(3)
col1.metric("Packet Loss", f"{loss}%")
col2.metric("Status", "Stable" if loss < 50 else "Unstable")
col3.metric("Action Engine", "Monitoring" if loss < 50 else "Fixing...")

st.text_area("Live Ping Log", result, height=150)

# ===== Decision Engine (الحل التلقائي) =====
if loss >= 50:
    st.error("🚨 High Jitter Detected! Triggering Auto-Fix...")
    st.info(change_dns())
    st.info(fix_mtu())
    st.info(toggle_qos())
    st.success(restart_pppoe())

# ===== Manual Buttons (التحكم اليدوي) =====
st.divider()
st.subheader("Manual Control Panel")
c1, c2, c3, c4 = st.columns(4)

if c1.button("Restart PPPoE"):
    st.write(restart_pppoe())
if c2.button("Optimize DNS"):
    st.write(change_dns())
if c3.button("Adjust MTU"):
    st.write(fix_mtu())
if c4.button("Enable QoS"):
    st.write(toggle_qos())
