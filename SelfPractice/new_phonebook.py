def get_name_age():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    return name, age


def collect_and_store_name_age(memory):
    name, age = get_name_age()
    records.append((name, age))


records = []

for _ in range(3):
    collect_and_store_name_age(records)

    print(records)