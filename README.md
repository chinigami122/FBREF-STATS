# Description
This project is a football statistics data pipeline that collects match data, processes it, and visualizes key metrics. It uses Python for data processing and visualization and stores the collected data in a MySQL database using SQLAlchemy.

The dataset includes match results, goals, possession statistics, expected goals (xG), and other key performance indicators. The project provides interactive visualizations using Plotly Express to analyze the most successful teams based on various metrics.

# Features
- **Data Storage**: Stores football match statistics in a structured MySQL database.
- **Data Processing**: Cleans and aggregates match data using Pandas.
- **Visualization**:
  - Most goals scored by teams.
  - Teams with the highest average possession.
  - Teams with the most wins.
  - Teams with the most losses.
  - Teams with the highest expected goals (xG).
- **Database Integration**: Uses SQLAlchemy for efficient MySQL database management.
- **Interactive Charts**: Utilizes Plotly Express to generate engaging visualizations.

# Requirements
Ensure you have the following Python libraries installed:
```bash
pip install pandas cryptography sqlalchemy pymysql plotly
```

# Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/football-stats.git
   cd football-stats
   ```

2. **Create the MySQL database and table:**
   - Run the provided SQL script (`create_mysql_db.sql`) in your MySQL server.

3. **Run the data pipeline:**
   ```python
   import pandas as pd
   from sqlalchemy import create_engine

   # Load CSV file
   df = pd.read_csv("new_matches1.csv")
   df["date"] = pd.to_datetime(df["date"], errors='coerce')

   # Define MySQL connection
   DATABASE_URL = os.getenv("DATABASE_URL")
   engine = create_engine(DATABASE_URL)

   # Load data into MySQL
   df.to_sql("matches", con=engine, if_exists="replace", index=False)
   print("Data successfully loaded into MySQL.")
   ```

4. **Run the visualization script:**
   ```python
   import plotly.express as px

   # Load data from MySQL
   df = pd.read_sql("SELECT * FROM matches", con=engine)
   
   # Generate bar chart for most goals scored
   fig = px.bar(df, x="team", y="gf", title="Most Goals Scored by Teams", color="gf")
   fig.show()
   ```

# License
This project is licensed under the MIT License. See the `LICENSE` file for details.

Created by [Soufiane Bouziani]

