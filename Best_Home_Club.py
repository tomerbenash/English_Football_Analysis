import pandas as pd
import matplotlib.pyplot as plt

# FOR THE LAST 3 YEARS, TOP 4 HOME TEAMS, AND HOW MANY EACH SEASON?

df = pd.read_csv('matches.csv', low_memory=False)

df = df[(df['division'] == 'Premier League') & (df['season'].isin([2019, 2020, 2021]))]

filtered_df = df[['season', 'home_team_name', 'home_team_score']]


top_4_by_season = (filtered_df.groupby(['season', 'home_team_name'])['home_team_score'].sum()
                   .groupby(level='season').nlargest(3))

# sums all home goals for each team each per season
pivot_df = filtered_df.pivot_table(index='season', columns='home_team_name', values='home_team_score', aggfunc='sum')

# filters to only top 4
pivot_df = pivot_df.loc[:, pivot_df.columns.isin(top_4_by_season.index.get_level_values('home_team_name').unique())]


# create a bar plot with 4 bars for each season and each home team
ax = pivot_df.plot(kind='bar', width=0.8, colormap='Set2')

# set the title and axis labels
ax.set_title('Total Home Goals For Each Team', fontsize=12)
ax.set_xlabel('Season', fontsize=12)
ax.set_ylabel('Total Goals', fontsize=12)

# rotate the x-axis labels
ax.tick_params(axis='x', rotation=0)

# add a grid
ax.grid(True)

# show the legend
ax.legend(ncol=3, fontsize=10)

# show the plot
plt.show()
