import csv

import helper


def write_player_to_csv(data):
    with open("out.csv", "a") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=",")
        csvWriter.writerows(data)


test = helper.get_pgcr("7305790649")
helper.save_json("alec", test)
with open("out.csv", "a") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=",")
    csvWriter.writerow(["Name", "Time Played", "Class", "Light", "Kills", "Deaths"])

for item in test["Response"]["entries"]:
    out = helper.get_player_stats(item)
    print(len(out))
    print(out)
    temp = [out]
    write_player_to_csv(temp)

with open("out.csv", "a") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=",")
    csvWriter.writerow(["END GROUP"])