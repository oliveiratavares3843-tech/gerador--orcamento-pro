# 💰 Pro Budget Generator

An intelligent commercial proposal and budget generation web application built with **Python**, **Streamlit**, and **Pandas**. Designed to streamline sales workflows with structured client data capture, automated proposal summaries, and cloud spreadsheet synchronization.

🔗 **Live Demo:** [Insert your Streamlit App URL here]

---

## 🔐 Demo Credentials (For Recruiters & Evaluators)

To test the full authentication flow and system features immediately, use the following credentials on the login screen:

* **Username:** `recruiter`
* **Password:** `demo2026`

---

## ✨ Key Features

* **3-Stage Navigation & Authentication Flow:** Structured routing (`Home` $\rightarrow$ `Login` $\rightarrow$ `System`) managed via `st.session_state` with secure session validation and logout controls.
* **Secrets Management Ready:** Built-in support for `st.secrets` to safely store production credentials outside the public codebase.
* **Commercial Proposal Builder:** Clean interface for capturing client details, service descriptions, and estimated pricing.
* **Structured Data Preview:** Real-time tabular summary of generated proposals using Pandas DataFrames.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Frontend & Routing:** Streamlit
* **Data Processing:** Pandas

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd pro-budget-generator
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

