import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)

df = pd.read_csv('data/Standings.csv', low_memory=False)

#G/F G/A G/D for every club
team_goals = df.groupby(["team_name"]).agg({"goals_for": "sum", "goals_against": "sum"})
team_goals["goal_difference"] = team_goals["goals_for"] - team_goals["goals_against"]
team_goals.sort_values(by="goal_difference", ascending=False, inplace=True)
#print(team_goals)


top_10_teams = df.groupby(["team_name"]).agg({"points": "sum"}).nlargest(10, "points")
top_10_teams.plot(kind="bar", title="Top 10 Teams by Points")
plt.xticks(rotation=20)
#print(top_10_teams)
#plt.show()

df = pd.read_csv('data/Standings.csv', low_memory=False)
filtered_df = df.loc[(df['division'] == 'Premier League' ) & (df['season'] == 2020 ),['team_name','wins','played']]



win_perc = filtered_df.groupby(["team_name"]).agg({"wins": "sum", "played": "sum"})
win_perc["win_percentage"] = (win_perc["wins"] / win_perc["played"]) * 100

print(win_perc)

sns.set(font_scale=1.2)
sns.set_style({"axes.facecolor": ".95"})

plt.figure(figsize=(10, 8))
sns.heatmap(win_perc[['win_percentage']], annot=True, cmap="coolwarm", linewidths=.5, vmin=0, vmax=100)
plt.title("Premier League 2020 Wins Ratio")
plt.show()
