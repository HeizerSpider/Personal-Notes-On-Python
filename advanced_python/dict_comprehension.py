def main():
    ctemps = [10, 32, 52, 130, 13]

    temp_dict = {t: t*7/2 for t in ctemps if t<100}
    print(temp_dict)

    team1 = {"Ali": 2, "Ah Beng": 4,"adi": 64}
    team2 = {"Bala": 5, "Benny": 34, "Badrul": 53}
    #merging teams
    new_team = {k:v for team in (team1,team2) for k,v in team.items()}
    print(new_team)

main()