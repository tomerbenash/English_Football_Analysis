import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Standings.csv')

df = df[df['division'] == 'Premier League']

filtered_df = df.loc[(df['season'] >= 1992 ) & (df['season'] <= 2021), ['position', 'team_name', 'wins', 'goal_difference','points']]


top_5 = filtered_df.groupby(['team_name']).mean().sort_values("position").head(5)
top_5_position = filtered_df.groupby('team_name')['position'].mean().sort_values().head(5).reset_index()


top_5_position.plot(kind='bar', x='team_name', y='position', legend=None)
colors = ['r', 'lightcoral', 'firebrick', 'b','c']
ax = top_5_position.plot(kind='bar', x='team_name', y='position', color=colors, legend=None)
plt.xticks(rotation=0)

plt.title('Top 5 clubs in the PL history (1992-2021)')
plt.xlabel('Club Name')
plt.ylabel('Club Position in the end of the season')


plt.show()

print(top_5_position)






