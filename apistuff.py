import csv

import helper


def write_player_to_csv(name, data):
    with open(name, "a", encoding="utf-8") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=",")
        csvWriter.writerows(data)

def do_pcgr(name, id):
    test = helper.get_pgcr(id)

    for item in test["Response"]["entries"]:
        out = helper.get_player_stats(item)
        print(len(out))
        print(out)
        temp = [out]
        write_player_to_csv(name, temp)

    with open(name, "a", encoding="utf-8") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=",")
        csvWriter.writerow(["END GROUP"])