import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

df = pd.read_csv('data/matches.csv', low_memory=False)

mc_matches = df.loc[(df['home_team_name'] == 'Manchester City' ) | (df['away_team_name'] == 'Manchester City'), ['home_team_name','away_team_name', 'home_team_score', 'away_team_score']]

def get_mc_goal_count(row):
    if row['home_team_name'] == 'Manchester City':
        return row['home_team_score']
    else:
        return row['away_team_score']

mc_matches['mc_goals'] = mc_matches.apply(get_mc_goal_count, axis=1)

opponent_goals = mc_matches.groupby(['home_team_name', 'away_team_name']).agg({'mc_goals': 'sum'})

opponent_goals = opponent_goals.reset_index().sort_values('mc_goals', ascending=False).head(3)

opponent_goals.plot.bar(x='away_team_name', y='mc_goals', rot=0)
plt.xlabel('Opposing Team')
plt.ylabel('Goals Scored by Manchester City')
plt.title('Manchester City\'s Top 3 Opponents by Goals Scored')
plt.xticks(rotation=0)

plt.show()

print(opponent_goals)