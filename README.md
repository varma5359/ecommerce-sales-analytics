# 🛒 E-Commerce Sales Performance & Customer Analytics

A data-driven business analytics dashboard for exploring e-commerce sales, customer value, product performance, and data quality using Python and Streamlit.

This project is designed to help business teams answer operational questions such as:

- How much revenue is generated over time?
- Which categories and products perform best?
- Which regions contribute most to sales?
- Who are the highest-value customers?
- Are there outliers or data quality issues in the dataset?

---

## ✨ Features

- Interactive multi-page Streamlit dashboard
- CSV/Excel upload support
- Automatic validation of required columns and data quality checks
- Data cleaning and standardization for analysis
- KPI cards for sales, orders, customers, units, and average order value
- Sales trend analysis by time period
- Category and regional performance views
- Customer segmentation and spend analysis
- Product-level revenue and low-performing product insights
- Statistical analysis with correlation, covariance, and IQR outlier detection
- Downloadable filtered results and summaries

---

## 🧰 Tech Stack

- Python 3.11+
- Pandas
- NumPy
- Streamlit
- Plotly
- OpenPyXL
- Pytest

---

## 📁 Project Structure

```text
ecommerce_analytics/
├── app.py                     # Main dashboard entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── flow.bat                  # Optional Windows run helper
├── config/
│   └── config.py             # App configuration, required columns, and constants
├── data/
│   ├── ecommerce_data.csv    # Default dataset
│   └── data_dictionary.md    # Data definitions and field descriptions
├── docs/
│   ├── business_requirements.md
│   ├── kpi_definitions.md
│   ├── data_quality_report.md
│   └── final_presentation.md
├── notebooks/
│   └── exploration.ipynb
├── pages/
│   ├── dashboard.py          # Executive overview
│   ├── sales.py              # Time-based and category/region sales analysis
│   ├── customers.py          # Spending and customer segmentation
│   ├── products.py           # Product and category performance
│   ├── statistics.py         # Statistical measures and outlier analysis
│   └── data_quality.py       # Data validation and quality dashboard
├── src/
│   ├── data_loader.py        # Dataset import and preview logic
│   ├── validation.py         # Data validation checks
│   ├── data_cleaning.py      # Cleaning and transformation logic
│   ├── kpi.py                # KPI calculations
│   ├── statistics.py         # Descriptive statistics and anomaly detection
│   ├── sales_analysis.py     # Sales aggregations and time-series logic
│   ├── customer_analysis.py  # Customer spend and segmentation logic
│   ├── product_analysis.py   # Product analytics logic
│   ├── insights.py           # Business insights and recommendations
│   └── page_utils.py         # Shared dashboard utilities
├── tests/
│   ├── test_data.py
│   ├── test_kpi.py
│   ├── test_statistics.py
│   └── test_validation.py
├── assets/
│   └── style.css
└── env/                      # Local virtual environment
```

---

## 🚀 Getting Started

### 1. Clone or open the project

```bash
cd "d:\Python\E-Commerce Sales Performance & Customer Analytics\ecommerce_analytics"
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

---

## 📊 Dashboard Pages

The app includes the following sections:

- Dashboard: KPI overview, monthly trends, category and regional sales
- Sales: time-series performance, order counts, product/category filters
- Customers: spend statistics, top customers, customer segmentation
- Products: best- and weakest-performing products, category summary
- Statistics: mean, median, variance, IQR, correlations, covariance, outliers
- Data Quality: validation, invalid rows, and missing-value diagnostics

---

## 🧪 Data Requirements

The app expects transaction data with the following columns:

- order_id
- order_date
- customer_id
- product_id
- category
- region
- quantity
- unit_price
- discount
- sales

If required columns are missing, the app displays a clear validation error and stops analysis.

The dataset can be loaded from:

- CSV files
- Excel files (.xlsx / .xls)

---

## ✅ Validation and Cleaning

Before analysis, the app performs validation to check:

- required fields are present
- duplicate orders are identified
- quantity values are valid
- unit prices are positive
- discount values are within the allowed range
- dates can be parsed correctly

The cleaned dataset is then used for KPI and chart calculations so reports stay consistent with the underlying data.

---

## 🧠 Business Value

This project supports business analysis across multiple functional areas:

- Sales management: understand revenue trends and growth patterns
- Category planning: compare product and category performance
- Regional analysis: identify strong and weak geographies
- Customer analytics: find top spenders and segment customer value
- Data quality monitoring: detect invalid or low-quality records early
- Executive reporting: review metrics from a single dashboard

---

## 🧾 Testing

The repository includes pytest tests for data validation, KPI calculation, and statistical checks.

Run tests with:

```bash
pytest
```

---

## ❓ Business Questions Answered

The project answers the business questions defined in the original requirements and several additional questions that emerged during implementation.

### Sales Questions

| # | Question | Answered in |
|---|----------|--------------|
| 1 | What is total revenue? | `app.py` KPI: Total Sales |
| 2 | How many orders were placed? | `app.py` KPI: Total Orders |
| 3 | What is the average order value? | `app.py` KPI: Average Order Value |
| 4 | How are sales changing over time? | `pages/dashboard.py`, `pages/sales.py` |
| 5 | Which months generate the highest sales? | `pages/sales.py` monthly bar chart |

### Product Questions

| # | Question | Answered in |
|---|----------|--------------|
| 6 | Which categories generate the highest sales? | `pages/dashboard.py`, `pages/products.py` |
| 7 | Which products generate the highest revenue? | `pages/products.py` Top 10 products chart |
| 8 | Which products have low sales volume? | `pages/products.py` low performers chart |

### Customer Questions

| # | Question | Answered in |
|---|----------|--------------|
| 9 | How much does the typical customer spend? | `pages/customers.py` mean + median values |
| 10 | Who are the high-value customers? | `pages/customers.py` Top 10 chart |
| 11 | How are customers distributed by spending? | `pages/customers.py` Low/Medium/High segmentation |

### Region Questions

| # | Question | Answered in |
|---|----------|--------------|
| 12 | Which regions generate the most revenue? | `pages/dashboard.py`, `pages/sales.py` |
| 13 | Which regions have low sales? | `pages/dashboard.py`, `pages/sales.py` |

### Statistics Questions

| # | Question | Answered in |
|---|----------|--------------|
| 14 | What are mean, median and mode? | `pages/statistics.py` |
| 15 | How variable are order values? | `pages/statistics.py` variance + standard deviation |
| 16 | What are Q1, Q2 and Q3? | `pages/statistics.py` quartiles |
| 17 | What is the IQR? | `pages/statistics.py` Q3 − Q1 |
| 18 | Are there potential outliers? | `pages/statistics.py` IQR outlier analysis |
| 19 | Is discount related to sales? | `pages/statistics.py` correlation analysis |
| 20 | Is quantity related to sales? | `pages/statistics.py` user-selected correlation |

### Additional Business Questions Added During Development

| # | Question | Answered in |
|---|----------|--------------|
| 21 | Which region is weakest? | `src/insights.py` |
| 22 | Is average much higher than median? | `src/insights.py` |
| 23 | Do customers repeat purchase? | `src/insights.py` recommendations |
| 24 | What is the outlier transaction? | `pages/statistics.py` outlier table |
| 25 | How many rows have data issues? | `pages/data_quality.py` |
| 26 | What is the covariance between two variables? | `pages/statistics.py` |
| 27 | What does each insight recommend? | `src/insights.py` |
| 28 | What is the source of the data? | `app.py` sidebar |
| 29 | Can I download filtered data? | `pages/sales.py` |
| 30 | Can I upload my own CSV? | `app.py` sidebar |

### Questions Not Included Yet

These are intentionally outside the current project scope:

- What will next month's sales be? — no forecasting module
- Which customers will churn? — no ML model
- What products should we recommend? — no recommender system
- What is the profit margin? — no cost data available
- What is customer lifetime value? — requires longer historical data
- What is the return rate? — no returns column in the source data
- How does shipping time affect sales? — no shipping-time data
- Which campaign drove the most sales? — no campaign data

### Coverage Summary

| Analytics Level | Coverage | Examples |
|---|---|---|
| Descriptive | ✅ 100% | Total sales, orders, top products, trends |
| Diagnostic | ✅ 60% | Outlier investigation, region weakness, correlation |
| Predictive | ❌ 0% | Not in scope for v1 |
| Prescriptive | ✅ 40% | Recommendations in `src/insights.py` |

### Visual Question Map

```text
Business Question                     → Solved In
────────────────────────────────────────────────────────────
Total sales?                          → app.py KPI
Orders count?                         → app.py KPI
Customers count?                      → app.py KPI
Average order value?                  → app.py KPI
Median order value?                   → app.py KPI
Units sold?                           → app.py KPI

Sales over time?                      → dashboard.py + sales.py
Monthly sales?                        → sales.py
Top categories?                       → dashboard.py + products.py
Top products?                         → products.py
Low-performing products?              → products.py

Top customers?                       → customers.py
Customer segments?                    → customers.py
Customer spending stats?              → customers.py

Regional performance?                 → dashboard.py + sales.py

Mean, median, mode?                   → statistics.py
Variance, std dev?                    → statistics.py
Q1, Q2, Q3, IQR?                      → statistics.py
Outliers (IQR method)?                → statistics.py
Correlation?                          → statistics.py
Covariance?                           → statistics.py

Data quality issues?                  → data_quality.py
Missing values?                       → data_quality.py
Duplicate orders?                     → data_quality.py

Business insights?                    → src/insights.py
Recommendations?                     → src/insights.py
Download results?                     → sales.py, customers.py, products.py, statistics.py
Upload CSV?                          → app.py sidebar
```

---

## 📌 Notes

- The app is designed for local use and does not require a database.
- It is intended for analytical exploration rather than production deployment.
- Outputs are recalculated from the active dataset and are not hard-coded.

---

## 🔎 Useful References

- Business requirements: `docs/business_requirements.md`
- KPI definitions: `docs/kpi_definitions.md`
- Data dictionary: `data/data_dictionary.md`
- Data quality report: `docs/data_quality_report.md`

---

## License

This project is for educational and business-analysis use within the workspace environment.

