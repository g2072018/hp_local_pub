import bs4
import re
import datetime
import csv

HTML_PATH = "../public_html/member_graduate.html"
CSV_PATH = "../doc/doc_obog/"
CSV_NAME = str(datetime.datetime.now().year) + "年度OBOG一覧表.csv"

# htmlをテキストで開いて、htmlへパースする
html_open = open(HTML_PATH, "r")
html_text = html_open.read()
soup = bs4.BeautifulSoup(html_text, "html.parser")

name_list = list()
reseach_list = list()

# divのclass名がmemb_textのものをスクレイピングしてくる
people = soup.find_all("div", {"class", "memb_text"})
# サイズ調整用を含んでしまうので、2回同じものを取得してしまうので、1/2を行う
length = len(people) // 2
for i in range(length):
    # 正規表現の処理を行っている
    profile = list(re.findall("：(.+)", people[i].get_text()))

    # 空になった場合、ループ処理を抜ける
    if not profile:
        break

    name, reseach = profile[0], profile[1]
    
    name_list.append(str(name))
    reseach_list.append(str(reseach))

# csv化する
# columnのヘッダーを作成
column = ["氏名", "研究内容"]
with open(CSV_PATH + CSV_NAME, "w") as f:
    writer = csv.writer(f)
    # ヘッダーを挿入
    writer.writerow(column)
    # １行ずつインサートしていく
    for i in range(length - 1):
        writer.writerow([name_list[i], reseach_list[i]])