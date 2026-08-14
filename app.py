import streamlit as st
from PIL import Image
import time

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Kafa Smart Segregation Hub", page_icon="♻️", layout="centered")

# --- HEADER ---
st.title("♻️ Kafa Smart Waste Incentives App")
st.markdown("### *If you mix up waste you are an idiot*")
st.caption("Don't be an idiot, then you will get money")
st.divider()

# --- STEP 1: SIMULATE HOUSEHOLD SCAN ---
st.subheader("Step 1: Scan Household QR/Barcode")
household_id = st.text_input("Enter Household ID or scan Barcode (e.g., kafabintekaderhome):", placeholder="kafazarin")

if household_id:
    st.success(f"✅ Connection Established with Household Account: **{household_id}**")
    
    # --- STEP 2: EVALUATION ---
    st.subheader("Step 2: Van Driver Inspection")
    st.write("Does the household's waste match the partitioned compartments?")
    
    col1, col2 = st.columns(2)
    with col1:
        is_sorted = st.radio("Segregation Status:", ["Properly Sorted (Green & Blue Bins)", "Mixed Trash (Failed Verification)"])
    with col2:
        waste_type = st.selectbox("Primary Waste Feedstock:", ["Organic Food Waste (For AD Plant)", "Textile Jhut/Plastics (For RDF)", "Unsorted/Contaminated"])

    # --- STEP 3: TRANSACTION ---
    st.subheader("Step 3: Process Reward Trigger")
    if st.button("🚀 Log Collection & Process Points"):
        with st.spinner("Syncing data to GCC Central Server..."):
            time.sleep(1.5) # Simulates a network delay
            
        if "Properly Sorted" in is_sorted:
            st.balloons() # Triggers an on-screen celebratory animation
            st.success("### 🎉 Transaction Successful!")
            st.metric(label="bKash Incentive Dispatched", value="+15 BDT", delta="Total Household Points: 240")
            st.info(f"Feedstock successfully tagged as **{waste_type}** and routed to processing hub.")
        else:
            st.error("❌ Transaction Flagged")
            st.warning("No incentives awarded. Household issued a system alert to separate next time.")
