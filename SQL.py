import pandas as pd
import sqlite3

df = pd.read_csv('data/matches.csv')
conn = sqlite3.connect('football.db')
df.to_sql('matches', conn, if_exists='replace', index=False)
cursor = conn.cursor()


#Query 1: Count the number of matches played in each season in each division
cursor.execute("SELECT season, division, COUNT(*) FROM matches GROUP BY season, division")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 2: Count the home games for each team in the premier league in 2021
cursor.execute("SELECT season, home_team_name, COUNT(*) AS num_matches "
               "FROM matches WHERE division = 'Premier League' AND season = 2021 GROUP BY season, home_team_name")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 3: AVG score per game for each team in the PL in 2019
cursor.execute("SELECT home_team_name, AVG(home_team_score + away_team_score) AS avg_score"
               " FROM matches WHERE division = 'Premier League' AND season = 2019 "
               "GROUP BY home_team_name ORDER BY avg_score DESC")
results = cursor.fetchall()
for row in results:
    print(row)

df = pd.read_csv('data/Seasons.csv')
conn = sqlite3.connect('football.db')
df.to_sql('Seasons', conn, if_exists='replace', index=False)

#Query 4: Who has the most titles in the Premier league
cursor.execute("SELECT winner, COUNT(*) AS num_wins "
               "FROM Seasons WHERE division = 'Premier League' GROUP BY winner ORDER BY num_wins DESC LIMIT 1")
result = cursor.fetchone()
print(result)

#Query 5: The numer of home goals for each team in the PL in 2020
cursor.execute("SELECT season, division, home_team_name, SUM(home_team_score)"
               " FROM matches WHERE season = 2020 AND division = 'Premier League' "
               "GROUP BY home_team_name, division ORDER BY SUM(home_team_score) DESC")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 6: For each season and division, the winner and how many away goals
cursor.execute("SELECT S.season, m.division, S.winner, SUM(m.away_team_score) FROM matches m, Seasons S "
               "WHERE m.away_team_name = S.winner AND m.season = S.season AND m.division = S.division "
               "GROUP BY S.season, S.winner")
results = cursor.fetchall()
for row in results:
    print(row)

df = pd.read_csv('data/Standings.csv')
conn = sqlite3.connect('football.db')
df.to_sql('Standings', conn, if_exists='replace', index=False)

#Query 7: Average goal per match in each season in each division
cursor.execute("SELECT S.season, S.division, AVG(m.home_team_score + m.away_team_score) "
               "FROM matches m, Seasons s WHERE S.season = m.season AND S.division = m.division "
               "GROUP BY S.season, S.division")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 8: Number of PL titles for each team that has won it
cursor.execute("SELECT winner, COUNT(*) FROM Seasons "
               "WHERE division = 'Premier League' "
               "GROUP BY winner ORDER BY COUNT(*) DESC")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 9: Number of Goals for and Goals against for each Winner
cursor.execute("SELECT S.season, S.division, S.winner, st.goals_for, st.goals_against "
               "FROM Seasons S, Standings st "
               "WHERE S.season = st.season AND S.division = st.division AND S.winner = st.team_name "
               "GROUP BY S.season ")
results = cursor.fetchall()
for row in results:
    print(row)

#Query 10: Teams that have won titles conescutive times
cursor.execute("SELECT s1.season, s2.season, s1.winner FROM Seasons s1, Seasons s2 "
               "WHERE s1.winner = s2.winner AND s1.season = s2.season -1 AND s1.division = s2.division "
               "GROUP BY s1.season ")
results = cursor.fetchall()
for row in results:
    print(row)
