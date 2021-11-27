# Demographic_Migration_Analysis
Basic analysis of migration patterns as well as their related demographic characteristics. The demographics of focus will be: education, race, sex, population by age, poverty levels, and housing types.

# Data
- [American Community Survey (in-depth demographic and migration data)](https://data.census.gov/cedsci/table?t=International%20and%20Domestic%20Migration%3APopulation%20Change%20and%20Components&g=0100000US%240400000&tid=ACSST1Y2019.S0701)

## In-depth demographics
- Population
  - 1-18 years old
  - 19-24 years old
  - 25-54 years old
  - 55 years old and above
- Sex
- Race
  - White
  - Black
  - Asian
  - Hispanic
  - Other
- Educational attainment
  - High school and below
  - Some college and associates degree
  - Bachelors degree and above
- Individual income
  - 1-35k
  - 35k-50k
  - 50k-75k
  - 75k+
- Poverty level
  - Below 150%
  - Above 150%
- Housing Tenure
  - Owner occupied
  - Renter occupied

## File Structure
```
.
├── README.md
├── data
│   └── migration_data
│       ├── ACSST1Y[2010-2019].S0701_data_with_overlays_2021[...].csv
│       ├── ACSST1Y[2010-2019].S0701_table_title_2021[...].csv
│       ├── ACSST1Y[2010-2019].S0701_table_title_2021[...].csv
│       └── README.md
├── src
│   ├── MigrationData.py
│   ├── data_analysis.py
│   ├── __init__.py
│   ├── age_and_sex_plots.py
│   ├── population_plots.
│   ├── Poverty_gif_plots.py
│   └── README.md
├── Visualization_and_plots
│   └── [...]
├──.gitignore
└── env.yaml
```

## Data Processing File Structure
1. Create functions to process each demographic
    1. clubbing (combining) some data
    2. removing irrelevant data
    3. make the state as rows
    4. demographics as columns
2. Create functions to get fastest and slowest growing states

~~More to be added--this is just the basic data engineering that needs to be done. Possible future functions to be added:~~
~~- top/bottom 10 states~~
~~- sorting~~
~~- averaging~~ 

It has been decided that at the moment the data engineering file is more than sufficient for the task of data analysis.
