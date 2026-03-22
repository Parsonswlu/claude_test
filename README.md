# EDA & Analytics Repo

A collection of exploratory data analyses, visualizations, and predictive analytics using SQL and Python.

## Structure

```
├── eda/                # Exploratory data analysis notebooks and scripts
├── sql/                # SQL queries and analyses
├── visualizations/     # Visualization scripts and notebooks
├── predictive/         # Predictive analytics and ML models
└── utils/              # Shared utilities and helper functions
```

## Setup

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Conventions

- **EDA**: Jupyter notebooks prefixed with a number indicate sequence (e.g., `01_initial_exploration.ipynb`)
- **SQL**: Queries organized by subject area in subdirectories under `sql/`
- **Visualizations**: Standalone scripts or notebooks producing charts/dashboards
- **Predictive**: Model training, evaluation, and inference scripts

## License

MIT
