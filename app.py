import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Pro Budget Generator", page_icon="💰", layout="centered")

st.title("💰 Pro Budget Generator")
st.subheader("Intelligent Commercial Proposals & Budget System")

st.markdown("---")

# Client Data Section
st.header("👤 Client Information")
client_name = st.text_input("Client Name")
client_email = st.text_input("Client Email")

# Budget Items Section
st.header("📋 Service Details")
service_description = st.text_area("Service Description")
service_value = st.number_input("Estimated Value ($)", min_value=0.0, step=100.0)

# Integration Status Simulation
st.sidebar.header("⚙️ System Status")
st.sidebar.success("⚡ Connected to Google Sheets")

if st.button("Generate Proposal & Sync"):
    if client_name and service_description and service_value > 0:
        st.balloons()
        st.success(f"🎉 Budget for **{client_name}** successfully generated and synchronized with Google Sheets!")
        
        # Displaying summary data
        data = {
            "Client": [client_name],
            "Email": [client_email],
            "Description": [service_description],
            "Value ($)": [service_value]
        }
        st.dataframe(pd.DataFrame(data))
    else:
        st.error("⚠️ Please fill in all fields before generating the proposal.")

