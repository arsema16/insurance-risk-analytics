# Insurance Risk Analytics

[![CI](https://github.com/arsema16/insurance-risk-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/arsema16/insurance-risk-analytics/actions/workflows/ci.yml)

## 📊 Project Overview

This project is part of the **10 Academy Artificial Intelligence Mastery** program (Week 3 Challenge). The goal is to analyze 18 months of historical insurance claim data for AlphaCare Insurance Solutions (ACIS) in South Africa, uncover low-risk segments, and build predictive models for risk-based pricing.

### Business Problem
ACIS needs to move from intuition-based pricing to **analytics-driven decisions** to optimize marketing investments and refine pricing models in the competitive South African auto-insurance market.

### Key Objectives
- 📈 Analyze claim patterns and risk drivers
- 🔬 Statistically validate risk hypotheses
- 🤖 Build predictive models for claim severity and probability
- 💰 Develop a risk-based pricing framework

---

## 📁 Project Structure
insurance-risk-analytics/
├── .github/workflows/ # CI/CD pipeline (GitHub Actions)
├── data/ # Versioned with DVC (not in Git)
│ ├── insurance_data.csv # Raw data (v1)
│ └── insurance_data_clean.csv # Cleaned data (v2)
├── notebooks/ # Jupyter notebooks
│ ├── 01_eda.ipynb # Exploratory Data Analysis
│ ├── 02_hypothesis_testing.ipynb # Statistical tests
│ └── 03_modeling.ipynb # Predictive models
├── src/ # Reusable Python modules
│ ├── data_loader.py
│ ├── eda_utils.py
│ ├── hypothesis_tests.py
│ └── modeling.py
├── reports/ # Documentation
│ ├── interim_report.md
│ └── final_report.md
├── tests/ # Unit tests
├── .dvc/ # DVC configuration
├── requirements.txt # Python dependencies
└── README.md # This file

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git
- DVC (Data Version Control)

### Installation

```bash
# Clone the repository
git clone https://github.com/arsema16/insurance-risk-analytics.git
cd insurance-risk-analytics

# Install dependencies
pip install -r requirements.txt

# Pull versioned data from DVC remote
dvc pull
```
## 🔄 Data Version Control (DVC)

This project uses DVC to version large data files. Two versions are tracked:

| Version | File | Description | Size |
|---------|------|-------------|------|
| v1 | `insurance_data.csv` | Raw original data | ~2MB |
| v2 | `insurance_data_clean.csv` | Cleaned (outliers removed, derived columns added) | ~2MB |

### Switch between versions:
```bash
# Check DVC status
dvc status

# List all versions
git log --oneline data/insurance_data.csv.dvc

# Checkout a specific version
git checkout <commit-hash> data/insurance_data.csv.dvc
dvc checkout
```
DVC Commands Used
```bash
# Initialize DVC
dvc init

# Add remote storage
dvc remote add -d localstorage C:\dvc_storage

# Track data files
dvc add data/insurance_data.csv
dvc add data/insurance_data_clean.csv

# Push to remote
dvc push

# Pull data (for reproducibility)
dvc pull
```
🧪 Running Tests
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v
```
## 📈 CI/CD Pipeline

GitHub Actions automatically runs:

- Code formatting check (Black)
- Unit tests (pytest)
- On every push and pull request

---

## 📚 Technologies Used

- **Python 3.10** - Core language
- **Pandas/NumPy** - Data manipulation
- **Matplotlib/Seaborn** - Visualization
- **Scikit-learn** - Machine learning
- **XGBoost** - Gradient boosting
- **SHAP** - Model interpretability
- **DVC** - Data version control
- **GitHub Actions** - CI/CD

---

## 📅 Timeline

| Task | Status | Due Date |
|------|--------|----------|
| Task 1: Git & EDA | ✅ Complete | - |
| Task 2: DVC | ✅ Complete | - |
| Task 3: Hypothesis Testing | 🔄 In Progress | - |
| Task 4: Modeling | ⏳ Pending | - |
| Interim Submission | ✅ Submitted | 25 May 2026 |
| Final Submission | ⏳ Pending | 27 May 2026 |

---

## 👥 Team

- **Arsema** - Data Analytics Engineer

### Tutors
- Kerod
- Mahbubah
- Feven

---

## 📄 License

This project is part of the 10 Academy AI Mastery program.

---

## 🙏 Acknowledgments

- 10 Academy for the learning resources
- AlphaCare Insurance Solutions for the business context

---

## 📞 Contact

- **GitHub**: [arsema16](https://github.com/arsema16)
- **Repository**: [insurance-risk-analytics](https://github.com/arsema16/insurance-risk-analytics)

---
