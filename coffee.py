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
        "water_g": water_g,
        "dose_g": dose_g,
        "overall_score": overall_score,
    }

def list_logs(logs):
    for index, log in enumerate(logs):
        print(str(1 + index) + "件目")
        print("bean_name:", log["bean_name"])
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
    		if len(logs) == 0:
    			print("表示する項目がありません。")
    			continue
        list_logs(logs)
    elif choice == "2":
        if len(logs) == 0:
            print("記録がありません。")
            continue
        list_logs(logs)
        index_text = input("見たい番号を入力してください: ")
        if index_text.isdecimal():
            index = int(index_text)
            internal_index = index - 1 
            if 0 <= internal_index < len(logs):
                show_log_detail(logs, internal_index)
            else:
                print("範囲内の数字を入力してください。")
        else:
            print("数字を入力してください。")

    elif choice == "3":
        print("追加する項目を入力してください。")
        bean_name = input("bean_name: ")
        
        water_g = input("water_g: ")
        if water_g.isdecimal():
            water_g = int(water_g)
        else:
            print("数字を入力してください。")
            continue

        dose_g = input("dose_g: ")
        if dose_g.isdecimal():
            dose_g = int(dose_g)
        else:
            print("数字を入力してください。")
            continue

        overall_score = input("overall_score: ")
        if overall_score.isdecimal():
            overall_score = int(overall_score)
        else:
            print("数字を入力してください。")
            continue

        log = make_log(bean_name, water_g, dose_g, overall_score)
        logs.append(log)
        save_logs(logs)
        print("新しい記録が追加されました。")
    elif choice == "4":
        break
    else:
        print("1, 2, 3, 4のうちいずれかを入力してください。")
        