from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re
import csv

# オプションを設定してHeadlessモードでChromeを起動
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモード（ブラウザを表示しない）
chrome_options.add_argument("--disable-gpu")  # GPUを無効にする
driver = webdriver.Chrome(options=chrome_options)

# ページを開く
url = "https://www.jma.go.jp/bosai/forecast/"
driver.get(url)

# 5秒待機してページが完全に読み込まれるのを待つ（必要に応じて調整）
time.sleep(5)

# 天気予報のテーブルを取得
weather_elements = driver.find_element(By.XPATH,"//*[@id='week-table-container']/div[1]/div/div/div[2]/table")

# 日付の取得
date_elements = driver.find_elements(By.XPATH,"//*[contains(@class,'forecast-date')]")
date_list =[]
for date_element in date_elements:
    if date_element.text == "":
        pass
    elif "\n" in date_element.text:
        patttern = r"(?<=\n).*"
        match = re.search(r'(?<=\n).*', date_element.text)
        date_list.append(match.group(0))
    else:
        date_list.append(date_element.text)

date_list = sorted(set(date_list))

date = 9

weather_probs = []
weather_prob = {}

# 天気予報を取得
prob_elements = weather_elements.find_elements(By.XPATH, "//*[@id='week-table-container']/div[1]/div/div/div[2]/table/tr[@class='contents-bold-top']")
for prob_element in prob_elements:
    prob_element.text.split()
    for count, prob_record in enumerate(prob_element.text.split()):
        if count % date == 0:
            region = prob_record
        elif count % date == 1:
            first = prob_record
        elif count % date == 2:
            second = prob_record
        elif count % date == 3:
            third = prob_record
        elif count % date == 4:
            fourth = prob_record
        elif count % date == 5:
            fifth = prob_record
        elif count % date == 6:
            sixth = prob_record
        elif count % date == 7:
            seventh = prob_record
        elif count % date == 8:
            eighth = prob_record
            weather_prob = [region, first, second, third, fourth, fifth, sixth, seventh, eighth,]
            weather_probs.append(weather_prob)

# ブラウザを閉じる
driver.quit()

# ヘッダーの作成
field_name = date_list.copy()
field_name.insert(0,"region")

# csv出力
with open('weather_forecast.csv', "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(field_name)
    writer.writerows(weather_probs)




