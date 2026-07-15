import numpy as np
import pandas as pd
from decorators import logger

class IplAnalyzer:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        print("Dataset Loaded Successfully!")

    def menu1(self):
        while True:
            print("\n" + "=" * 50)
            print("          IPL MATCH ANALYZER")
            print("=" * 50)
            print("1. Dataset Information")
            print("2. Team Analysis")
            print("3. Season Analysis")
            print("4. Venue Analysis")
            print("5. Player Analysis")
            print("6. Head-to-Head Analysis")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.dataset_info()

            elif choice == 2:
                self.team_analysis()

            elif choice == 3:
                self.season_analysis()

            elif choice == 4:
                self.venue_analysis()

            elif choice == 5:
                self.player_analysis()

            elif choice == 6:
                self.head_head()

            elif choice == 7:
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

    def dataset_info(self):
        print("\n" + "=" * 50)
        print("DATASET INFORMATION")
        print("=" * 50)

        print("\n1. First 5 Records")
        print(self.df.head())

        print("\n2. Last 5 Records")
        print(self.df.tail())

        print("\n3. Rows:", self.df.shape[0])
        print("4. Columns:", self.df.shape[1])

        print("\n5. Column Names")
        print(self.df.columns)

        print("\n6. Missing Values")
        print(self.df.isnull().sum())

        print("\n7. Dataset Description")
        print(self.df.describe())

        print("\n8. Dataset Information")
        self.df.info()

    @logger
    def team_analysis(self):
        match_won=self.df['winner'].value_counts()
        Total_match=pd.concat([self.df['team1'],self.df['team2']]).value_counts()

        while True:
            print("\n" + "=" * 50)
            print("            TEAM ANALYSIS")
            print("=" * 50)
            print("1. Total Number of Teams")
            print("2. List of All Teams")
            print("3. Matches Played by Each Team")
            print("4. Matches Won by Each Team")
            print("5. Winning Percentage")
            print("6. Most Successful Team")
            print("7. Back to Main Menu")
            print("8.TO END ANALYSIS")
            
            choice1 = int(input("\nEnter your choice: "))
            
            if choice1 == 1:
                print("\n" + "=" * 20)
                print("Total team")
                print("=" * 20)
                total_teams =pd.concat([self.df['team1'], self.df['team2']]).unique()
                print("\nTotal Number of Teams:", len(total_teams))

                df_2026 = self.df[self.df['season'] == '2026']
                teams_now = pd.concat([df_2026['team1'], df_2026['team2']]).unique()
                print("\nTotal Teams in 2026:", len(teams_now))


            elif choice1 == 2:
                print("\n" + "=" * 20)
                print("Teams names")
                print("=" * 20)
                print("List of teams played till:")
                print(total_teams)
                print("\n List of teams playing in 2026:")
                print(teams_now)

            elif choice1 == 3:
                print("\n" + "=" * 20)
                print("Match Played")
                print("=" * 20)
                print("Match Played by Each team till now:",Total_match)

                self.df['match']=self.df['team1'] + 'vs' + self.df['team2']

            elif choice1==4:
                print("\n" + "=" * 50)
                print("            Match won")
                print("=" * 50)
                print("Match Won by each team:",match_won)

            elif choice1==5:
                print("\n" + "=" * 50)
                print("            Team Statistics")
                print("=" * 50)
                team_stats=pd.DataFrame({
                    "Match_played":Total_match,
                    "Match_won":match_won
                }).fillna(0)
                team_stats["win_Percentage"] = ((team_stats['Match_won'] / team_stats['Match_played']) * 100).round(2)
                print("\nTeam Statistics:")
                print(team_stats.sort_values(by='win_Percentage', ascending=False))

            elif choice1==6:
                teams=self.df['winner'].value_counts()
                print("Top 5 Teams:",teams.sort_values(ascending=False).head(5))
                

            elif choice1==7:
                self.menu1()
            elif choice1==8:
                break
    @logger     
    def player_analysis(self):
        players=pd.concat([self.df['team1_players'],self.df['team2_players']])
        players=players.str.split(",")   #split string into list
        players=players.explode()
        players=players.str.strip()

        players_match=players.value_counts()

        while True:
            print("\n" + "=" * 50)
            print("           PLAYER ANALYSIS")
            print("=" * 50)
            print("1. Total Players")
            print("2. Player Names")
            print("3. Top 10 Most Matches Played")
            print("4. Search Player")
            print("5. Exit")
            print("6.TO END ANALYSIS")
            
            
            choice2 = int(input("\nEnter your choice: "))

            if choice2==1:
                print("\n" + "=" * 20)
                print("Total Players")
                print("=" * 20)
                
                print("Total players:",len(players_match))

            elif choice2==2:
                print("\n" + "=" * 20)
                print("Players Names")
                print("=" * 20)

                for player_names in players_match.index:
                    print(player_names)

                
            
            elif choice2==3:
                print("\n" + "=" * 20)
                print("Most Match")
                print("=" * 20)

                most_match=players_match.head(10)
                print("Player with most match",most_match)
                
            elif choice2==4:
                print("\n" + "=" * 20)
                print("Search Player")
                print("=" * 20)

                name=input("Enter player name:")

                if name in players_match:
                    print("Player name:",name)
                    print("Match Played:",players_match[name])
                else:
                    print("player not found")

                
                
            elif choice2==5:
                self.menu1()
            elif choice2==6:
                break
            
      
        
    @logger
    def venue_analysis(self):

        venue=self.df.groupby('venue')
        total_match_played=venue.size()

        while True:
            print("\n" + "="*50)
            print("           VENUE ANALYSIS")
            print("="*50)
            
            print("1. Total Number of Venues")
            print("2. List of All Venues")
            print("3. Matches Played at Each Venue")
            print("4. Most Popular Venue")
            print("5. Matches Played in a Particular Venue")
            print("6. Winning Teams at a Particular Venue")
            print("7. Back to Main Menu")
            print("8.To end")
            
            choice4 = int(input("\nEnter your choice: "))
            
            if choice4 == 1:
                print("\n" + "=" * 20)
                print("Total Venue")
                print("=" * 20)

                print("Total venues:",len(venue))



                
            elif choice4 == 2:
                print("\n" + "=" * 20)
                print("List of venue")
                print("=" * 20)

                for venues,data in venue:
                    print(venues)

            elif choice4 == 3:
                print("\n" + "=" * 20)
                print("Total match played at each venue:")
                print("=" * 20)

                
                print("Total match played at each venue:")
                print(total_match_played)

            
            elif choice4 == 4:
                print("\n" + "=" * 20)
                print("Most popular venues:")
                print("=" * 20)
                
                popular=total_match_played.sort_values(ascending=False).head(5)

                print("Top 5 most popular venues:")
                print(popular)

            elif choice4 == 5:
                print("\n" + "=" * 20)
                print(" Matches Played in a Particular Venue")
                print("=" * 20)

                venue_name=input('Enter venue name:')

                venue_stats=self.df[self.df['venue']==venue_name]

                print("Matches played in",venue_name)
                print(len(venue_stats))

               

                
            elif choice4 == 6:
                print("\n" + "=" * 20)
                print(" Winning team in a Particular Venue")
                print("=" * 20)

                venue_name=input('Enter venue name:')

                venue_stats=self.df[self.df['venue']==venue_name]

                print("Winners in",venue_name)
                print(venue_stats['winner'].value_counts())

            elif choice4 == 7:
                self.menu1()
            elif choice4==8:
                break

    @logger        
    def season_analysis(self):

        seasons=self.df.groupby('season')

        while True:
            print("\n" + "=" * 50)
            print("          SEASON ANALYSIS")
            print("=" * 50)
            
            print("1. Total Number of Seasons")
            print("2. List of All Seasons")
            print("3. Matches Played in Each Season")
            print("4. Season with Maximum Matches")
            print("5. Season with Minimum Matches")
            print("6. Winner of Each Season")
            print("7. Back to Main Menu")
            print("8. To End")

            choice3=int(input("Enter your choice:"))

            if choice3==1:
                print("\n" + "=" * 20)
                print("No of Seasons")
                print("=" * 20)

                print("Total no of Season:",len(seasons))

            elif choice3==2:
                print("\n" + "=" * 20)
                print("List of season")
                print("=" * 20)

                print("List of seasons:")

                for groups,data in seasons:
                    print(groups)
            
            elif choice3==3:
                print("\n" + "=" * 20)
                print("Match played in Season")
                print("=" * 20)
                matches=self.df['season'].value_counts().sort_index()
                print("\n Match played in each Sesaon:",matches)
                
            elif choice3==4:
                print("\n" + "=" * 20)
                print("Maximum Match played in Season")
                print("=" * 20)
                matches=self.df['season'].value_counts().sort_values(ascending=False).head(1)
                print("\n Match played in each Sesaon:",matches)
                
                
            elif choice3==5:
                print("\n" + "=" * 20)
                print("Minimum Match played in Season")
                print("=" * 20)
                matches=self.df['season'].value_counts().sort_values(ascending=True).head(1)
                print("\n Match played in each Sesaon:",matches)
                
            elif choice3==6:
               winners= seasons['winner'].last()
               print("Winner of Each seasons:")
               for season,winner in winners.items():
                   print(f"{season} : {winner}")


            elif choice3==7:
                self.menu1()
            elif choice3==8:
                break



        
        
        
    @logger
    def head_head(self):
        while True:
            print("\n" + "=" * 50)
            print("         HEAD TO HEAD ANALYSIS")
            print("=" * 50)

            print("1. Compare Two Teams")
            print("2. Back to Main Menu")
            print("3. TO END")

            choice5 = int(input("\nEnter your choice: "))

            if choice5 == 1:

                print("\n" + "=" * 20)
                print("Compare Two Teams")
                print("=" * 20)

                team1 = input("Enter Team 1: ")
                team2 = input("Enter Team 2: ")

                head_to_head = self.df[
                    ((self.df["team1"] == team1) & (self.df["team2"] == team2)) |
                    ((self.df["team1"] == team2) & (self.df["team2"] == team1))
                ]

                print("\nTotal Matches Played :", len(head_to_head))

                winners = head_to_head["winner"].value_counts()

                print("\nMatches Won")

                print(team1, ":", winners.get(team1, 0))
                print(team2, ":", winners.get(team2, 0))

                no_result = len(head_to_head) - (
                    winners.get(team1, 0) + winners.get(team2, 0)
                )

                print("No Result :", no_result)

                if len(head_to_head) > 0:

                    team1_percentage = (winners.get(team1, 0) / len(head_to_head)) * 100
                    team2_percentage = (winners.get(team2, 0) / len(head_to_head)) * 100

                    print("\nWinning Percentage")
                    print(team1, ":", round(team1_percentage, 2), "%")
                    print(team2, ":", round(team2_percentage, 2), "%")

                else:
                    print("\nNo matches found between these teams.")

            elif choice5 == 2:
                self.menu1()

            elif choice5 == 3:
                break