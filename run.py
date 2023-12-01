import csv

import pandas as pd
import apistuff

# RUN INSTRUCTIONS::

# Change this to the name you want to save all the data to (im already running crota)
output_name = "crotasplayers.csv"

# Rename this to the name file you want to read pcgrs from
df = pd.read_csv("crotasend.csv", header=None)
df.columns = ["pcgr", "time"]

with open(output_name, "a", encoding="utf-8") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=",")
    csvWriter.writerow(
        ["Name", "Time Played", "Class", "Light", "Kills", "Deaths", "KDR", "KDA", "Grenade", "Melee", "Super",
         "Completed"])

df["pcgr"] = df["pcgr"].apply(lambda thing: thing[6:])

df["pcgr"].apply(lambda item: apistuff.do_pcgr(output_name, item))
