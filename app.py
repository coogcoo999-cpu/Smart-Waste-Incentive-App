import streamlit as st
import time

# --- STYLING HOOKS (Injects CSS to enforce absolute readability and colors) ---
st.set_page_config(page_title="Green Rewards", page_icon="🌸", layout="wide")

st.markdown("""
    <style>
    /* Main background styling set to a soft light red */
    .stApp {
        background-color: #FEE2E2;
    }
    
    /* Soft white human-designed card styling */
    .dashboard-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0px 4px 20px rgba(149, 157, 165, 0.1);
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
    }
    
    /* Global Text Enforcements to Deep Dark Red */
    p, span, label, .stRadio, .stSelectbox, div[data-testid="stMarkdownContainer"] p {
        color: #7F1D1D !important;
        font-weight: 500;
    }
    
    /* Global Header Enforcements to Deep Dark Red */
    h1, h2, h3, h4, h5, h6 {
        color: #7F1D1D !important;
        font-family: 'Inter', sans-serif;
        font-weight: bold !important;
    }
    
    /* Forcing the text input box background to remain Solid White with dark text */
    div[data-testid="stTextInput"] input {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---
# Main grid split: Hero Card (Left) and Mascot Panel (Right)
col_main, col_mascot = st.columns(2)

with col_main:
    st.markdown("""
        <div class="dashboard-card" style="display: flex; align-items: center; justify-content: space-between;">
            <div style="flex: 1; padding-right: 15px;">
                <h1 style="margin: 0; font-size: 28px;">Hi, Kafa! ✨</h1>
                <p style="color: #7F1D1D; font-size: 15px; margin-top: 5px; margin-bottom: 15px;">
                    Glad to see you again.
                </p>
                <hr style="border: 0.5px solid #E2E8F0; margin: 15px 0;">
                <p style="color: #7F1D1D; font-weight: 600; font-size: 14px; margin-bottom: 5px;">⚡ Trash Talk that actually helps:</p>
                <ul style="color: #7F1D1D; padding-left: 20px; line-height: 1.6; font-size: 13px; margin: 0;">
                    <li> Think before you throw</li>
                    <li> Trash has a bad habit of coming back to bite us</li>
                </ul>
            </div>
            <!-- Your Custom Anime Girl Visual Anchor Block -->
            <div style="text-align: center; margin-left: 10px;">
                <img src="https://githubusercontent.com" style="width: 120px; height: 120px; border-radius: 12px; object-fit: cover;">
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_mascot:
    st.markdown("""
        <div class="dashboard-card" style="text-align: center; padding: 20px; height: 100%;">
            <!-- Your Cat's Photo Asset (.jpeg format matching your repository configuration) -->
            <img src="https://githubusercontent.com" style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; margin-bottom: 10px; border: 3px solid #7F1D1D;">
            <h4 style="margin: 0; color: #7F1D1D;">Eco Assistant, Oggy 🐾</h4>
            <p style="font-size: 13px; color: #7F1D1D; margin: 5px 0 0 0; font-weight: bold;">Keep Our World Clean!</p>
        </div>
    """, unsafe_allow_html=True)

# Interactive Form Elements wrapped in an administrative sub-panel
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.subheader("📌 Household Verification Panel")

household_id = st.text_input("Scan or Enter Household Account ID:", placeholder="e.g., kafa's home")

if household_id:
    st.markdown(f"Status: <span style='color: #2563EB; font-weight: bold;'>Account Found ({household_id})</span>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        is_sorted = st.radio("Field Inspection Result:", ["Properly Separated (Green/Blue Bins Match)", "Unsorted Mixed Trash (Failed Verification)"])
    with col2:
        waste_type = st.selectbox("Primary Tagged Feedstock:", ["Organic Material (AD Route)", "Textile Jhut & Plastics (RDF Route)", "Contaminated Residue"])

    st.write("")
    if st.button("➕ Log Entry & Get Rewards"):
        with st.spinner("Processing ledger transaction..."):
            time.sleep(1.2)
            
        if "Properly Separated" in is_sorted:
            st.balloons()
            st.success("### 🎉 Good job, buddy!")
            
            # Metric blocks matching dashboard card styles
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric(label="Incentive Transferred via bKash", value="+15.00 BDT")
            with m_col2:
                st.metric(label="Feedstock System Routing", value=waste_type)
        else:
            # --- DYNAMIC ERROR REACTION INJECTED HERE ---
            st.error("❌ Transaction Denied: Guidelines Not Met.")
            
            # Displays a cute, grumpy anime girl giving a thumbs down on failure conditions
            st.markdown("""
                <div style="text-align: center; margin-top: 20px; padding: 15px; background-color: #FFF1F2; border-radius: 12px; border: 1px dashed #FDA4AF;">
                    <img src="https://pngtree.com" style="width: 130px; object-fit: contain;">
                    <p style="color: #9F1239; font-weight: bold; margin-top: 10px; font-size: 14px;">
                        "Hmph! Bad guy, no money for you!" 💢
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
st.markdown('</div>', unsafe_allow_html=True)
