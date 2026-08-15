import streamlit as st
import time
from PIL import Image

# --- STYLING HOOKS (Injects CSS to enforce absolute readability and colors) ---
st.set_page_config(page_title=" Green Rewards", page_icon="🌸", layout="wide")

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
col_main, col_mascot = st.columns(2)

with col_main:
    # We use Streamlit container columns to hold our custom layout fields
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    
    # Left content arrangement split into Text data vs Local Mascot layout
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
            <h1 style="margin: 0; font-size: 28px;">Hi, Kafa! ✨</h1>
            <p style="color: #7F1D1D; font-size: 15px; margin-top: 5px; margin-bottom: 15px;">
                Glad to see you again.
            </p>
            <hr style="border: 0.5px solid #E2E8F0; margin: 15px 0;">
            <p style="color: #7F1D1D; font-weight: 600; font-size: 14px; margin-bottom: 5px;">⚡ Trash Talk that actually helps:</p>
            <p style="margin: 0; font-size: 13px;"> Think before you throw</p>
            <p style="margin: 0; font-size: 13px;"> Trash has a bad habit of coming back to bite us</p>
        """, unsafe_allow_html=True)
    with c2:
        try:
            # Native relative local path calling bypassing GitHub web errors
            img_mascot = Image.open("mascot.png")
            st.image(img_mascot, use_container_width=True)
        except:
            st.caption("Mascot loading...")
            
    st.markdown('</div>', unsafe_allow_html=True)

with col_mascot:
    st.markdown('<div class="dashboard-card" style="text-align: center;">', unsafe_allow_html=True)
    try:
        # Native relative path calling for Oggy's local jpeg file asset
        img_cat = Image.open("cat.jpeg")
        st.image(img_cat, width=130)
    except:
        st.caption("Cat avatar loading...")
    st.markdown("""
        <h4 style="margin-top: 10px; color: #7F1D1D;">Eco Assistant, Oggy 🐾</h4>
        <p style="font-size: 13px; color: #7F1D1D; margin: 5px 0 0 0; font-weight: bold;">Keep Our World Clean!</p>
        </div>
    """, unsafe_allow_html=True)

# Interactive Form Elements wrapped in an administrative sub-panel
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.subheader(" Household Verification Panel")

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
                st.metric(label="Incentive Transferred via bKash", value="+26.00 BDT")
            with m_col2:
                st.metric(label="Feedstock System Routing", value=waste_type)
        else:
            st.error("❌ Transaction Denied: Guidelines Not Met.")
            # Displays a fallback text system safely handled by the application logic
            st.warning('"Hmph! Bad guy, no money for you!" 💢')
            
st.markdown('</div>', unsafe_allow_html=True)
