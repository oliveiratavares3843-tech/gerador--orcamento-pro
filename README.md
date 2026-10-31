Pro Budget Generator 💼
Description: Intelligent system for creating commercial budgets and proposals, integrated with Google Sheets and featuring custom report generation.

🔗 CLICK HERE TO ACCESS THE ONLINE GENERATOR

An intelligent system for creating, calculating, and managing commercial budgets and proposals, directly integrated with Google Sheets for secure data storage.

🚀 Features
Dynamic Web Interface: Designed to easily capture client and service data.

Cloud Database: Native integration with Google Sheets to save and query generated budgets.

Custom Visuals: Optimized interface using custom CSS styling for an enhanced visual experience.

Data Manipulation: Uses Pandas for agile data table processing and internal calculations.

🛠️ Technologies Used
Python

Streamlit (Web interface development)

Pandas (Data structuring and processing)

st-gsheets-connection (Secure connection to the Google Sheets API)

📦 How to Install and Run
Clone the repository to your local machine.

Make sure to install the required dependencies listed in requisitos.txt:

Bash
pip install -r requisitos.txt
Run the Streamlit server:

Bash
streamlit run app.py
🔐 Database Configuration (.toml)
For the Google Sheets integration to work correctly, remember to configure your credentials in the local .streamlit/secrets.toml directory or in the Secrets tab of Streamlit Cloud.
