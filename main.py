# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
matches = pd.read_csv('WorldCupMatches.csv')
cups = pd.read_csv('WorldCups.csv')
players = pd.read_csv('WorldCupPlayers.csv')

# Clean column names by removing spaces
matches.columns = matches.columns.str.strip()
cups.columns = cups.columns.str.strip()
players.columns = players.columns.str.strip()

# Display the first few rows of each dataset
print(matches.head())
print(cups.head())
print(players.head())

# Data overview
print(matches.info())
print(cups.info())
print(players.info())

# Step 3: Data Filtering
# Example: Filter matches from the year 2014
matches_2014 = matches[matches['Year'] == 2014]
print(matches_2014.head())

# Step 4: Exploratory Data Analysis (EDA)

# WorldCupMatches EDA
# Distribution of goals
plt.figure(figsize=(10, 6))
sns.histplot(matches['Home Team Goals'], bins=20, kde=True, color='blue', label='Home Team Goals')
sns.histplot(matches['Away Team Goals'], bins=20, kde=True, color='red', label='Away Team Goals')
plt.title('Distribution of Goals')
plt.legend()
plt.xlabel('Goals')
plt.ylabel('Frequency')
plt.savefig('goals_distribution.png')
plt.show()

# Average goals per year
avg_goals_per_year = matches.groupby('Year')[['Home Team Goals', 'Away Team Goals']].mean()
avg_goals_per_year.plot(kind='bar', figsize=(12, 6), stacked=True)
plt.title('Average Goals per Year')
plt.xlabel('Year')
plt.ylabel('Average Goals')
plt.savefig('avg_goals_per_year.png')
plt.show()

# WorldCups EDA
# Total goals scored each World Cup
plt.figure(figsize=(12, 6))
sns.barplot(x='Year', y='GoalsScored', data=cups, palette='viridis')
plt.title('Total Goals Scored Each World Cup')
plt.xlabel('Year')
plt.ylabel('Total Goals')
plt.savefig('total_goals_per_cup.png')
plt.show()

# Attendance per World Cup
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Attendance', data=cups)
plt.title('Attendance Over the Years')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.savefig('attendance_over_years.png')
plt.show()

# WorldCupPlayers EDA
# Top 10 players with most appearances
top_players = players['Player Name'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_players.values, y=top_players.index, palette='rocket')
plt.title('Top 10 Players with Most Appearances')
plt.xlabel('Appearances')
plt.ylabel('Player Name')
plt.savefig('top_players_appearances.png')
plt.show()

# Step 5: Save the results into a PowerPoint report
from pptx import Presentation
from pptx.util import Inches

