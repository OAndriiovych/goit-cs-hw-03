from pymongo import MongoClient


# Функція для виведення всіх записів із колекції
def read_all_records(collection):
    records = collection.find({})
    for record in records:
        print(record)


# Функція для виведення інформації про кота за ім'ям
def read_record_by_name(collection, name):
    record = collection.find_one({"name": name})
    if record:
        print(record)
    else:
        print("Кіт з іменем '{}' не знайдено.".format(name))


# Функція для оновлення віку кота за ім'ям
def update_age_by_name(collection, name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print("Вік кота '{}' оновлено до {}.".format(name, new_age))
    else:
        print("Кіт з іменем '{}' не знайдено.".format(name))


# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_feature_by_name(collection, name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print("Характеристику '{}' додано до кота '{}'.".format(new_feature, name))
    else:
        print("Кіт з іменем '{}' не знайдено.".format(name))


# Функція для видалення запису з колекції за ім'ям тварини
def delete_record_by_name(collection, name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Запис про кота '{}' видалено.".format(name))
    else:
        print("Кіт з іменем '{}' не знайдено.".format(name))


# Функція для видалення всіх записів із колекції
def delete_all_records(collection):
    result = collection.delete_many({})
    print("Всі записи в колекції видалено. Кількість видалених записів: {}.".format(result.deleted_count))


# Додавання тестових даних
def add_test_data(collection):
    test_data = [
        {"name": "Barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
        {"name": "Murka", "age": 5, "features": ["чорна"]},
        {"name": "Pushok", "age": 2, "features": ["сірий"]},
        {"name": "Tom", "age": 4, "features": ["полосатий"]},
        {"name": "Whiskers", "age": 6, "features": ["білий"]},
        {"name": "Fluffy", "age": 1, "features": ["білий"]},
    ]

    collection.insert_many(test_data)
    print("Додано {} тестових записів.".format(len(test_data)))


if __name__ == "__main__":
    # Підключення до бази даних
    database_url = "database_url"  # Посилання на базу даних відправви у формі
    client = MongoClient(database_url)
    db = client.get_database()
    collection = db["cats"]
    add_test_data(collection)

    read_all_records(collection)
    read_record_by_name(collection, "barsik")
    update_age_by_name(collection, "barsik", 4)
    add_feature_by_name(collection, "barsik", "ласкавий")
    delete_record_by_name(collection, "barsik")
    delete_all_records(collection)
