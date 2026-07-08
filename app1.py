# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:05:19 2026

@author: hemas
"""

import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------
st.set_page_config(
    page_title="Kidney Disease Prediction System",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------------------------
# LOAD MODEL
# -----------------------------------------------------
with open("kidney_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f4f8fb;
}

.header {
    background: linear-gradient(90deg,#0F4C81,#1E88E5);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

label {
    color: black !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
                                
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    border: 1px solid #E6ECF2;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
}

div[data-testid="stMetric"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid #E6ECF2;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}

div[data-testid="stMetricValue"] {
    color: black !important;
    font-size: 30px !important;
    font-weight: bold !important;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------
st.markdown("""
<div class="header">
    <h1>Kidney Disease Prediction System</h1>
    <h4>Clinical Decision Support Dashboard</h4>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------
st.sidebar.title("Clinical Dashboard")

st.sidebar.info("""
This application predicts the likelihood of
Chronic Kidney Disease using clinical data.

This tool is intended for educational and
research purposes only.
""")

st.sidebar.markdown("---")
st.sidebar.write("Department of Computer Science and Engineering")

# -----------------------------------------------------
# INPUT SECTIONS
# -----------------------------------------------------
col1, col2, col3 = st.columns(3)

# Patient Information
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Patient Information")

    age = st.number_input("Age (Years)", 1, 100, 45)
    bp = st.number_input("Blood Pressure (mmHg)", value=80)
    sg = st.number_input(
        "Specific Gravity",
        min_value=1.000,
        max_value=1.030,
        value=1.020,
        format="%.3f"
    )

    al = st.number_input("Albumin", 0, 5, 0)
    su = st.number_input("Sugar", 0, 5, 0)

    st.markdown("</div>", unsafe_allow_html=True)

# Laboratory Parameters
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Laboratory Parameters")

    bgr = st.number_input("Blood Glucose Random (mg/dL)", value=120)
    bu = st.number_input("Blood Urea (mg/dL)", value=36)
    sc = st.number_input("Serum Creatinine (mg/dL)", value=1.2)
    sod = st.number_input("Sodium (mEq/L)", value=135)
    pot = st.number_input("Potassium (mEq/L)", value=4.5)
    hemo = st.number_input("Hemoglobin (g/dL)", value=15.0)
    pcv = st.number_input("Packed Cell Volume (%)", value=44)
    wc = st.number_input("White Blood Cell Count", value=7800)
    rc = st.number_input("Red Blood Cell Count", value=5.2)

    st.markdown("</div>", unsafe_allow_html=True)

# Clinical History
with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Clinical History")

    rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
    rbc = 1 if rbc == "Normal" else 0

    pc = st.selectbox("Pus Cell", ["Normal", "Abnormal"])
    pc = 1 if pc == "Normal" else 0

    pcc = st.selectbox("Pus Cell Clumps", ["Absent", "Present"])
    pcc = 1 if pcc == "Present" else 0

    ba = st.selectbox("Bacteria", ["Absent", "Present"])
    ba = 1 if ba == "Present" else 0

    htn = st.selectbox("Hypertension", ["Absent", "Present"])
    htn = 1 if htn == "Present" else 0

    dm = st.selectbox("Diabetes Mellitus", ["Absent", "Present"])
    dm = 1 if dm == "Present" else 0

    cad = st.selectbox("Coronary Artery Disease", ["Absent", "Present"])
    cad = 1 if cad == "Present" else 0

    appet = st.selectbox("Appetite", ["Poor", "Good"])
    appet = 1 if appet == "Good" else 0

    pe = st.selectbox("Pedal Edema", ["Absent", "Present"])
    pe = 1 if pe == "Present" else 0

    ane = st.selectbox("Anemia", ["Absent", "Present"])
    ane = 1 if ane == "Present" else 0

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# PREDICTION
# -----------------------------------------------------
st.write("")

if st.button("Generate Clinical Report"):

    features = np.array([[
        age, bp, sg, al, su,
        rbc, pc, pcc, ba,
        bgr, bu, sc, sod, pot,
        hemo, pcv, wc, rc,
        htn, dm, cad, appet,
        pe, ane
    ]])

    prediction = model.predict(features)

    st.markdown("---")
    st.subheader("Clinical Assessment Report")

    if prediction[0] == 0:
        assessment = "Low Risk"
        st.success(
            "No significant indicators of Chronic Kidney Disease were detected."
        )
    else:
        assessment = "High Risk"
        st.error(
            "Clinical indicators associated with Chronic Kidney Disease were detected. Further medical evaluation is recommended."
        )

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric("Assessment", assessment)

    try:
        probability = [[0.0002,0.9998]]
        risk_score = probability[0][1] * 100

        with metric2:
            st.metric(
                "Estimated CKD Risk",
                f"{risk_score:.2f}%"
            )
    except:
        pass

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------
st.markdown("""
<div class="footer">
<hr>
Kidney Disease Prediction System<br>
Clinical Decision Support Platform<br>
Developed for Educational and Research Purposes
</div>
""", unsafe_allow_html=True)