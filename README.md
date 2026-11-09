# Pro Budget Generator

Description: Intelligent system for creating commercial budgets and proposals, integrated with Google Sheets and featuring custom report generation.

An intelligent system for creating, calculating, and managing commercial budgets and proposals, directly integrated with Google Sheets for secure data storage.

## 📁 Repository Structure

- `.streamlit/` - Configuration files for the Streamlit interface and web deployment.
- `src/` - Core Python application source code.
- `tests/` - Automated test suite for validating calculations and connections.
- `requirements.txt` - List of Python dependencies (Streamlit, Pandas, etc.).
- `README.md` - Documentation of the project structure and execution steps.

## 🚀 Features
- **Dynamic Web Interface:** Designed to easily capture client and service data.
- **Cloud Database:** Native integration with Google Sheets to save and query generated budgets.
- **Custom Visuals:** Optimized interface using custom CSS styling for an enhanced visual experience.

## 🛠️ Technologies Used
- **Python** - Core programming language.
- **Streamlit** - Web interface development framework.
- **Pandas** - Agile data table processing and internal calculations.
- **gspread / google-sheets-connection** - Secure connection to the Google Sheets API.

## 🔧 How to Run the Project

1. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Google Sheets Credentials:**
   Place your Google API credentials JSON file in the appropriate directory or configure your `.streamlit/secrets.toml` file.

3. **Execute the Application:**
   Run the following command to start the local development server:
   ```bash
   streamlit run app.py
   ```

## 🧪 Automated Tests and Coverage

To ensure application stability and verify features without modifying core code:

1. **Run Tests:**
   Execute the automated test suite using `pytest`:
   ```bash
   pytest
   ```

2. **Check Test Coverage:**
   To generate a visual report of code coverage, run:
   ```bash
   pytest --cov=src tests/
   ```

