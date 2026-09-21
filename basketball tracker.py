
Total_points_scored = 0
Total_shots_attempted = 0
Total_shots_made = 0
Total_fouls_committed = 0
while True:
                action =  int(input("Choose an option: 2 pointer(1) - 3 pointer(2) - foul(3) - miss(4) - game ended(5):  "))
                if action == 5:
                    break
                elif action == 1:
                    Total_shots_made += 1
                    Total_points_scored += 2
                    Total_shots_attempted += 1
                    print("you have scored ", Total_points_scored, "points")
                elif action == 2:
                    Total_shots_made += 1
                    Total_points_scored += 3
                    Total_shots_attempted += 1
                    print("you have scored ", Total_points_scored, "points")
                elif action == 3:
                    Total_fouls_committed += 1
                    print("You have committed" , Total_fouls_committed, "fouls")
                elif action == 4:
                    Total_shots_attempted += 1
Goal_percentage = (Total_shots_made / Total_shots_attempted) * 100
print("you scored ", Goal_percentage, "percent of your shots")
print("you committed", Total_fouls_committed, "fouls")
print("You scored", Total_points_scored, "points")
