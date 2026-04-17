latency = 120
jitter = 45

col1, col2 = st.columns(2)

col1.metric("Latency", f"{latency} ms")
col2.metric("Jitter", f"{jitter} ms")


if st.button("Run Auto Fix 🤖"):
    st.warning("⚠️ Fixing...")

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
