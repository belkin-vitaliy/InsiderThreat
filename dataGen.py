import random
import datetime
import csv

# Количество пользователей
NUM_USERS = 500


# Функции для генерации случайных данных
def generate_random_user():
    user_ids = list(range(NUM_USERS))  # уникальные идентификаторы пользователей
    names = ["User_" + str(id_) for id_ in user_ids]
    roles = random.choices(["admin", "developer", "analyst"], k=NUM_USERS)
    login_counts = [random.randint(10, 1000) for _ in range(NUM_USERS)]  # количество логинов
    access_levels = random.choices(list(range(1, 5)), k=NUM_USERS)  # уровни доступа
    session_times = [round(random.uniform(300, 3600), 2) for _ in range(NUM_USERS)]  # средняя длительность сессии
    var_activity = [round(random.uniform(0.1, 10), 2) for _ in range(NUM_USERS)]  # вариация активности

    # Генерация времени последнего входа в указанном формате
    last_login_times = [
        (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30)),
         datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59)))
         for _ in range(NUM_USERS)
    ]

    formatted_last_login_times = [
        f"{date.strftime('%Y-%m-%d %H:%M:%S')},{str(time).zfill(8)}"
        for date, time in last_login_times
    ]

    return {
        "user_id": user_ids,
        "name": names,
        "role": roles,
        "login_count": login_counts,
        "access_level": access_levels,
        "session_time": session_times,
        "var_activity": var_activity,
        "last_login_time": formatted_last_login_times
    }


users = generate_random_user()

# Сохраняем данные в файл nodes.csv
fields = ["user_id", "name", "role", "login_count", "access_level", "session_time", "var_activity", "last_login_time"]

with open('data/nodes1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    rows = zip(users["user_id"], users["name"], users["role"], users["login_count"],
               users["access_level"], users["session_time"], users["var_activity"], users["last_login_time"])
    writer.writerows(rows)

# Количество ресурсов
NUM_RESOURCES = 200

# Количество событий
NUM_EVENTS = 10000


def generate_random_events():
    event_types = ["access", "modification", "deletion"]  # разные виды взаимодействий
    timestamps = [(datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))).isoformat() for _ in
                  range(NUM_EVENTS)]
    weights = [random.uniform(0.1, 1) for _ in range(NUM_EVENTS)]  # веса связей
    source_users = random.choices(users["user_id"], k=NUM_EVENTS)  # выбираем случайных пользователей
    target_resources = random.choices(list(range(NUM_RESOURCES)), k=NUM_EVENTS)  # целевые ресурсы
    event_types_list = random.choices(event_types, k=NUM_EVENTS)  # типы событий

    return {
        "event_id": list(range(NUM_EVENTS)),
        "source_user": source_users,
        "target_resource": target_resources,
        "event_type": event_types_list,
        "timestamp": timestamps,
        "weight": weights
    }


events = generate_random_events()

# Сохраняем данные в файл edges.csv
fields = ["event_id", "source_user", "target_resource", "event_type", "timestamp", "weight"]

with open('data/edges1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    rows = zip(events["event_id"], events["source_user"], events["target_resource"],
               events["event_type"], events["timestamp"], events["weight"])
    writer.writerows(rows)


# Функция для генерации ресурсов
def generate_random_resources():
    types = ["file", "database", "api", "service"]  # типы ресурсов
    frequencies = [random.randint(10, 1000) for _ in range(NUM_RESOURCES)]  # частота обращений
    importance = random.choices(list(range(1, 5)), k=NUM_RESOURCES)  # важность ресурса
    protection_levels = random.choices(list(range(1, 5)), k=NUM_RESOURCES)  # уровень защиты

    return {
        "resource_id": list(range(NUM_RESOURCES)),
        "type": random.choices(types, k=NUM_RESOURCES),
        "frequency": frequencies,
        "importance": importance,
        "protection_level": protection_levels
    }


resources = generate_random_resources()

# Сохраняем данные в файл resources.csv
fields = ["resource_id", "type", "frequency", "importance", "protection_level"]

with open('data/resources1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    rows = zip(resources["resource_id"], resources["type"], resources["frequency"],
               resources["importance"], resources["protection_level"])
    writer.writerows(rows)