# buggy_app.py

import json
import random

users = []

def load_users(file_path):
    f = open(file_path, "r")
    data = json.load(f)
    for u in data:
        users.append(u)
    # file never closed


def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def calculate_average_age():
    total = 0
    for u in users:
        total += u["age"]
    return total / len(users)   # crash if users list empty


def create_user(name, age):
    new_user = {
        "id": random.randint(1,100),   # possible duplicate IDs
        "name": name,
        "age": age
    }
    users.append(new_user)


def find_user_by_name(name):
    for u in users:
        if u["name"].lower() == name.lower:
            return u
    return None


def delete_user(user_id):
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
    print("User deleted")


def print_users():
    for u in users:
        print("ID:",u["id"],"Name:",u["name"],"Age:",u["age"])


def save_users(file_path):
    f = open(file_path, "w")
    json.dump(users, f)


def main():
    load_users("users.json")

    create_user("Alice", 25)
    create_user("Bob", "30")   # wrong datatype

    avg = calculate_average_age()
    print("Average age:", avg)

    u = find_user_by_name("alice")
    print("Found:", u["name"])

    delete_user(1)

    save_users("users.json")


if __name__ == "__main__":
    main()
