import time
import csv
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def write_to_file(path, data):
    with open(path.split("/")[0] + ".csv", "a") as my_csv:
        csvWriter = csv.writer(my_csv)
        csvWriter.writerows(data)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("uBlock Origin 1.53.0.0.crx")
#chrome_options.add_argument('--blink-settings=imagesEnabled=false')
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless=new")

browser = webdriver.Chrome(options=chrome_options)

base_url = "https://raid.report/leaderboard/worldsfirst/"
raids = list()
raids.append(["crotasend/normal", 146])
raids.append(["rootofnightmares/normal", 909])
raids.append(["kingsfall/normal", 173])
raids.append(["vowofthedisciple/normal", 136])
raids.append(["vaultofglass/normal", 134])
raids.append(["deepstonecrypt/normal", 106])
print(raids[0][0].split("/")[0])


browser.get(base_url + raids[0][0])

soup = BeautifulSoup(browser.page_source, "html.parser")
output = list()
time.sleep(2)
temp = soup.find_all("a")
for item in temp:
    if item["href"][1:5] == "pgcr":
        print(item["href"])
        time_taken = item.find_next("span", class_="hide-on-med-and-up time-value-cell").text
        output.append([item["href"], time_taken])
print(output)
write_to_file(raids[0][0], output)



for raid in raids:
    pcgrs = list()
    temp_page_val = 0
    while temp_page_val <= raid[1]:
        browser.get(base_url + raid[0] + f"?page={temp_page_val}")
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        temp = soup.find_all("a")
        print(f"{temp_page_val} had {len(temp)} items")
        output = list()
        for item in temp:
            if item["href"][1:5] == "pgcr":
                time_taken = item.find_next("span", class_="hide-on-med-and-up time-value-cell").text
                output.append([item["href"], time_taken])
        write_to_file(raid[0], output)
        temp_page_val += 1



