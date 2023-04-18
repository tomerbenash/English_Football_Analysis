import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

df = pd.read_csv('Standings.csv',low_memory=False)

filtered_df = df.loc[(df['division'] == 'Premier League' ) & (df['position'] == 1 ), ['season','team_name' ,'position', 'goal_difference']]

filtered_df = filtered_df.reset_index().sort_values(by='goal_difference', ascending=False).head(6)
filtered_df['team_season'] = filtered_df['team_name'] + ' (' + filtered_df['season'].astype(str) + ')'


colors = ['c','c','c','b','c','c']
filtered_df.plot.bar(x='team_season', y='goal_difference', rot=0, color=colors)
plt.xlabel('Team Name')
plt.ylabel('Goal Difference')
plt.title('Highest G/D in the PL when won the League')
plt.xticks(rotation=20)
plt.show()
print(filtered_df)