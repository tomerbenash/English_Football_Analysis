import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)

df = pd.read_csv('Standings.csv',low_memory=False)

filtered_df1 = df.loc[(df['division'] == 'Premier League' ) & (df['season'] >= 1995 ) & (df['season'] <= 2021) &
                     ((df['position'] == 18) | (df['position'] == 19) | (df['position'] == 20)),
                     ['season','team_name' ,'position']]

filtered_df2 = df.loc[(df['division'] == 'Premier League' ) & (df['season'] >= 1992 ) & (df['season'] <= 1993) &
                     ((df['position'] == 20) | (df['position'] == 21) | (df['position'] == 22)),
                     ['season','team_name' ,'position']]

filtered_df3 = df.loc[(df['division'] == 'Premier League' ) & (df['season'] == 1994 )  &
                     ((df['position'] == 19) | (df['position'] == 20) | (df['position'] == 21) | (df['position'] == 22)),
                     ['season','team_name' ,'position']]


relegation_counts1 = filtered_df1['team_name'].value_counts()
relegation_counts2 = filtered_df2['team_name'].value_counts()
relegation_counts3 = filtered_df3['team_name'].value_counts()

concatenated_df = pd.concat([filtered_df1, filtered_df2, filtered_df3])
relegation_counts = concatenated_df['team_name'].value_counts().head(5)

colors = ['y','navy','r','crimson','darkred']
relegation_counts.plot(kind='bar',color=colors ,legend=None)
plt.title('Top 5 most relegated Clubss in the PL')
plt.xlabel('Club')
plt.ylabel('Number of Relegations')
plt.xticks(rotation=10)
plt.show()

print(relegation_counts)














