# NYCHA Water Consumption Analysis (2013–2025)

This project explores a public dataset of New York City Housing Authority (NYCHA) water bills from 2013 to 2025. Using Python and pandas, I cleaned the data, created a **daily consumption** metric, and compared trends across boroughs over time.

## Research question
How has the average daily water consumption per billing period changed across different boroughs between 2013 and 2025 in New York City?

## Methods
- Preliminary EDA: dataset shape, types, summary stats and histograms for consumption and charges
- Data cleaning:
  - Dropped negative current charges (rare) and missing values
  - Converted `Revenue Month` to datetime
  - Kept reasonable billing periods (days between 1 and 365)
- Feature engineering:
  - `consumptionPerDay = Consumption (HCF) / # days`
  - Removed top 5% of daily consumption values to reduce extreme outlier influence (industrial/commerical buildings metrics)
- Aggregation & visualization:
  - Grouped by `Borough` and `Revenue Month` to compute mean daily consumption
  - Plotted borough time series with year-labeled ticks (2013–2025)

## Key results
Queens and the Bronx show the highest mean daily usage, followed by Manhattan and Brooklyn, while Staten Island is much lower. Most boroughs show a gradual decline after ~2020, and the 2025 series ends mid-year.

## Repo structure
- `src/` – Python scripts
- `data/` – CSV datasets
- `figures/` – generated plots

## How to run
```bash
python src/analysis.py
