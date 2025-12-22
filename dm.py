from constants import PLAYERS
import copy
import random
import sys


def combine_(PLAYERS):
    players_copy = copy.deepcopy(PLAYERS)
    random.shuffle(players_copy)
    new_datas = []
    for player in players_copy:
        new_player = {"experience": False, "height": False}
        if "name" in player:
            new_player["name"] = player["name"]
        if "experience" in player:
            new_player["experience"] = player["experience"].upper() == "YES"
        if "height" in player:
            try:
                new_player["height"] = int(player["height"].split(" ")[0])
            except ValueError:
                new_player["height"] = False
        new_datas.append(new_player)

    divide_players_per_team = len(players_copy) // 3
    panthers = new_datas[:divide_players_per_team]
    bandits = new_datas[divide_players_per_team:divide_players_per_team * 2]
    warriors = new_datas[divide_players_per_team * 2:]

    print("1) PANTHERS TEAM:")
    team_stats(panthers)
    print("\n2) BANDITS TEAM:")
    team_stats(bandits)
    print("\n3) WARRIORS TEAM:")
    team_stats(warriors)

    return {"panthers": panthers, "bandits": bandits, "warriors": warriors}




def team_stats(team):
    total_players = len(team)
    experienced = len([player for player in team if player.get("experience", False) is True])
    inexperienced = total_players - experienced

    print(f"Total players: {total_players}")
    print(f"Experienced players: {experienced}")
    print(f"Inexperienced players: {inexperienced}\n")

    print("Selected players:")
    list_var_heights = []
    list_var_names = []

    for player in team:
        if "name" in player and isinstance(player["name"], str):
            list_var_names.append(player["name"])

        if "height" in player and isinstance(player["height"], int) and player["height"]:
            list_var_heights.append(player["height"])

    convert_to_string = ", ".join(list_var_names)
    print(convert_to_string)

    if list_var_heights:
        av = sum(list_var_heights) / len(list_var_heights)
        print(f"Team average height: {av}")
    else:
        print("No valid player heights to compute average.")


def greeting():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---------------MENU------------\n")
    print(
        "Here are your choices:\n",
        "1) Display Team Stats\n",
        "2) Quit \n"
    )
    try:
        variable = int(input("Enter an option > "))
    except ValueError:
        print("Invalid input")
        sys.exit()

    if variable == 1:
        combine_(PLAYERS)
    elif variable == 2:
        sys.exit()
    else:
        sys.exit()


def main():
    greeting()
