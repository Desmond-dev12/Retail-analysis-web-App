<<<<<<< HEAD
# 💊 Pharmacy Sales & Revenue Analytics Dashboard

An interactive, multi-tab Streamlit web application engineered to clean, analyze, and display sales performance, category margins, and daily volume trends across pharmacy branches.

---

## 📌 Executive Summary
This project processes raw transaction data to provide branch managers with real-time operational insights. It evaluates store-level performance, tracks fast-moving consumer health items, and provides strategic recommendations to optimize inventory restocking windows.

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Plotly Express
* **Web UI Framework:** Streamlit
* **Version Control:** Git & GitHub

## 🚀 App Features & Architecture
* **Global Sidebar Filtering:** Dynamic slicing by Branch and Date Range across all metrics.
* **Executive Metrics:** Live calculated KPI cards for Total Revenue, Transaction Volume, and Average Order Value.
* **Structured Multi-Tab Design:**
  * **Data View:** Filtered raw dataset inspection and verification.
  * **Sales Analytics:** Categorical revenue charts, customer satisfaction scores, and daily sales trends.
  * **Developer Profile:** Key operational takeaways and direct contact links.

## 📊 Key Business Recommendations
* **Inventory Restocking Alignment:** Shift primary inventory replenishment to Wednesday afternoons to support peak sales spikes occurring on Thursdays and Fridays.
* **Core Product Protection:** Maintain safety stock buffers for high-volume drivers (Painkillers and Skincare) to eliminate stockout risks.
* **Customer Loyalty Growth:** Introduce targeted perks to convert the ~49% non-member customer baseline into registered loyalty members.

---

## ⚙️ Local Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Desmond12-dev/pharmacy-sales-dashboard.git](https://github.com/Desmond1-dev/pharmacy-sales-dashboard.git)
=======
# Universal Data Cleaner

Universal Data Cleaner is a simple data-cleaning and conversion app built with Python and Streamlit.

It helps users upload CSV and Excel files, clean the data, review key metrics, visualize patterns, and export the cleaned file in a new format.

## Project overview

This app is designed for people working with messy spreadsheet data. It makes it easier to:

- clean up raw files
- remove duplicate records
- fill missing numeric values
- select useful columns
- review key dataset information
- create quick visual insights
- export cleaned data back into CSV or Excel

## Main features

- upload multiple CSV and Excel files
- preview the first rows of each dataset
- remove duplicate rows
- fill missing numeric values using the column average
- select which columns to keep before export
- view bar, line, scatter, and histogram charts
- review summary statistics
- detect common sales-related KPI columns when they exist
- convert data into CSV or Excel format
- download the cleaned file

## Why this project matters

This project shows practical data-handling skills using real tools that are widely used in analytics and business work.

It combines:

- file processing
- data cleaning
- data analysis
- business KPI checks
- data visualization
- user interface building

## Tech stack

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL

## Project structure

- `unicleaner1.py` - main Streamlit app
- `requirements.txt` - project dependencies
- `README.md` - project documentation

## Installation

1. Open the project folder in your terminal.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the app

From the project folder, run:

```bash
streamlit run unicleaner1.py
```

Then open the local URL shown in the terminal in your browser.

## How to use

1. Upload one or more CSV or Excel files.
2. Review the preview and summary report.
3. Clean the dataset if needed.
4. Choose which columns to keep.
5. Turn on the visualization section if you want charts.
6. Select the output format: CSV or Excel.
7. Click the download button to save the cleaned file.

## Example use case

A user may receive sales data in Excel format, remove duplicate entries, fill missing values, review the summary metrics, and export the cleaned data for reporting or further analysis.

## Planned improvements

- improve validation for unusual or broken files
- add stronger text-cleaning options
- add more missing-value handling choices
- improve dashboard styling
- add more business KPIs and data checks
- deploy the app online for public access

## License

This project is intended for learning, personal use, and portfolio development.
>>>>>>> 4d52e79 (Add projects files)
