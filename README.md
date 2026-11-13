# 💰 Pro Budget Generator

![Python](https://shields.io)
![Streamlit](https://shields.io)
![Pandas](https://shields.io)
![Security](https://shields.io)

An intelligent commercial proposal and budget generation web application built with **Python**, **Streamlit**, and **Pandas**. Designed to streamline sales workflows with structured client data capture, automated proposal summaries, and cloud spreadsheet synchronization.

🔗 **Live Demo:** **[Access the Pro Budget Generator](https://gerador--orcamento-pro.streamlit.app/)**

---

## 🔐 Demo Credentials (For Recruiters & Evaluators)

To test the full authentication flow and system features immediately, use the following credentials on the login screen:

* **Username:** `recruiter`
* **Password:** `demo2026`

---

## ✨ Key Features

* **3-Stage Navigation & Authentication Flow:** Structured routing (`Home → Login → System`) managed via `st.session_state` with secure session validation and logout controls.
* **Secrets Management Ready:** Built-in support for `st.secrets` to safely store production credentials outside the public codebase.
* **Commercial Proposal Builder:** Clean interface for capturing client details, service descriptions, and estimated pricing.
* **Structured Data Preview:** Real-time tabular summary of generated proposals using Pandas DataFrames.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Frontend & Routing:** Streamlit
* **Data Processing:** Pandas

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd gerador--orcamento-pro
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```
