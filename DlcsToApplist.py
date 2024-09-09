import json

with open('games.json', 'r') as games_file:
    games_data = json.load(games_file)

with open('applist.json', 'r') as applist_file:
    applist_data = json.load(applist_file)

new_dlc_count = 0

for game_id, game_info in games_data.items():
    if 'dlc' in game_info:
        for dlc_id in game_info['dlc']:
            dlc_id_str = str(dlc_id)
            if dlc_id_str not in applist_data:
                applist_data.append(dlc_id_str)
                new_dlc_count += 1

with open('applist.json', 'w') as applist_file:
    json.dump(applist_data, applist_file, indent=4)

print(f"DLC IDs have been added to applist.json. Total new DLCs added: {new_dlc_count}.")
