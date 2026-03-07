from constants import PLAYERS
import copy
import pdb
import random
import shutil
import sys
import time

def clean_data_function_(PLAYERS):
    player_per_copy = copy.deepcopy(PLAYERS)
    #pdb.set_trace()
    try:
        # returns None
        random.shuffle(player_per_copy) # return None
    except: # except never runs
        print('error') # never prints

    append_it_to_the_new_list = []
    for player in player_per_copy:
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
        append_it_to_the_new_list.append(new_player)

    total_number_of_players = len(player_per_copy) // 3
    panthers = append_it_to_the_new_list[:total_number_of_players] # ?
    bandits = append_it_to_the_new_list[total_number_of_players:total_number_of_players * 2]
    warriors = append_it_to_the_new_list[total_number_of_players * 2:]

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
    columns = shutil.get_terminal_size().columns
    VAR = 'BASKETBALL TEAM STATS TOOL'
    print(f"\n{VAR.center(columns)}")
    second_var = "---------------MENU------------\n"
    print()
    print(second_var.center(columns))
    print()
    print(
        "Select an option:\n",
        "1) Press 1 to Display Team Stats\n",
        "2) Press 2 to Quit \n"
    )
    try:
        variable = int(input("Enter an option > "))
    except ValueError:
        print("Invalid input")
        sys.exit()

    if variable == 1:
        clean_data_function_(PLAYERS)
        time.sleep(1)
        print('\nPress Enter to continue...')
        input()
        greeting()
        
    elif variable == 2:
        sys.exit()
    else:
        sys.exit()


def main():
    greeting()
