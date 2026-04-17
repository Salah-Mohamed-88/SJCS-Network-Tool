import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # عدلها لو عندك سيرفر اونلاين

st.set_page_config(page_title="NetFix AI", layout="centered")

st.title("🚀 NetFix AI - Router Self-Healing")

st.markdown("### 📡 Network Status")

col1, col2 = st.columns(2)

latency = 120
jitter = 45

col1, col2 = st.columns(2)

col1.metric("Latency", f"{latency} ms")
col2.metric("Jitter", f"{jitter} ms")


st.button("Run Auto Fix 🤖", key="fix1")
st.button("Run Auto Fix 🤖", key="fix2")

    # simulate improvement
    latency = 80
    jitter = 25

    col1.metric("Latency", f"{latency} ms")
    col2.metric("Jitter", f"{jitter} ms")

    latency = 40
    jitter = 10

    col1.metric("Latency", f"{latency} ms")
    col2.metric("Jitter", f"{jitter} ms")

    st.success("✅ Issue Resolved (Latency: 40ms | Jitter: 10ms)")

st.warning("⚠️ Network Issue Detected")

if st.button("Run Auto Fix 🤖"):
    requests.post(f"{API_URL}/send-command", json={"action": "auto_fix"})
    st.success("Fix in progress...")

st.success("✅ Issue Resolved (Latency: 40ms | Jitter: 10ms)")
