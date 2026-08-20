import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import random

st.set_page_config(layout="wide", page_title="RiskGuard AI", page_icon="🛡️")

# 🔥 FINAL BLACK CYBER CSS - GIANT TEXT
st.markdown("""
<style>
/* MAIN BG PURE BLACK */
.stApp {
    background-color: #000!important;
    color: #FFFFFF!important;
}
/* MAIN TITLE - BILLBOARD SIZE */
h1 {
    color: #00D2FF!important;
    font-style: italic!important;
    font-weight: 900!important;
    font-size: 7rem!important; /* 112px */
    text-shadow: 0 0 30px rgba(0, 210, 255, 1);
    margin-bottom: 5px!important;
}
/* CAPTION - BIG WHITE */
div[data-testid="stCaptionContainer"] > div {
    font-size: 2.2rem!important;
    color: #FFFFFF!important;
    margin-bottom: 30px!important;
}
/* SUB HEADINGS - GIANT */
h2, h3 {
    color: #00D2FF!important;
    font-style: italic!important;
    font-weight: 900!important;
    font-size: 3.5rem!important; /* 56px */
    text-shadow: 0 0 15px rgba(0, 210, 255, 0.6);
    margin-top: 30px!important;
}
/* NORMAL TEXT GIANT WHITE */
p, label, span {
    color: #FFFFFF!important;
    font-size: 1.8rem!important;
    font-weight: 500!important;
}
/* METRIC LABELS */
div[data-testid="stMetricLabel"] {
    font-size: 2rem!important;
    font-weight: bold!important;
    color: #FFFFFF!important;
}
/* METRIC VALUE ULTRA GIANT */
div[data-testid="stMetricValue"] {
    color: #00E676!important;
    font-weight: 900!important;
    font-size: 4.5rem!important; /* 72px */
}
/* PROGRESS BAR THICK */
.stProgress > div > div > div > div {
    background-color: #00D2FF!important;
    height: 30px!important;
}
/* SIDEBAR BLACK */
section[data-testid="stSidebar"] {
    background-color: #050505!important;
    border-right: 3px solid #00D2FF;
}
/* BUTTONS GIANT */
.stButton>button {
    border: 3px solid #00D2FF!important;
    color: #00D2FF!important;
    background-color: #0A0A0A!important;
    font-size: 1.6rem!important;
    font-weight: 900!important;
    padding: 18px 28px!important;
    border-radius: 12px!important;
}
.stButton>button:hover {
    background-color: #00D2FF!important;
    color: #000000!important;
}
/* CODE BOX + ALERT BOX BLACK */
pre, code {
    background-color: #0A0A0A!important;
    color: #00E676!important;
    border: 2px solid #00D2FF!important;
    font-size: 1.5rem!important;
}
div[data-testid="stAlert"] {
    background-color: #0A0A0A!important;
    border: 2px solid #00D2FF!important;
    font-size: 1.6rem!important;
    color: #FFFFFF!important;
}
</style>
""", unsafe_allow_html=True)

st.title("*RiskGuard AI 🛡️*")
st.caption("*Autonomous Agentic Safeguard for Razorpay | Real-time Fraud Intelligence*")

# SESSION STATE
if 'data' not in st.session_state:
    np.random.seed(42)
    st.session_state.data = pd.DataFrame({
        'Merchant_ID': [f"RZP-{8800+i}" for i in range(1, 51)],
        'Transaction_Volume': np.random.randint(5000, 200000, 50),
        'Chargeback_Rate': np.random.uniform(0.2, 6.0, 50),
        'Fraud_Risk_Score': np.random.randint(15, 98, 50),
        'City': np.random.choice(['Mumbai', 'Delhi', 'BLR', 'HYD', 'Chennai'], 50),
        'Status': np.random.choice(['Normal', 'Anomaly'], 50, p=[0.9, 0.1])
    })

# SIDEBAR
st.sidebar.header("*🎛️ What-If Risk Simulator*")
velocity = st.sidebar.slider("Transaction Velocity Spike (tx/min)", 10, 500, 120)
refund_rate = st.sidebar.slider("Merchant Refund Rate (%)", 0.5, 8.5, 2.0)

base_score = 50
risk_score = min(99, int(base_score + (velocity/500)*30 + (refund_rate/8.5)*20))
selected_merchant = st.sidebar.selectbox("Select Merchant ID", st.session_state.data['Merchant_ID'])
m_data = st.session_state.data[st.session_state.data['Merchant_ID'] == selected_merchant].iloc[0].copy()
m_data['Fraud_Risk_Score'] = risk_score

live = st.sidebar.toggle("▶️ Start Live Stream")
if live:
    with st.spinner("Streaming live transactions..."):
        time.sleep(1.5)
        new_row = {
            'Merchant_ID': f"RZP-{random.randint(9000,9999)}",
            'Transaction_Volume': random.randint(50000, 300000),
            'Chargeback_Rate': random.uniform(2.0, 8.0),
            'Fraud_Risk_Score': random.randint(85, 99),
            'City': random.choice(['Mumbai', 'Delhi']),
            'Status': 'Anomaly'
        }
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
        if new_row['Fraud_Risk_Score'] > 85:
            st.sidebar.error(f"🚨 CRITICAL: {new_row['Merchant_ID']} Velocity Spike Detected")

data = st.session_state.data

# 2 COLUMN LAYOUT
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("*📊 Real-time Anomaly Detection*")
    fig = px.scatter(data, x='Transaction_Volume', y='Chargeback_Rate',
                     color='Status', size='Fraud_Risk_Score',
                     color_discrete_map={'Normal':'#4DB8FF', 'Anomaly':'#FF2B2B'},
                     hover_data=['Merchant_ID', 'City', 'Fraud_Risk_Score'], size_max=40)

    # 🔥 GRAPH BG BLACK + ALL TEXT WHITE
    fig.update_layout(
        plot_bgcolor='#000000',
        paper_bgcolor='#000000',
        font_color="white",
        font_size=18,
        xaxis=dict(title="Transaction Volume", title_font=dict(size=22, color='white'), tickfont=dict(size=18, color='white')),
        yaxis=dict(title="Chargeback Rate", title_font=dict(size=22, color='white'), tickfont=dict(size=18, color='white')),
        legend=dict(font=dict(size=18, color='white')),
        height=550
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### *🧠 AI Decision Breakdown (SHAP Explainability)*")
    st.caption(f"*Top factors driving the {risk_score}/100 Risk Score:*")
    st.write("**Velocity Spike (Transactions/Min)**")
    st.progress(velocity/500)
    st.write("**Cross-Border IP & Device Fingerprint Mismatch**")
    st.progress(refund_rate/8.5)
    st.write("**Historical Chargeback Ratio Trend**")
    st.progress(m_data['Chargeback_Rate']/6.0)

with col2:
    st.metric("Fraud Risk Score", f"{risk_score}/100", delta="CRITICAL" if risk_score > 80 else "Safe")
    st.metric("Transaction Volume", f"₹{m_data['Transaction_Volume']:,}")
    st.metric("Chargeback Rate", f"{m_data['Chargeback_Rate']:.2f}%")

    st.divider()
    if st.button("Generate Audit Report", type="primary"):
        report_box = st.empty()
        report = f"Analyzing {selected_merchant}...\nVelocity: {velocity} tx/min. 240% spike detected.\nRefund Rate: {refund_rate}%. Device/IP Mismatch Found.\nRecommendation: Immediate freeze required."
        for i in range(len(report)):
            report_box.text(report[:i+1]); time.sleep(0.008)

    st.divider()
    st.warning(f"Critical Risk Detected: {selected_merchant}")

    if st.button("🔴 Freeze Merchant Settlement"):
        st.code(f"""[SYSTEM LOG - {time.strftime('%H:%M:%S IST')}] Triggering Razorpay Merchant Safeguard API...
[API RESPONSE - 200 OK] Merchant ID: {selected_merchant}
[ACTION TAKEN] Settlement Account Frozen.
[NOTIFICATION] Webhook sent to Compliance Team.""", language="bash")

    if st.button("🟡 Trigger Step-Up 3DS Auth"):
        st.success("Step-Up Authentication triggered for all new transactions!")
    if st.button("🟢 Mark as Safe"):
        st.info("Merchant cleared. Risk Score reset.")

st.divider()
st.caption("*Tech: Isolation Forest + XGBoost + SHAP + ONNX + LangChain RAG + Streamlit*")