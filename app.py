import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Pro Budget Generator", page_icon="💰", layout="centered")

# Session state initialization
if "page" not in st.session_state:
    st.session_state.page = "home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Demo credentials for recruiters and visitors
DEMO_USERS = {
    "recruiter": "demo2026",
    "admin": "1234"
}

# --- SCREEN 1: HOME PAGE ---
def home_screen():
    st.title("💰 Welcome to Pro Budget Generator")
    st.subheader("Intelligent Commercial Proposals & Budget System")
    st.markdown("---")
    st.write("Create professional commercial proposals in seconds and synchronize your data seamlessly with Google Sheets.")
    
    st.write("")
    if st.button("Access System ➡️", type="primary"):
        st.session_state.page = "login"
        st.rerun()

# --- SCREEN 2: LOGIN PAGE ---
def login_screen():
    st.title("🔐 System Login")
    st.subheader("Enter your credentials to access the generator")
    st.markdown("---")

    # Box displaying test credentials for recruiters
    st.info("👋 **Recruiter / Visitor Demo Access:**\n\n* **Username:** `recruiter`\n* **Password:** `demo2026`")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", type="primary"):
            # Checks both demo users and optional Streamlit Secrets
            secrets_users = st.secrets.get("usuarios", {}) if hasattr(st, "secrets") else {}
            valid_users = {**DEMO_USERS, **secrets_users}

            if username in valid_users and str(valid_users[username]) == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.session_state.page = "system"
                st.rerun()
            else:
                st.error("⚠️ Invalid username or password.")
    with col2:
        if st.button("⬅️ Back to Home"):
            st.session_state.page = "home"
            st.rerun()

# --- SCREEN 3: BUDGET GENERATOR ---
def system_screen():
    st.sidebar.header("👤 Active Session")
    st.sidebar.info(f"Logged in as: **{st.session_state.current_user}**")
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "home"
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.header("⚙️ System Status")
    st.sidebar.success("⚡ Connected to Google Sheets")

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

    if st.button("Generate Proposal & Sync", type="primary"):
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

# --- ROUTING CONTROL ---
if st.session_state.page == "home":
    home_screen()
elif st.session_state.page == "login":
    login_screen()
elif st.session_state.page == "system":
    if st.session_state.logged_in:
        system_screen()
    else:
        st.session_state.page = "login"
        st.rerun()

