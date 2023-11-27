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