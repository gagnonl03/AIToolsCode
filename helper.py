import requests
import json
import key

base_url = "https://www.bungie.net/Platform"
HEADERS = {"X-API-Key": f"{key.key}"}


def save_json(file_name, data):
    json_data = json.dumps(data, indent=4)
    with open(f"{file_name}.json", "w") as outfile:
        outfile.write(json_data)


def make_request(url):
    return requests.get(url, headers=HEADERS)


def get_pgcr(pgcr_id):
    temp_url = base_url + f"/Destiny2/Stats/PostGameCarnageReport/{pgcr_id}"
    return make_request(temp_url).json()


def get_player_playtime(id, type):
    temp_url = base_url + f"/Destiny2/{type}/Profile/{id}/?components=200"
    data = make_request(temp_url).json()
    save_json("check", data)
    minutes_played_total = 0
    for item in data["Response"]["characters"]["data"]:
        minutes_played_total += int(data["Response"]["characters"]["data"][item]["minutesPlayedTotal"])

    return minutes_played_total


def get_player_stats(data):
    player_data = data["player"]
    player_name = player_data["destinyUserInfo"]["displayName"]
    player_memberID = player_data["destinyUserInfo"]["membershipId"]
    player_memberType = player_data["destinyUserInfo"]["membershipType"]
    player_time_played = get_player_playtime(player_memberID, player_memberType)
    player_class = player_data["characterClass"]
    player_light = player_data["lightLevel"]
    player_kills = data["values"]["kills"]["basic"]["value"]
    player_deaths = data["values"]["deaths"]["basic"]["value"]
    player_kdr = data["values"]["killsDeathsRatio"]["basic"]["value"]
    player_kda = data["values"]["killsDeathsAssists"]["basic"]["value"]
    player_grenade = data["extended"]["values"]["weaponKillsGrenade"]["basic"]["value"]
    player_melee = data["extended"]["values"]["weaponKillsMelee"]["basic"]["value"]
    player_super = data["extended"]["values"]["weaponKillsSuper"]["basic"]["value"]
    return [player_name, player_time_played, player_class, player_light, player_kills, player_deaths,
            player_kdr, player_kda, player_grenade, player_melee, player_super]

