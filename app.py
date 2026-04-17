import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # عدلها لو عندك سيرفر اونلاين

st.set_page_config(page_title="NetFix AI", layout="centered")

st.title("🚀 NetFix AI - Router Self-Healing")

st.markdown("### 📡 Network Status")

col1, col2 = st.columns(2)

col1.metric("Latency", "120 ms")
col2.metric("Jitter", "45 ms")

st.warning("⚠️ Network Issue Detected")

if st.button("Run Auto Fix 🤖"):
    requests.post(f"{API_URL}/send-command", json={"action": "auto_fix"})
    st.success("Fix in progress...")

st.success("✅ Issue Resolved (Latency: 40ms | Jitter: 10ms)")
