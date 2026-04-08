import json

def load_logs():
    try:
        with open("logs.json", "r", encoding="utf-8") as infile:
            logs = json.load(infile)
            return logs
    except FileNotFoundError:
        return []

def save_logs(logs):
    with open("logs.json", "w", encoding="utf-8") as outfile:
        json.dump(logs, outfile)

def make_log(bean_name, water_g, dose_g, overall_score):
    return {
        "bean_name": bean_name,
        "water_g": int(water_g),
        "dose_g": int(dose_g),
        "overall_score": int(overall_score),
    }

def list_logs(logs):
    for index, log in enumerate(logs):
        print(str(index) + "件目")
        print("bean_name:", log["bean_name"])
        print("water_g:", log["water_g"])
        print("dose_g:", log["dose_g"])
        print("overall_score:", log["overall_score"])
        print("---------")

def show_log_detail(logs, index):
    print("bean_name:", logs[index]["bean_name"])
    print("water_g:", logs[index]["water_g"])
    print("dose_g:", logs[index]["dose_g"])
    print("overall_score:", logs[index]["overall_score"])
    print("---------")

logs = load_logs()

while True:
    print("1: ログ一覧")
    print("2: ログ詳細")
    print("3: ログを追加")
    print("4: 終了")

    choice = input("選んでください: ")
    if choice == "1":
        list_logs(logs)
    elif choice == "2":
        list_logs(logs)
        index_text = input("見たい番号を入力してください: ")
        if index_text.isdecimal():
            index = int(index_text)
            if 0 <= index < len(logs):
                show_log_detail(logs, index)
            else:
                print("範囲内の数字を入力してください。")
        else:
            print("数字を入力してください。")
    elif choice == "3":
        print("追加する項目を入力してください。")
        bean_name = input("bean_name: ")
        water_g = input("water_g: ")
        dose_g = input("dose_g: ")
        overall_score = input("overall_score: ")
        log = make_log(bean_name, water_g, dose_g, overall_score)
        logs.append(log)
        save_logs(logs)
        print ("新しい記録が追加されました。")
    elif choice == "4":
        break
    else:
        print("1, 2, 3, 4のうちいずれかを入力してください。")
        