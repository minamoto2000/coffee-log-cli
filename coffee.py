import json

def load_logs():
    try:
        with open("logs.json", "r", encoding="utf-8") as infile:
            logs = json.load(infile)
            return logs
    except FileNotFoundError:
        return[]  

def save_logs(logs):
    with open("logs.json", "w", encoding="utf-8") as outfile:
        json.dump(logs, outfile)

def make_log(bean_name, water_g, dose_g, overall_score):
    return {"bean_name": bean_name,
        "water_g": int(water_g),
        "dose_g": int(dose_g),
        "overall_score": int(overall_score),
    }

def list_logs(logs):
    for log in logs:
        print("bean_name:", log["bean_name"])
        print("water_g:", log["water_g"])
        print("dose_g:", log["dose_g"])
        print("overall_score:", log["overall_score"])
        print("---------")

def show_log_detail(logs):

    print(logs[0]["bean_name"])
    print(logs[0]["water_g"])
    print(logs[0]["dose_g"])
    print(logs[0]["overall_score"])
    print("---------")

logs = load_logs()

log = make_log("Japan", "150", "10", "8")

logs.append(log)
save_logs(logs)

show_log_detail(logs)

