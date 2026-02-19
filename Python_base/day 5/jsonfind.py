import json

target_date = "2025-04-10"

with open("app.json.log", "r", encoding="utf-8") as log:
    for line in log:
        entry = json.loads(line)

        if entry["level"] == "ERROR" and entry["timestamp"].startswith(target_date):
            print(entry["timestamp"], entry["message"])


# Здесь мы открываем файл журнала в формате JSON, читаем его построчно и разбираем каждую строку как JSON-объект. 
# Результат - словарь Python(dict). 
# Затем мы проверяем, соответствует ли уровень журнала "ERROR" и начинается ли временная метка с целевой даты. 
# Если оба условия выполняются, мы выводим временную метку и сообщение