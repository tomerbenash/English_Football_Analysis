import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Standings.csv')

df = df[df['division'] == 'Premier League']

filtered_df = df.loc[(df['season'] >= 1992 ) & (df['season'] <= 2021), ['team_name', 'goals_against']]
top_5 = filtered_df.groupby('team_name')['goals_against'].mean().sort_values().head(5).reset_index()


top_5.plot(kind='bar', x='team_name', y='goals_against', legend=None)
colors = ['r', 'b', 'firebrick', 'lightcoral','c']
ax = top_5.plot(kind='bar', x='team_name', y='goals_against', color=colors, legend=None)
plt.xticks(rotation=0)

plt.title('Best defence in the PL history (1992-2021)')
plt.xlabel('Club Name')
plt.ylabel('Goals Against in average every season')

plt.show()

print(top_5)

