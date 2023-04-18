import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/matches.csv', low_memory=False)

df = df[df['match_name'].isin(['Arsenal vs Tottenham Hotspur', 'Tottenham Hotspur vs Arsenal'])]

filtered_df = df.loc[(df['season'] >= 1913 ) & (df['season'] <= 2021), ['home_team_name','away_team_name', 'home_team_score', 'away_team_score']]

filtered_df['winning_team'] = filtered_df.apply(lambda row: row['home_team_name'] if row['home_team_score'] > row['away_team_score'] else row['away_team_name'] if row['away_team_score'] > row['home_team_score'] else 'draw', axis=1)

win_counts = filtered_df['winning_team'].value_counts()

colors = ['r','black','gray']
win_counts.plot(kind='bar',color=colors, legend=None)
plt.title('The Kings of the North London Derby (1913-2021)')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.xticks(rotation=0)
plt.show()

print(win_counts)









