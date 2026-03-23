# Project Instructions

## Notebooks & Explorations

When creating any exploratory notebook (Jupyter or otherwise), always include self-contained setup cells at the top that handle:

1. **Dependencies** — `!pip install <package> -q` for any required packages
2. **Data requirements** — a conditional check that detects whether the required data is present, and automatically runs the appropriate download script if it is not

The goal is that a user can open a notebook and run top-to-bottom without needing any separate terminal commands.
