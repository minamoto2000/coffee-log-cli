import json

def load_logs():
    try:
        with open("logs.json", "r", encoding="utf-8") as infile:
            logs = json.load(infile)
            return logs
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]

def save_logs(logs):
    with open("logs.json", "w", encoding="utf-8") as outfile:
        json.dump(logs, outfile, indent=4, ensure_ascii=False)

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
        print("豆の名前:", log["bean_name"])
        print("スコア(1~5点):", log["overall_score"])
        print("---------")

def show_log_detail(logs, index):
    print("豆の名前:", logs[index]["bean_name"])
    print("湯量(g):", logs[index]["water_g"])
    print("豆の量(g):", logs[index]["dose_g"])
    print("スコア(1~5点):", logs[index]["overall_score"])
    print("---------")

def no_records():
    print("記録がありません。")

def print_invalid_input():
    print("正しい値を入力してください。")

logs = load_logs()

while True:
    print("1: ログ一覧")
    print("2: ログ詳細")
    print("3: ログを追加")
    print("4: 終了")

    choice = input("メニューを選んでください。: ")
    if choice == "1":
        if len(logs) == 0:
            no_records()
            continue
        list_logs(logs)
    elif choice == "2":
        if len(logs) == 0:
            no_records()
            continue
        list_logs(logs)
        index_text = input("見たい番号を入力してください。: ")
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
        bean_name = input("豆の名前: ")
        
        bean_name = bean_name.strip()
        if bean_name == "":
            print_invalid_input()
            continue
        
        water_g = input("湯量(1g 以上): ")
        water_g = water_g.strip()
        if water_g.isdecimal():
            water_g = int(water_g)
            if water_g < 1:
                print_invalid_input()
                continue

        else:
            print_invalid_input()
            continue

        dose_g = input("豆の量(1g 以上): ")
        dose_g = dose_g.strip()
        if dose_g.isdecimal():
            dose_g = int(dose_g)
            if dose_g < 1:
                print_invalid_input()
                continue
        else:
            print_invalid_input()
            continue

        overall_score = input("スコア(1~5点): ")
        overall_score = overall_score.strip()
        if overall_score.isdecimal():
            overall_score = int(overall_score)
            if overall_score < 1 or overall_score > 5:
                print_invalid_input()
                continue
        else:
            print_invalid_input()
            continue

        log = make_log(bean_name, water_g, dose_g, overall_score)
        logs.append(log)
        save_logs(logs)
        print("新しい記録が追加されました。")
    elif choice == "4":
        break
    else:
        print("1, 2, 3, 4のうちいずれかを入力してください。")