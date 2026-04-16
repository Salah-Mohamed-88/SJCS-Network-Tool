import streamlit as st
import os
import time
import requests

ROUTER = "http://192.168.1.1"

# ===== Functions =====
def ping_test():
    result = os.popen("ping -n 4 8.8.8.8").read()

    loss = 0
    if "Lost = 1" in result: loss = 25
    if "Lost = 2" in result: loss = 50
    if "Lost = 3" in result: loss = 75
    if "Lost = 4" in result: loss = 100

    return result, loss

def restart_pppoe():
    try:
        requests.post(ROUTER + "/api/pppoe/reconnect")
        return "PPPoE Restarted"
    except:
        return "Failed"

def reboot_router():
    try:
        requests.post(ROUTER + "/api/device/reboot")
        return "Router Rebooting"
    except:
        return "Failed"

# ===== UI =====
st.set_page_config(page_title="Smart Network Tool", layout="wide")

st.title("📡 Smart Network Auto-Healing")

col1, col2, col3 = st.columns(3)

# Run Test
result, loss = ping_test()

ping_value = "Good"
status = "Stable"

if loss > 25:
    ping_value = "Bad"
    status = "Unstable"

col1.metric("Packet Loss", f"{loss}%")
col2.metric("Ping Status", ping_value)
col3.metric("Network Status", status)

st.text_area("Ping Details", result, height=200)

# Auto Fix Logic
if loss >= 50:
    st.warning("⚠️ High Issue Detected → Auto Fix Running")

    fix = restart_pppoe()
    st.success(fix)

# Manual Buttons
st.subheader("Manual Control")

if st.button("Restart PPPoE"):
    st.success(restart_pppoe())

if st.button("Reboot Router"):
    st.error(reboot_router())
